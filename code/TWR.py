!pip install tiktoken google-generativeai transformers -q
import os
import google.generativeai as genai
import pandas as pd
import tiktoken
from transformers import AutoTokenizer
 
INPUT_FILE = "code_switching_resultsx.xlsx"
SHEET_NAME = "code_switching_results"
OUTPUT_FILE = "token_word_ratiotest.xlsx"
#insert gemini API key
GOOGLE_API_KEY = "[APIkey]"
genai.configure(api_key=GOOGLE_API_KEY)
gpt_encoder = tiktoken.get_encoding("o200k_base")
gemini_model = genai.GenerativeModel("gemini-3.1-pro-preview")
qwen_tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen3.5-397B-A17B")
 
def count_gpt(text: str) -> int:
  return len(gpt_encoder.encode(text))
def count_gemini(text: str) -> int:
  return gemini_model.count_tokens(text).total_tokens
def count_qwen(text: str) -> int:
  return len(qwen_tokenizer.encode(text))
 
print("Loading")
df = pd.read_excel(INPUT_FILE, sheet_name=SHEET_NAME)
 
df["Word_Count"] = df["Prompt"].apply(lambda x: len(str(x).split()))
 
print("Calculating tokens...")
df["GPT_Tokens"] = df["Prompt"].apply(count_gpt)
df["Gemini_Tokens"] = df["Prompt"].apply(count_gemini)
df["Qwen_Tokens"] = df["Prompt"].apply(count_qwen)
 
#TWR
df["GPT_TWR"] = (df["GPT_Tokens"] / df["Word_Count"]).round(3)
df["Gemini_TWR"] = (df["Gemini_Tokens"] / df["Word_Count"]).round(3)
df["Qwen_TWR"] = (df["Qwen_Tokens"] / df["Word_Count"]).round(3)
 
df["Level"] = df["Category"].apply(
    lambda cat: next((lvl for lvl in ["Mono", "Bi", "Tri"] if str(cat).endswith(lvl)), "Other"))
 
#Save
df.to_excel(OUTPUT_FILE, index=False)
print(f"Saved to {OUTPUT_FILE}")
 
print("Mean TWR by language code-switching level")
summary = df.groupby("Level")[["GPT_TWR", "Gemini_TWR", "Qwen_TWR"]].mean()
print(summary.round(3))
