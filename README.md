# Suspicious Email Detector

## Overview

The **Suspicious Email Detector** is an AI-powered web application built using Python, Streamlit, and machine learning models to classify email or SMS messages as spam or not spam. The app uses Natural Language Processing (NLP) techniques for text preprocessing and a machine learning model to determine whether an incoming message is spam.

### Features
- **Spam Detection**: Classifies an email or SMS as spam or not spam based on its content.
- **Preprocessing**: Cleans the text by removing unwanted characters, stopwords, and stemming words to prepare the text for machine learning.
- **Chatword Treatment**: Recognizes and replaces common chat abbreviations (e.g., "LOL", "BRB") with their full forms.

## Technologies Used

- **Python**: The main programming language for developing the app.
- **Streamlit**: For building the web app interface.
- **scikit-learn**: For machine learning model (Naive Bayes classifier).
- **NLTK**: For text preprocessing and NLP tasks.
- **pickle**: For saving and loading models and vectorizers.
- **CountVectorizer**: Converts text data into numeric format that the machine learning model can interpret.

## Setup Instructions

### Prerequisites

To run this project, you need to have Python installed on your local machine. You can download Python from [here](https://www.python.org/downloads/).

### Steps to run the app locally:

1. **Clone the repository**:
   ```
   git clone https://github.com/Warishayat/Suspicious-Email-Detector-App.git
   cd suspicious-email-detector
   ```

2. **Create a virtual environment** (optional but recommended):
   - On Windows:
     ```
     python -m venv env
     env\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     python3 -m venv env
     source env/bin/activate
     ```

3. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Run the app**:
   ```
   streamlit run app.py
   ```

   After running this command, the app will be available at `http://localhost:8501` in your browser.

## How it Works

1. **Input Text**: You can input the text of the email or SMS message into the Streamlit app.
2. **Preprocessing**: The app processes the input text by removing special characters, stopwords, and applies stemming. Common chat abbreviations are replaced with their full forms.
3. **Text Vectorization**: The cleaned text is converted into a numeric vector using `CountVectorizer`.
4. **Prediction**: The processed vector is passed to a trained machine learning model (Naive Bayes classifier). The model predicts whether the input is spam or not.
5. **Result**: The app displays the result, indicating whether the message is "Spam" or "Not Spam".

## How to Contribute

1. Fork the repository.
2. Create a new branch for your changes.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Create a pull request for review.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or suggestions, feel free to reach out at warishayat666@gmail.com`.
```
