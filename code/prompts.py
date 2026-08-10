!pip install openai --upgrade -q
import pandas as pd
import time
from openai import OpenAI
from google.colab import userdata
 
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=userdata.get("keyopenrouter"))
 
 
df_excel = pd.read_excel("prompts.xlsx")
prompts = []
current_id = 1
 
for _, row in df_excel.iterrows():
    if pd.notna(row['Category']):
        prompts.append({"id": current_id, "category": f"{row['Category']}Mono", "text": str(row['Monolingual']).strip()})
        current_id += 1
        prompts.append({"id": current_id, "category": f"{row['Category']}Bi", "text": str(row['Bilingual']).strip()})
        current_id += 1
        prompts.append({"id": current_id, "category": f"{row['Category']}Tri", "text": str(row['Trilingual']).strip()})
        current_id += 1
#insert one of the instruction texts below
for i in prompts:
    i["text"] = "Instruction texts: [Translate the following text into English. Provide only the translation. Do not include any explanations, notes, or conversational filler. ] and [Solve the given logical task. Keep your reasoning very short and concise. Use strictly this format: Explanation: [1 short sentence]; Answer: [Direct final answer]. ]" + i["text"]
 
results = []
 
for i in prompts:
    print(f"Processing Prompt {i['id']}...")
 
    row = {"ID": i["id"], "Category": i["category"], "Prompt": i["text"]}
 
    geminiout = client.chat.completions.create(
        model="google/gemini-3.1-pro-preview",
        messages=[{"role": "user", "content": i["text"]}],
        temperature=0.0,
        max_tokens=10000,
        timeout=45.0)
 
    gptout = client.chat.completions.create(
        model="openai/gpt-5.5",
        messages=[{"role": "user", "content": i["text"]}],
        temperature=0.0,
        max_tokens=10000,
        timeout=45.0)
 
    qwenout = client.chat.completions.create(
        model="qwen/qwen3.5-397b-a17b",
        messages=[{"role": "user", "content": i["text"]}],
        temperature=0.0,
        max_tokens=10000,
        timeout=45.0)
 
    row["Gemini"] = geminiout.choices[0].message.content
    row["GPT"] = gptout.choices[0].message.content
    row["Qwen"] = qwenout.choices[0].message.content
    results.append(row)
    time.sleep(3)
 
df = pd.DataFrame(results)
df.to_csv("code_switching_results.csv", index=False, sep=";", encoding='utf-8-sig')
display(df.head())
