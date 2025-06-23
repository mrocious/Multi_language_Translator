import streamlit as st
from transformers.utils import logging
from transformers import pipeline
import torch

# Silence most transformer logs
logging.set_verbosity_error()

# Load the model once at startup
@st.cache_resource
def load_translator():
    return pipeline(
        task="translation",
        model="facebook/nllb-200-distilled-600M",
        torch_dtype=torch.bfloat16,
        device=0 if torch.cuda.is_available() else -1
    )

translator = load_translator()

# Minimal working set of languages (replace with full later)
LANGUAGES = {
    "English": "eng_Latn",
    "French": "fra_Latn",
    "Spanish": "spa_Latn",
    "Arabic": "arb_Arab",
    "Chinese (Simplified)": "zho_Hans",
    "Hindi": "hin_Deva",
    "Russian": "rus_Cyrl",
    "Portuguese": "por_Latn",
    "Urdu": "urd_Arab",
    "Swahili": "swh_Latn",
    "Zulu": "zul_Latn",
}

def main():
    st.set_page_config(page_title="NLLB Translation", layout="centered")
    st.title("🌐 FLORES-200 Translation App")

    st.header("1. Enter text to translate")
    input_text = st.text_area("Text Input", height=200)

    st.header("2. Select Languages")
    col1, col2 = st.columns(2)
    with col1:
        source_lang = st.selectbox("Source Language", list(LANGUAGES.keys()))
    with col2:
        target_lang = st.selectbox("Target Language", list(LANGUAGES.keys()))

    st.header("3. Translate")
    if st.button("Translate"):
        if not input_text.strip():
            st.warning("Please enter some text.")
            return

        if source_lang == target_lang:
            st.info("Source and target languages are the same.")
            st.write(input_text)
            return

        with st.spinner("Translating..."):
            result = translator(
                input_text,
                src_lang=LANGUAGES[source_lang],
                tgt_lang=LANGUAGES[target_lang]
            )[0]['translation_text']

        st.success("Translated Text")
        st.write(result)

if __name__ == "__main__":
    main()
