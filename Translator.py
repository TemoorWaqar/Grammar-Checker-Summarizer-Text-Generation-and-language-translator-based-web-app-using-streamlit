import googletrans

from googletrans import Translator
import streamlit as st

def app():

    html_temp = """
    <div style="background:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;"> Language Translation </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)
    
    b = """ <style> div.stButton > button:first-child { background-color: #00FFFF; }
    </style>"""
    
    st.markdown(b, unsafe_allow_html = True)
    
    translator = Translator()
    
    language = googletrans.LANGUAGES
    languageV = list(language.values())
    languageV1 = list(language.values())
    lang1 = language.keys()
    
    col1, col2 = st.columns(2)
    
    lang_in = col1.selectbox('From', languageV)
    lang_out = col2.selectbox('To', languageV1)
    
    
    input = st.text_input("Enter Text")
    
    
    if st.button("Translate"):
        
        result = translator.translate(input, src=lang_in, dest=lang_out)
        
        st.success(result.text)


