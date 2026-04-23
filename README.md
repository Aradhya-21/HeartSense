# HeartSense: Heart Disease Prediction System

![HeartSense](https://img.shields.io/badge/HeartSense-Predictive%20Health-blueviolet.svg)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-orange.svg)
![Python](https://img.shields.io/badge/Python-3.8%2B-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

HeartSense is a machine learning–powered system designed to predict the risk of heart disease using clinical health parameters. The project combines data analysis, predictive modeling, and a user-friendly interface to deliver fast and accurate cardiovascular risk assessments.

---

## 🌟 Features

* **Multiple Machine Learning Models** for improved prediction accuracy
* **Web-Based Interface** for interactive predictions
* **Command-Line Support** for quick testing and automation
* **Clinical Data Analysis** using real-world health indicators
* **Model Comparison & Evaluation** with performance metrics
* **Secure Handling** of sensitive healthcare data

---

## 📋 Project Overview

HeartSense helps healthcare professionals, researchers, and individuals assess heart disease risk through machine learning.

The system evaluates clinical parameters such as age, cholesterol, blood pressure, and heart rate to estimate cardiovascular disease probability.

---

## 🚀 Quick Start

### Prerequisites

Before running the project, ensure you have:

* Python 3.8 or higher
* pip (Python package manager)
* Git

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Aradhya-21/HeartSense.git
cd HeartSense
```

### 2. Create a Virtual Environment (Recommended)

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### Run the Web Application

```bash
python app.py
```

Open your browser and visit:

```text
http://localhost:5000
```

### Run via Command Line

```bash
python predict.py --age 45 --sex 1 --cp 2 --trestbps 130 --chol 250 --fbs 0 --restecg 1 --thalach 150 --exang 0 --oldpeak 2.3 --slope 1 --ca 1 --thal 2
```

### Explore Jupyter Notebooks

Navigate to the `notebooks/` directory for:

* Data analysis
* Feature engineering
* Model experimentation
* Visualization

---

## 📊 Dataset

HeartSense uses the **Cleveland Heart Disease Dataset** from the UCI Machine Learning Repository.

### Dataset Highlights

* **303 patient records**
* **14 clinical attributes**

### Key Features Included

* Age
* Sex
* Chest pain type
* Resting blood pressure
* Cholesterol levels
* Fasting blood sugar
* Resting ECG results
* Maximum heart rate achieved
* Exercise-induced angina
* ST depression induced by exercise
* Peak exercise ST segment slope
* Number of major vessels colored by fluoroscopy
* Thalassemia

---

## 🧠 Machine Learning Models

The project compares multiple algorithms to identify the best-performing model:

* Random Forest Classifier
* Logistic Regression
* Support Vector Machine (SVM)
* Gradient Boosting (XGBoost)
* Neural Networks
* K-Nearest Neighbors (KNN)

---

## 📈 Performance Metrics

### Best Model Performance

| Metric    | Score |
| --------- | ----- |
| Accuracy  | 88.5% |
| Precision | 89.2% |
| Recall    | 87.8% |
| F1-Score  | 88.5% |
| AUC-ROC   | 0.93  |

---

## 🗂️ Project Structure

```text
HeartSense/
├── app.py                 # Flask web application
├── predict.py             # Command-line prediction script
├── train_model.py         # Model training script
├── requirements.txt       # Project dependencies
├── data/
│   └── processed/         # Processed dataset files
├── models/                # Saved trained models
├── notebooks/             # Data exploration notebooks
├── src/
│   ├── preprocessing.py   # Data preprocessing logic
│   ├── models.py          # Model definitions
│   └── utils.py           # Utility functions
├── static/                # CSS, JS, and image assets
├── templates/             # HTML templates
└── tests/                 # Unit tests
```

---

## 🔧 Customization

### Add a New Model

1. Create the model inside `src/models.py`
2. Add training logic in `train_model.py`
3. Update prediction handling in `predict.py` and `app.py`

### Use Your Own Dataset

1. Add your dataset to the `data/` folder
2. Update preprocessing paths in `src/preprocessing.py`
3. Retrain models:

```bash
python train_model.py
```

---

## 🤝 Contributing

Contributions are welcome.

### Contribution Workflow

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature/AmazingFeature
```

3. Commit your changes

```bash
git commit -m "Add AmazingFeature"
```

4. Push to GitHub

```bash
git push origin feature/AmazingFeature
```

5. Open a Pull Request

---

## 📝 License

This project is licensed under the **MIT License**.

See the `LICENSE` file for more details.

---

## 🙏 Acknowledgments

* UCI Machine Learning Repository for the dataset
* The Scikit-learn community for ML tools
* Flask framework contributors
* Open-source contributors and developers

---

## 📞 Support

If you encounter any issues:

1. Visit the GitHub Issues page
2. Check for existing solutions
3. Create a new issue if needed

---

## 🔮 Future Enhancements

HeartSense has the potential to evolve into a more advanced healthcare intelligence platform. Future improvements can enhance prediction accuracy, usability, scalability, and real-world healthcare integration.

### Planned Enhancements

#### 📱 Mobile Application Support

Develop Android and iOS applications to allow users to access heart disease prediction features directly from smartphones.

#### ⌚ Wearable Device Integration

Integrate with smartwatches and fitness trackers to collect real-time health metrics such as heart rate, oxygen levels, and activity data.

#### 🧠 Deep Learning Models

Implement advanced deep learning techniques such as Artificial Neural Networks (ANN) and Recurrent Neural Networks (RNN) for improved predictive performance.

#### 📊 Interactive Analytics Dashboard

Build a rich dashboard with visual charts and health trend analysis to help users understand their cardiovascular risk factors.

#### 🌍 Multi-Language Support

Expand accessibility by supporting multiple languages for a broader global audience.

#### ☁️ Cloud Deployment

Deploy the application on cloud platforms such as �entity�["company","Amazon Web Services","AWS cloud platform"] (AWS), �entity�["company","Google Cloud Platform","Cloud computing platform by Google"], or �entity�["company","Microsoft Azure","Cloud computing platform by Microsoft"] to improve scalability and availability.

#### 🔐 Enhanced Security & Authentication

Add secure login systems, encrypted health records, and role-based access for healthcare professionals.

#### 🏥 Hospital System Integration

Enable integration with Electronic Health Record (EHR) systems to automatically fetch patient data.

#### 📈 Continuous Model Training

Implement automated retraining pipelines so the model improves over time with new healthcare datasets.

#### 🤖 AI Health Assistant

Introduce an AI-powered assistant that provides personalized recommendations based on patient health inputs.

---

<div align="center">"center">
  <strong>Made with ❤️ by Aradhya Srivastava</strong>
</div>
