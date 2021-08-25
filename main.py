import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("hello world")
st.write("show progress bar")
'Start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)



left, right = st.columns(2)

button = left.button('display to right')
if button:
    right.write('press!!')

expander = st.expander('contact')
expander.write('write here')

# text = st.text_input('your hobby')
# 'your hobby is', text, '.'

# condition = st.slider('label', 0, 100, 10)
# 'your condition is', condition, '.'


# option = st.selectbox(
#     'preffered color',
#     list(range(1,10))
# )

# 'your color is', option, '.'

# if st.checkbox('show image'):
#     img = Image.open('tokyo-sta.jpg')
#     st.image(img, caption = 'tokyo station', use_column_width=True)


