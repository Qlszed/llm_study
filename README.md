# llm_study
This repository contains the raw data tables and Python scripts referenced in
"Subword Fragmentation: Evaluating LLM Error Patterns in Kazakh-Russian-English Code-Switching"
(Zhanadil Yenbayev, Pioneer Academics, 2026).

This repository is structured as follows:

artifacts/
- `scoring_matrixanalyzed.xlsx` - per-response accuracy and Faithfulness scores for all 360 model responses, percentage tables
- `token_word_ratiotest.xlsx` - token counts, word counts, and TWR for all 120 prompts
- `code_switching_resultsx.xlsx` - the full set of 120 Monolingual/Bilingual/Trilingual prompts used in the study and all 360 model responses
- `sample.xlsx` - a random sample of 72 responses given to a second reviewer to evaluate through discussion

code/
- `prompts.py` - This script builds the 120 prompts from the base sentence set, sends each one to GPT-5.5, Gemini 3.1 Pro Preview, and Qwen3.5 397B A17B through OpenRouter, and saves all responses to a CSV file.
- `TWR.py` - This script computes the word count and token count of each prompt using each model’s tokenizer, then calculates the Token-to-Word Ratio (TWR) for each response.
- `correlations.py` - This script merges the scoring data with the TWR data and computes Pearson and Spearman correlations between TWR and accuracy score for each model.
- `graphs.py` - This script produces Figure 1 (average accuracy by model and category) and Figure 2 (average TWR by code-switching level).

The Python scripts are also listed in the Appendices of the paper. Requirements are included in the scripts, since each was ran independently via the Google Colab platform.
Model identifiers used: openai/gpt-5.5, google/gemini-3.1-pro-preview, qwen/qwen3.5-397b-a17b, (temperature=0.0, max_tokens=10000, timeout=45.0).
