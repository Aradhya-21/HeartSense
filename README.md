# HeartSense: Heart Disease Prediction System

```markdown
# HeartSense: Heart Disease Prediction System

![HeartSense](https://img.shields.io/badge/HeartSense-Predictive%20Health-blueviolet.svg)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-orange.svg)
![Python](https://img.shields.io/badge/Python-3.8%2B-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

A comprehensive machine learning system for predicting heart disease risk using clinical parameters. HeartSense leverages advanced algorithms to provide accurate cardiovascular health assessments.

## 🌟 Features

- **Advanced Predictive Models**: Multiple machine learning algorithms for accurate predictions
- **User-Friendly Interface**: Intuitive web-based and command-line interfaces
- **Comprehensive Analysis**: Detailed data visualization and model interpretation
- **Real-time Predictions**: Instant risk assessment based on clinical parameters
- **Data Security**: Secure handling of sensitive health information

## 📋 Project Overview

HeartSense is designed to assist healthcare professionals and individuals in assessing heart disease risk factors through machine learning. The system analyzes various clinical parameters to provide actionable insights about cardiovascular health.

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Aradhya-21/HeartSense.git
   cd HeartSense
   ```

2. **Set up virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Usage

**Web Application:**
```bash
python app.py
```
Visit `http://localhost:5000` in your browser.

**Command Line Interface:**
```bash
python predict.py --age 45 --sex 1 --cp 2 --trestbps 130 --chol 250 --fbs 0 --restecg 1 --thalach 150 --exang 0 --oldpeak 2.3 --slope 1 --ca 1 --thal 2
```

**Jupyter Notebooks:**
Explore the `notebooks/` directory for data analysis and model experimentation.

## 📊 Dataset

The system utilizes the Cleveland Heart Disease dataset from UCI Machine Learning Repository, featuring:

- **303 patient records**
- **14 clinical attributes** including:
  - Age, sex, chest pain type
  - Resting blood pressure, cholesterol levels
  - Electrocardiographic results
  - Maximum heart rate achieved
  - Exercise-induced angina
  - ST depression induced by exercise
  - Slope of the peak exercise ST segment
  - Number of major vessels colored by fluoroscopy
  - Thalassemia

## 🧠 Machine Learning Models

HeartSense implements and compares multiple algorithms:

- **Random Forest Classifier**
- **Logistic Regression**
- **Support Vector Machine (SVM)**
- **Gradient Boosting (XGBoost)**
- **Neural Networks**
- **K-Nearest Neighbors (KNN)**

## 📈 Performance Metrics

Our best-performing model achieves:

- **Accuracy**: 88.5%
- **Precision**: 89.2%
- **Recall**: 87.8%
- **F1-Score**: 88.5%
- **AUC-ROC**: 0.93

## 🗂️ Project Structure

```
HeartSense/
├── app.py                 # Flask web application
├── predict.py            # Command-line prediction script
├── train_model.py        # Model training script
├── requirements.txt      # Python dependencies
├── data/                 # Dataset directory
│   └── processed/        # Processed data files
├── models/               # Trained model files
├── notebooks/            # Jupyter notebooks for exploration
├── src/                  # Source code modules
│   ├── preprocessing.py  # Data preprocessing
│   ├── models.py         # Model definitions
│   └── utils.py          # Utility functions
├── static/               # Web static files
│   ├── css/
│   ├── js/
│   └── images/
├── templates/            # HTML templates
└── tests/                # Unit tests
```

## 🔧 Customization

### Adding New Models
1. Implement your model in `src/models.py`
2. Add training logic in `train_model.py`
3. Update the prediction pipeline in `predict.py` and `app.py`

### Using Your Own Data
1. Place your dataset in the `data/` directory
2. Update the data loading paths in `src/preprocessing.py`
3. Retrain models with `python train_model.py`

## 🤝 Contributing

We welcome contributions to HeartSense! Please follow these steps:

1. Fork the project
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please read our [Contributing Guidelines](CONTRIBUTING.md) for more details.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **UCI Machine Learning Repository** for the heart disease dataset
- **Scikit-learn** team for the machine learning library
- **Flask** team for the web framework
- **Contributors** and open-source community

## 📞 Support

If you have any questions or issues:

1. Check the [Issues](https://github.com/Aradhya-21/HeartSense/issues) page
2. Create a new issue if your problem isn't already addressed
3. Email: [Your Email] (optional)

## 🔮 Future Enhancements

- [ ] Mobile application version
- [ ] Integration with wearable devices
- [ ] Additional health parameters
- [ ] Multi-language support
- [ ] Advanced visualization dashboard

---

<div align="center">
Made with ❤️ by <a href="https://github.com/Aradhya-21">Aradhya Srivastava</a>
</div>
```
