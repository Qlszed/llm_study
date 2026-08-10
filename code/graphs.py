import pandas as pd
import matplotlib.pyplot as plt
 
d1 = pd.read_excel('scoring_matrixanalyzed.xlsx')
d2 = pd.read_excel('token_word_ratiotest.xlsx')
df = pd.merge(d1, d2, on='ID')
df['Prompt Category'] = df['Category_x'].str.replace('Mono','').str.replace('Bi','').str.replace('Tri','')
 
res1 = df.groupby('Prompt Category')[['Gemini Total', 'GPT Total', 'Qwen Total']].mean()
res1 = res1.reindex(['Regular', 'Inversion', 'Lexical', 'Logical'])
colors = ['red', 'green', 'blue']
ax = res1.plot(kind='bar', color=colors, legend=False)
plt.title('Accuracy')
ax.legend(['Gemini', 'GPT', 'Qwen'], bbox_to_anchor=(1.02, 1), loc='upper left')
plt.tight_layout()
plt.show()
 
res2 = df.groupby('Level')[['Gemini_TWR', 'GPT_TWR', 'Qwen_TWR']].mean().reset_index()
res2['Level'] = pd.Categorical(res2['Level'], categories=['Mono', 'Bi', 'Tri'], ordered=True)
res2 = res2.sort_values('Level')
 
plt.plot(res2['Level'], res2['Gemini_TWR'], color='red', label='Gemini', marker='o')
plt.plot(res2['Level'], res2['GPT_TWR'], color='green', label='GPT', marker='o')
plt.plot(res2['Level'], res2['Qwen_TWR'], color='blue', label='Qwen', marker='o')
 
plt.legend()
plt.title('TWR')
plt.show()
