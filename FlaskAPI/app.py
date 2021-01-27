import pickle
from flask import Flask, request, jsonify
from models.ml_model import predict_rent


app = Flask('rent_prediction')

@app.route('/predict', methods=['POST'])
def predict():
    vehicle = request.get_json()
    print(vehicle)
    with open('./models/rent_model_file.p', 'rb') as f_in:
        model = pickle.load(f_in)
        f_in.close()
    predictions = predict_rent(vehicle, model)

    result = {
        'rent_prediction': list(predictions)
    }
    return jsonify(result)

@app.route('/ping', methods=['GET'])
def ping():
    return "Pinging Model!!"