from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the model from the pickle file
with open('scaler_model.pkl', 'rb') as file:
    scaler = pickle.load(file)

with open("Logistic_prediction.pkl", 'rb') as file:
    model = pickle.load(file)

with open("Random_Forest_Classifier.pkl", 'rb') as file:
    forest_classifier = pickle.load(file)


def preprocess_input(name, sex, urban_rural, income, gpa, parents_qualification, attendance):
    # Your preprocessing code here
    # For simplicity, let's assume 'sex' and 'urban_rural' are already encoded (0 or 1)
    parents_qualification_mapping = {'High School': 0, 'Illiterate': 1, 'Graduate': 2}

    # Map income options to numerical values
    income_mapping = {'Low': 0, 'Medium': 1, 'High': 2}

    # Create a numpy array with the preprocessed values
    input_data = np.array([
        income_mapping[income], gpa, parents_qualification_mapping[parents_qualification], attendance
    ])
    return input_data


def predict_dropout_probability(model, input_data):
    # Your prediction code here
    # Assuming binary classification
    input_data = np.reshape(input_data, (1, -1))
    dropout_probability = model.predict_proba(input_data)[:, 1]
    return dropout_probability[0]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        name = request.form['name']
        sex = int(request.form['sex'])
        urban_rural = int(request.form['urban_rural'])
        income = request.form['income']
        gpa = float(request.form['gpa'])
        parents_qualification = request.form['parents_qualification']
        attendance = float(request.form['attendance'])

        gpa_avg = scaler.transform([[gpa, attendance]])
        if income == "Low":
            income_input = [1, 0]
        elif income == "Medium":
            income_input = [0, 1]
        else:
            income_input = [0, 0]

        if parents_qualification == "Illiterate":
            quali_input = [1, 0]
        elif parents_qualification == "High School":
            quali_input = [0, 1]
        else:
            quali_input = [0, 0]

        to_be_predicted = [gpa_avg[0][0], gpa_avg[0][1], sex, urban_rural, income_input[0], income_input[1], quali_input[0], quali_input[1]]
        prediction = forest_classifier.predict_proba([to_be_predicted])
        print(forest_classifier.feature_importances_)


        # Preprocess input data
        # input_data = preprocess_input(name, sex, urban_rural, income, gpa, parents_qualification, attendance)

        # Predict dropout probability
        dropout_probability = 100

        # Render the result template
        return render_template('result.html', name=name, dropout_probability=prediction)


if __name__ == '__main__':
    app.run(debug=True)
