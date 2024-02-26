from flask import Flask, request, jsonify
from services import SensorDataService

app = Flask(__name__)
PREFIX = '/sensor/'
sensorDataService = SensorDataService.SensorDataService()


@app.route(f'{PREFIX}/create', methods=['POST'])
def create():
    data = request.json
    item = sensorDataService.create_item(data)
    return jsonify(item), 201


@app.route(f'{PREFIX}/read/<item_id>', methods=['GET'])
def read(item_id):
    item = sensorDataService.read_item(item_id)
    return jsonify(item)


@app.route(f'{PREFIX}/update/<item_id>', methods=['PUT'])
def update(item_id):
    data = request.json
    item = sensorDataService.update_item(item_id, data)
    return jsonify(item)


@app.route(f'{PREFIX}/delete/<item_id>', methods=['DELETE'])
def delete(item_id):
    sensorDataService.delete_item(item_id)
    return jsonify({'message': 'Item deleted successfully'})


if __name__ == '__main__':
    app.run(debug=True)
