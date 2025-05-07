import streamlit as st
import tensorflow as tf
import numpy as np

# TensorFlow Model Prediction
def model_prediction(test_image):
    model = tf.keras.models.load_model("trained_model.h5")
    image = tf.keras.preprocessing.image.load_img(test_image, target_size=(64, 64))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.expand_dims(input_arr, axis=0)  # batch dimension
    predictions = model.predict(input_arr)
    return np.argmax(predictions)

# Page Configuration
st.set_page_config(page_title="Fruit & Vegetable Classifier", layout="centered", page_icon="🥦")

# Sidebar
st.sidebar.markdown("## 🌐 Navigation")
app_mode = st.sidebar.selectbox("Select Page", ["🏠 Home", "📖 About Project", "🔍 Prediction"])

# Home Page
if app_mode == "🏠 Home":
    st.markdown("<h1 style='text-align: center; color: green;'>🍎 Fruits & Vegetables Recognition System 🥕</h1>", unsafe_allow_html=True)
    st.image("home_img.jpg", use_container_width=True)
    st.markdown("<hr>", unsafe_allow_html=True)

# About Project
elif app_mode == "📖 About Project":
    st.markdown("<h2 style='color: purple;'>📊 About the Dataset</h2>", unsafe_allow_html=True)
    st.info("This dataset contains images of the following food items:")
    st.markdown("**Fruits:** 🍌 Banana, 🍎 Apple, 🍐 Pear, 🍇 Grapes, 🍊 Orange, 🥝 Kiwi, 🍉 Watermelon, 🍍 Pineapple, 🥭 Mango, 🍎 Pomegranate")
    st.markdown("**Vegetables:** 🥒 Cucumber, 🥕 Carrot, 🌶️ Capsicum, 🧅 Onion, 🥔 Potato, 🍋 Lemon, 🍅 Tomato, and more...")
    st.markdown("### 📁 Dataset Structure")
    st.code("1. train (100 images each)\n2. test (10 images each)\n3. validation (10 images each)")
    st.markdown("<hr>", unsafe_allow_html=True)

# Prediction Page
elif app_mode == "🔍 Prediction":
    st.markdown("<h2 style='color: teal;'>🔍 Upload an Image to Predict</h2>", unsafe_allow_html=True)
    test_image = st.file_uploader("📁 Choose an Image", type=["jpg", "png", "jpeg"])

    if test_image is not None:
        st.image(test_image, use_container_width=True, caption='Uploaded Image ✅')

    if st.button("🔮 Predict"):
        with st.spinner("Predicting... Please wait"):
            result_index = model_prediction(test_image)

            # Reading Labels
            with open("labels.txt") as f:
                labels = [line.strip() for line in f]

            prediction = labels[result_index]
            st.balloons()
            st.success(f"🎯 The model predicts it's a **{prediction.upper()}**!")
