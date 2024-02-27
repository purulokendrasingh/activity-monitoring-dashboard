from flask import Flask, request, jsonify, Blueprint
from services.DataService import DataService
from utils import Constants

ld_bp = Blueprint('location-data', __name__)
PREFIX = '/location-data/'
service = DataService(container_name_key=Constants.LOCATION_DATA_CONTAINER)


@ld_bp.route(f'{PREFIX}/health', methods=['GET'])
def health_check():
    return jsonify({'message': 'Service is healthy'})


@ld_bp.route(f'{PREFIX}/create', methods=['POST'])
def create():
    data = request.json
    item = service.create_item(data)
    return jsonify(item), 201


@ld_bp.route(f'{PREFIX}/read/<item_id>', methods=['GET'])
def read(item_id):
    item = service.read_item(item_id)
    return jsonify(item)


@ld_bp.route(f'{PREFIX}/update/<item_id>', methods=['PUT'])
def update(item_id):
    data = request.json
    item = service.update_item(item_id, data)
    return jsonify(item)


@ld_bp.route(f'{PREFIX}/delete/<item_id>', methods=['DELETE'])
def delete(item_id):
    service.delete_item(item_id)
    return jsonify({'message': 'Item deleted successfully'})
