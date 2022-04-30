import streamlit as st
import pickle

def app():
    
    happy_tt = pickle.load(open('model.pkl','rb'))
    
    
    html_temp = """
    <div style="background:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;"> Text Summarize </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)
    text = st.text_area("")
    
    b = """ <style> div.stButton > button:first-child { background-color: #00FFFF; }
    </style>"""
    
    st.markdown(b, unsafe_allow_html = True)
    
    
    if st.button("Summarize"):
        result = happy_tt.generate_text(text)
        
        st.success(result.text)