# 🌐 Streamlit Translation App using NLLB-200

This project is an interactive web-based translation tool built with [Streamlit](https://streamlit.io/), powered by Meta AI's [NLLB-200 (No Language Left Behind)](https://huggingface.co/facebook/nllb-200-distilled-600M) multilingual model. It allows users to translate text between over 200 languages supported by the FLORES-200 benchmark.

---

## 🚀 Features

- 🌍 Translate between 200+ languages using FLORES-200 codes.
- ⚡ Fast and efficient model: `facebook/nllb-200-distilled-600M`.
- 🧠 Built with HuggingFace Transformers and PyTorch.
- 🖥️ Runs on both CPU and GPU (with support for `torch.bfloat16` on GPU).
- 💡 Simple and clean user interface using Streamlit.

---

## 📦 Requirements

Install the necessary Python packages using:

```bash
pip install -r requirements.txt
```

Required packages:
- `streamlit`
- `transformers`
- `torch`
- `numpy<2.0` (recommended for compatibility)

---

## ▶️ How to Run

To launch the app locally:

```bash
streamlit run app.py
```

Once running, open the provided local URL (e.g., `http://localhost:8501`) in your browser.

---

## 📚 How to Use

Once the app is running, follow these steps:

1. **Enter the text**  
   In the “Text Input” section, type or paste the sentence you want to translate.

2. **Select languages**  
   Choose the **source language** and **target language** from the dropdown menus.

3. **Click “Translate”**  
   Press the **Translate** button to generate the output. The translated text will appear below.

4. *(Optional)*  
   You can switch languages or input and re-translate as needed.

---

## 🌐 Supported Languages

Languages follow FLORES-200 standard codes, e.g.:
- English → `eng_Latn`
- French → `fra_Latn`
- Hindi → `hin_Deva`
- Chinese (Simplified) → `zho_Hans`
- Arabic → `arb_Arab`

You can extend or modify the language list in `app.py`.

---

## 🧠 Model Used

- **Model:** [`facebook/nllb-200-distilled-600M`](https://huggingface.co/facebook/nllb-200-distilled-600M)
- **Hosted via:** HuggingFace `pipeline()`
- **Supported tasks:** Translation (src_lang → tgt_lang)

---

## 📁 Project Structure

```
.
├── app.py               # Main Streamlit app
├── requirements.txt     # Python dependencies
├── README.md            # Project overview (you are here)
├── .gitignore           # Ignored files for Git
├── LICENSE              # Open-source license (MIT)
├── assets/              # (Optional) Static files like screenshots
```

---

## 📜 License

This project is licensed under the **MIT License**. See `LICENSE` for details.

---

## 🙌 Acknowledgments

- [Meta AI](https://ai.facebook.com/research/publications/no-language-left-behind/) for NLLB.
- [HuggingFace Transformers](https://huggingface.co/transformers/)
- [Streamlit](https://streamlit.io/)

---

## ✨ Future Ideas

- File upload for batch translation.
- Auto-detect source language.
- Download translated results.
- Language filtering/search bar for dropdowns.
