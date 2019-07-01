from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from text_classification import Predict

app = Flask(__name__)
api = Api(app)


class ApiTextClassification(Resource):
    def post(self):
        json = request.get_json(force=True)
        model = Predict("text_classification.pkl")
        predict = model.predict([json])
        return jsonify(category=predict[0])


api.add_resource(ApiTextClassification, "/")


if __name__ == "__main__":
    app.run(debug=True)