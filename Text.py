import streamlit as st
import pickle

def app():
    gpt2 = pickle.load(open('text_gerneration.pkl','rb'))
    
    
    html_temp = """
    <div style="background:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;"> Text Generator </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)
    
    b = """ <style> div.stButton > button:first-child { background-color: #00FFFF; }
    </style>"""
    
    st.markdown(b, unsafe_allow_html = True)
    
    text1 = st.text_input("")
    
    if st.button("Generate Text"):
        
        result1 = gpt2.generate_text(text1)
        
        st.success(result1.text)