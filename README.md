
## 🥦 Fruit & Vegetable Image Classifier 🍎

A simple and interactive **image classification web app** built with **TensorFlow** and **Streamlit**, designed to identify various fruits and vegetables from uploaded images.

---

### 🚀 Features

* Upload an image of a fruit or vegetable 🍉🥕
* Get instant AI-based predictions using a pre-trained CNN model
* Fun UI with animations like balloons on successful predictions
* Easy navigation with sidebar menu

---

### 📊 Dataset

The model was trained on a custom dataset containing:

* **Fruits**: Apple, Banana, Orange, Kiwi, Mango, Watermelon, etc.
* **Vegetables**: Carrot, Tomato, Potato, Cucumber, Onion, etc.

Each class contains:

* 100 training images
* 10 validation images
* 10 test images

---

### 🛠️ Requirements

Here are the main Python packages required:

```
streamlit
tensorflow
numpy

```




---

### 📂 Project Structure

```
.
├── app.py                 # Streamlit app (main file)
├── trained_model.h5       # Pre-trained TensorFlow model
├── labels.txt             # Label file mapping predictions to class names
├── home_img.jpg           # Image for home page
└── README.md              # Project documentation
```
