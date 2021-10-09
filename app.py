from flask import Flask, render_template, request, url_for
import numpy as np
import pickle


model = pickle.load(open('model.pkl', 'rb')) 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/types')
def types():
    return render_template('types.html')

@app.route('/predictheartdisease')
def predictheartdisease():
    return render_template('predictheartdisease.html')
    
@app.route('/predict', methods =['POST','GET'])
def predict():
    
    # Put all form entries values in a list 
    features = [float(i) for i in request.form.values()]
    # Convert features to array
    array_features = [np.array(features)]
    # Predict features
    prediction = model.predict(array_features)
    
    output = prediction
    # Check the output values and retrive the result with html tag based on the value
    if output == 1:
        return render_template('predictheartdisease.html', 
                               result = 'The patient is not likely to have heart disease!')
    else:
        return render_template('predictheartdisease.html', 
                               result = 'The patient is likely to have heart disease!')

@app.route('/prevention')
def prevention():
    return render_template('prevention.html')

if __name__ == '__main__':
    app.run(debug=True)
