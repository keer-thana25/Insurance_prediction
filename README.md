# Insurance Premium Prediction

This project is a Machine Learning web application that predicts the insurance premium amount based on user inputs such as age, annual income, policy term, and sum assured. The application uses a trained ML model and provides predictions through an interactive Streamlit web interface.

## Project Workflow

1. Data Collection – Raw insurance dataset is stored in the `data/raw` folder.
2. Data Preprocessing – Cleaning and splitting the dataset into training and testing sets.
3. Feature Engineering – Transforming features and scaling the data.
4. Model Training – Training a regression model to predict insurance premiums.
5. Prediction – Loading the trained model and scaler to generate predictions.
6. Web Application – Streamlit UI to input values and get predictions.

## Project Structure

```
Insurance_prediction
│
├── artifacts
│   ├── model.pkl
│   └── scaler.pkl
│
├── data
│   ├── raw
│   └── processed
│       ├── X_train.csv
│       ├── X_test.csv
│       ├── y_train.csv
│       └── y_test.csv
│
├── src
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── model_training.py
│   └── prediction.py
│
└── app.py
```

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit

## Installation

Clone the repository:

```
git clone https://github.com/yourusername/insurance_prediction.git
cd insurance_prediction
```

Install dependencies:

```
pip install -r requirements.txt
```

## Run the Application

```
streamlit run app.py
```

The app will open in your browser where you can enter:

- Age
- Annual Income (LPA)
- Policy Term (Years)
- Sum Assured (Lakhs)

and get the predicted insurance premium.

## Features

- End-to-end ML pipeline
- Data preprocessing and feature engineering
- Model training and saving artifacts
- Interactive prediction using Streamlit
- Modular project structure

## Output

The application predicts the annual insurance premium in thousands based on the given inputs.
