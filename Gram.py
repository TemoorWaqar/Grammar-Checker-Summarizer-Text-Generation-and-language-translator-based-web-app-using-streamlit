import streamlit as st
import pickle
from happytransformer import TTSettings

def app():
    
    happy_tt = pickle.load(open('Grammer1.pkl','rb'))
    
    
    html_temp = """
    <div style="background:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;"> Grammar Corrector </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)
    text = st.text_area("")
    
    b = """ <style> div.stButton > button:first-child { background-color: #00FFFF; }
    </style>"""
    
    st.markdown(b, unsafe_allow_html = True)
    
    top_k_sampling_settings = TTSettings(do_sample=True, top_k=20, temperature=0.7, min_length=1, max_length=100)
    
    
    if st.button("Correct"):
        result = happy_tt.generate_text(text, args=top_k_sampling_settings)
        
        st.success(result.text)