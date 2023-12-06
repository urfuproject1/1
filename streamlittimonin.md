import io
import streamlit as st

from PIL import Image



def load_image():
   #Cоздание формы для загрузки изображения
   #Форма для загрузки изображения средствами стримлит
  uploaded_file = st.file_uploader(
      label='выберите изображение для распознавания')
  if uploaded_file is not None:
   # получение загруженного изображения
      image_data = uploaded_file.getvalue()
   #показ загруженного изображения
      st.image(image_data)
   # возврат изображения в формате пил
      return Image.open(io.BytesIO(image_data))
  else: 
      return None
   # выводим заголовок
st.title('Классификация изображений')
  # вызываем функциюю создания формы загрузки изображения
img = load_image() 
