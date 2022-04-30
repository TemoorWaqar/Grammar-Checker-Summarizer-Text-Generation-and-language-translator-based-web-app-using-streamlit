import streamlit as st
import pickle
from happytransformer import TTSettings

def app():
    
    happy_c_t_f = pickle.load(open('ctf.pkl','rb'))
    
    
    html_temp = """
    <div style="background:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;"> Convert Casual Language to Formal Language </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)
    
    
    top_k_sampling_settings = TTSettings(do_sample=True, top_k=20, temperature=0.5, min_length=1, max_length=100)

    
    text = st.text_area("")
    
     # I would like to play chess with you while we watch television.
    
    
    
    b = """ <style> div.stButton > button:first-child { background-color: #00FFFF; }
    </style>"""
    
    st.markdown(b, unsafe_allow_html = True)
    
    
    if st.button("Formal"):
        result = happy_c_t_f.generate_text(text, args=top_k_sampling_settings)
        
        st.success(result.text)