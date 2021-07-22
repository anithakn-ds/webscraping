import streamlit as st 
import pandas as pd
from pickle import dump
from pickle import load
from PIL import Image
import sklearn
import base64
from sklearn.feature_extraction.text import CountVectorizer
import pickle

CV = CountVectorizer(stop_words="english")

from load_css import local_css

local_css("style.css")

st.markdown(
        f"""
<style>
    .reportview-container .main .block-container{{
        padding-top: 0rem;
    }}
   
</style>
""",
        unsafe_allow_html=True,
    )

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    width: auto;
    height: auto;
    }
  }
    
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)
                                      
set_background('Pic1.jpg')                          


col1, col2 = st.beta_columns(2)

names = "<div><span class='blue_heading'>Topic Modelling</span></div>"
col1.markdown(names, unsafe_allow_html=True)

image = Image.open('excelr.png')
col2.image(image, caption=None, width=200, use_column_width=None, clamp=False, channels='RGB', output_format='auto')

names = "<div><span class='blue'>Anitha-Suraj-Shriniwas</span></div>"
st.markdown(names, unsafe_allow_html=True)

sentence = st.text_area("Input your sentence here:")
#sentence = st.text_input('Input your sentence here:')
sentence1 = [sentence]
#loaded_model = load(open("model.pickle", 'rb'))
loaded_model = load(open('model.pickle', 'rb'))



#t_car = "The greater the distance driven per year, the more likely the total cost of ownership for an electric car will be less than for an equivalent ICE car.[53] The break even distance varies by country depending on the taxes, subsidies, and different costs of energy.  In some countries the comparison may vary by city, as a type of car may have different charges to enter different cities; for example, the UK city of London charges ICE cars more than the UK city of Birmingham does"
#t_air = "An aircraft is a vehicle or machine that is able to fly by gaining support from the air. It counters the force of gravity by using either static lift or by using the dynamic lift of an airfoil, or in a few cases the downward thrust from jet engines."
#t = [t_air]
#t1 = CV.fit_transform(t)

if(len(sentence)!=0):
    prediction = loaded_model.predict(sentence1)
    if(prediction==1): col1.markdown("<div><span class='purple'>TOPIC - CAR</span></div>",unsafe_allow_html=True)
    if(prediction==2): col1.markdown("<div><span class='purple'>TOPIC - AIRLINES</span></div>",unsafe_allow_html=True)
    if(prediction==3): col1.markdown("<div><span class='purple'>TOPIC - AUTOMOTIVE</span></div>",unsafe_allow_html=True)
