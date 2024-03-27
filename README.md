# Password Strength Checker Using Machine Learning

## Technologies and Languages Used
- HTML
- Python
- Flask

## Dataset
Find the dataset [here](https://www.kaggle.com/datasets/bhavikbb/password-strength-classifier-dataset/data).

## Models Used
I utilized TFIDF to create vectors for corresponding passwords, which were then fed into the Random Forest Classifier for classification into three categories: Weak, Medium, and Strong.

# Model Results
The model achieved a recall and precision of approximately 95%.

## Application
The backend logic is implemented using Flask, which accepts both GET requests from the frontend for passwords and POST requests to send the password strength back to the frontend. For the frontend, a simple HTML file has been provided.

## Running the Application
To run the application locally:
1. Clone this repository.
2. Install the necessary dependencies by running `pip install -r requirements.txt`.
3. Run the Python notebook and use the pickle files of both the Random Forest Classifier and TFIDF for further implementation in Flask.





## Acknowledgments
- [Kaggle](https://www.kaggle.com/) for providing the dataset.
