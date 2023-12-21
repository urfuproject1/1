import streamlit as st
import streamlit.components.v1 as components
from transformers import pipeline
from io import BytesIO
from PIL import Image

def main():
    overlay_opacity = 0.5
    
    # Пользовательский CSS для изменения заднего фона
    page_bg_img = f"""
    <style>
    .main {{
        background-image: url("https://avatars.dzeninfra.ru/get-zen_doc/1718877/pub_61cacc9bd1e72b6a321017e8_62335a98f781ab27c5f97f55/scale_1200");
        background-size: cover;
    }}
    .main::before {{
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: black;
        opacity: {overlay_opacity};
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

    current_page = st.session_state.get("current_page", "home")
    
    # Определение текущей страницы и её отображение
    if current_page == "home":
        home_page()
    elif current_page == "second":
        second_page()

def StyleButton(widget_label, font_color='white', background_color='transparent', width='200px', height='60px', margin_top='10px'):
    """
    Функция для стилизации кнопки с использованием пользовательского CSS.

    Parameters:
    - widget_label (str): Текст на кнопке.
    - font_color (str): Цвет текста кнопки.
    - background_color (str): Цвет фона кнопки.
    - width (str): Ширина кнопки.
    - height (str): Высота кнопки.
    - margin_top (str): Отступ сверху кнопки.

    Returns:
    None
    """
    htmlstr = f"""
        <script>
            var elements = window.parent.document.querySelectorAll('button');
            for (var i = 0; i < elements.length; ++i) {{ 
                if (elements[i].innerText == '{widget_label}') {{ 
                    elements[i].style.color = '{font_color}';
                    elements[i].style.background = '{background_color}';
                    elements[i].style.border = '2px solid white';  // Добавляем белую границу
                    elements[i].style.width = '{width}';
                    elements[i].style.height = '{height}';
                    elements[i].style.margin = 'auto';  // Центрируем кнопку
                    elements[i].style.display = 'block';  // Делаем блочным элементом для использования margin:auto
                    elements[i].style.marginTop = '{margin_top}';
                }}
            }}
        </script>
        """
    components.html(f"{htmlstr}", height=0, width=0)

def home_page():
    # Пользовательский CSS для главной страницы
    custom_css = """
    <style>
    h1 {
        color: white;
        font-size: 50px;
        text-shadow: 4px 4px 4px rgba(0, 0, 0, 0.8);
        white-space: nowrap;
        margin-left: -15%;
    }
    .underline {
        border: 1px solid white;
        margin-top: -30px;  /* Отрицательное значение отступа для приближения к заголовку */
    }
    .subtitle {
        color: rgba(255, 255, 255, 0.7);
        font-size: 30px;
        text-align: center;
        margin-top: -10px;
        line-height: 1.2;
        font-weight: bold;
    }
    .subtitle2 {
        color: rgba(255, 255, 255, 0.7);
        font-size: 30px;
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
        white-space: nowrap;
        margin-left: -25%;
    }
    </style>
    """

    st.title("Классификация достопримечательностей")
    st.markdown(custom_css, unsafe_allow_html=True)
    st.markdown("<hr class='underline'>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Мы определяем название достопримечательностей Москвы<br> с помощью нейросети</p>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle2'>Вы можете загрузить свою фотографию и узнать название достопримечательности</p>", unsafe_allow_html=True)
    
    # Создание кнопки "Попробовать" с использованием пользовательского CSS
    StyleButton('Попробовать', width='250px', height='70px', margin_top='200px')
    
    # Обработка события нажатия на кнопку
    if st.button("Попробовать", key="home_button"):
        st.session_state["current_page"] = "second"
        st.experimental_rerun()

def second_page():
    # Пользовательский CSS для второй страницы
    custom_css = """
    <style>
    h1 {
        color: white;
        font-size: 50px;
        text-shadow: 4px 4px 4px rgba(0, 0, 0, 0.8);
        white-space: nowrap;
        margin-left: -15%;
    }
    .underline {
        border: 1px solid white;
        margin-top: -30px;  /* Отрицательное значение отступа для приближения к заголовку */
    }
    .subtitle3 {
        color: rgba(255, 255, 255, 0.7);
        font-size: 30px;
        font-weight: bold;
        text-align: center;
        white-space: nowrap;
        margin-top: 20px;
    }
    </style>
    """
    st.title("Классификация достопримечательностей")
    st.markdown(custom_css, unsafe_allow_html=True)
    st.markdown("<hr class='underline'>", unsafe_allow_html=True)
    
    # Загрузка фото
    uploaded_file = st.file_uploader('', type=['jpg', 'jpeg', 'png'])
    
    # Отображение фото
    if uploaded_file is not None:
        st.image(uploaded_file, caption='', use_column_width=True)
        # используем PIL для открытия изображения из байтов
        image = Image.open(BytesIO(uploaded_file.read()))

    # Создание кнопки "Распознать" с использованием пользовательского CSS
    StyleButton('Распознать', width='250px', height='60px', margin_top='50px')
  
    # Обработка события нажатия на кнопку
    if st.button("Распознать", key="recognition_button"):
        # Вывод результата
        st.markdown("<p class='subtitle3'>Распознанная достопримечательность:</p>", 
                    unsafe_allow_html=True)
        # используем модель для классификации изображения
        run_classification(image)



def run_classification(image):
    """
    Функция запускает классификацию изображения с помощью модели
    и выводит результаты предсказания в приложении.
    image: PIL.Image, изображение для классификации
    """
    # загружаем модель
    pipe = pipeline("image-classification", model="Poliandr/moscow-attractions")
    # находим максимальный результат предсказания
    result = max(pipe(image), key=lambda x: x['score'])
    # выводим результаты предсказания в приложении
    # st.title(result['label'])
    st.markdown(f"<h1 style='text-align: center; margin: 0 auto;'>{result['label']}</h1>", unsafe_allow_html=True)
if __name__ == "__main__":
    main()
