from flask import Flask, request, jsonify, Blueprint
from services.DataService import DataService
from utils import Constants

sd_bp = Blueprint('sensor', __name__)
PREFIX = '/sensor/'
service = DataService(container_name_key=Constants.SENSOR_DATA_CONTAINER)


@sd_bp.route(f'{PREFIX}/health', methods=['GET'])
def health_check():
    return jsonify({'message': 'Service is healthy'})


@sd_bp.route(f'{PREFIX}/create', methods=['POST'])
def create():
    data = request.json
    item = service.create_item(data)
    return jsonify(item), 201


@sd_bp.route(f'{PREFIX}/read/<item_id>', methods=['GET'])
def read(item_id):
    item = service.read_item(item_id)
    return jsonify(item)


@sd_bp.route(f'{PREFIX}/update/<item_id>', methods=['PUT'])
def update(item_id):
    data = request.json
    item = service.update_item(item_id, data)
    return jsonify(item)


@sd_bp.route(f'{PREFIX}/delete/<item_id>', methods=['DELETE'])
def delete(item_id):
    service.delete_item(item_id)
    return jsonify({'message': 'Item deleted successfully'})


@sd_bp.route(f'{PREFIX}/fetch-records/<device_id>', methods=['GET'])
def fetch_records(device_id):
    page = int(request.args.get('page', 1))
    page_size = int(request.args.get('page_size', 10))
    response = service.fetch_records(device_id, page, page_size)
    return jsonify(response)
