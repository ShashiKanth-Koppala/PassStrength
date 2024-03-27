from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)

# Load the CLASSIFIER MODEL
model = joblib.load('/Users/shashikanth/Downloads/random_forest_model.pkl')


def word(password):
    return list(password)

#LOAD THE TFIDF PICKLE FILE
tdif = joblib.load('/Users/shashikanth/Downloads/tfidf_vectorizer.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/classify-password', methods=['GET', 'POST'])  # Allow both GET(FROM FRONTEND) and POST(TO DISPLAY) requests
def classify():
    if request.method == 'POST':
        content = request.get_json()
        password = content.get('password')
        if not password:
            return jsonify({'error': 'Password is required'}), 400

        # Transform password using tfidf( USED FOR FURTHER PROCESS)
        vectorized_pass = tdif.transform([password])
        
        # Predict password strength
        prediction = model.predict(vectorized_pass)[0]

        # Return prediction as strength
        strength = prediction
        return jsonify({'strength': strength})


if __name__ == '__main__':
    app.run(debug=True)
