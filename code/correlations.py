import pandas as pd
from scipy.stats import pearsonr, spearmanr
 
tab1 = pd.read_excel('scoring_matrixanalyzed.xlsx')
tab2 = pd.read_excel('token_word_ratiotest.xlsx')
all_data = pd.merge(tab1, tab2, on='ID')
print("GPT")
df_gpt = all_data[['GPT Total', 'GPT_TWR']].dropna()
corr_p, p_p = pearsonr(df_gpt['GPT_TWR'], df_gpt['GPT Total'])
corr_s, p_s = spearmanr(df_gpt['GPT_TWR'], df_gpt['GPT Total'])
print(f"Pearson: {round(corr_p, 3)} (p={round(p_p, 3)})")
print(f"Spearman: {round(corr_s, 3)} (p={round(p_s, 3)})")
 
print("GEMINI")
df_gemini = all_data[['Gemini Total', 'Gemini_TWR']].dropna()
corr_p, p_p = pearsonr(df_gemini['Gemini_TWR'], df_gemini['Gemini Total'])
corr_s, p_s = spearmanr(df_gemini['Gemini_TWR'], df_gemini['Gemini Total'])
print(f"Pearson: {round(corr_p, 3)} (p={round(p_p, 3)})")
print(f"Spearman: {round(corr_s, 3)} (p={round(p_s, 3)})")
 
print("QWEN")
df_qwen = all_data[['Qwen Total', 'Qwen_TWR']].dropna()
corr_p, p_p = pearsonr(df_qwen['Qwen_TWR'], df_qwen['Qwen Total'])
corr_s, p_s = spearmanr(df_qwen['Qwen_TWR'], df_qwen['Qwen Total'])
print(f"Pearson: {round(corr_p, 3)} (p={round(p_p, 3)})")
print(f"Spearman: {round(corr_s, 3)} (p={round(p_s, 3)})")
