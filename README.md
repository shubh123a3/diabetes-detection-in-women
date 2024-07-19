# Diabetes Prediction App

This Diabetes Prediction App is designed to predict the probability of a person having diabetes based on their health data. It is built using Python and leverages the Streamlit framework for the web interface, making it user-friendly and accessible.


https://github.com/user-attachments/assets/ac344b5f-6275-45f0-99b4-654e362edb69


## Features

- **User-Friendly Interface**: The app is built with Streamlit, offering a clean and straightforward interface for users to input their data.
- **Health Data Input**: Users can input their health data through interactive widgets. The required inputs include:
  - Number of pregnancies
  - Glucose level
  - Body Mass Index (BMI)
  - Age
- **Real-Time Predictions**: Upon entering their data and clicking the 'Predict' button, users receive real-time predictions about their diabetes status.
- **Data-Driven Predictions**: The predictions are made using a machine learning model trained on historical health data. The model is loaded from a pickle file, ensuring quick and reliable predictions.

## Installation

To run this app locally, you need to have Python installed on your system. Follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies by running:
4. 4. Run the app using Streamlit:
## Dependencies

- Streamlit: For creating the web app interface.
- Pandas: For data manipulation and analysis.
- Scikit-learn: For machine learning model prediction.
- Pickle: For loading the pre-trained machine learning model.

## How It Works

The app uses a pre-trained machine learning model to predict diabetes. Users input their health data, which is then converted into a DataFrame. This DataFrame is fed into the model, which predicts the user's diabetes status.

## Contributing

Contributions to improve the app are welcome. Please feel free to fork the repository, make changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

   
