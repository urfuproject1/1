import streamlit as st
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

# Инициализация BlipProcessor и BlipForConditionalGeneration моделей
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base").to("cuda")

def main():
    # Заголовок веб-приложения
    st.title("Формирование описания к изображению")

    # Загрузка изображения через стримлит
    uploaded_file = st.file_uploader("Выберите изображение...", type="jpg")

    if uploaded_file is not None:
        # Открытие и преобразования картинки в rgb формат
        raw_image = Image.open(uploaded_file).convert('RGB')

        # Создание описания к картинке
        text = "Картинка"
        inputs = processor(raw_image, text, return_tensors="pt")
        out = model.generate(**inputs)

        # Вывод сгенерированного описания
        st.image(raw_image, caption="Загруженное изображение", use_column_width=True)
        st.write("Описание картинки:", processor.decode(out[0], skip_special_tokens=True))

        # Perform unconditional image captioning
        inputs = processor(raw_image, return_tensors="pt")
        out = model.generate(**inputs)

        # Вывод сгенерированного описания
        st.write("Описание картинки:", processor.decode(out[0], skip_special_tokens=True))

if __name__ == '__main__':
    main()