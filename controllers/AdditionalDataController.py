from flask import Flask, request, jsonify, Blueprint
from services.DataService import DataService
from utils import Constants

ad_bp = Blueprint('additional-data', __name__)
PREFIX = '/additional-data/'
service = DataService(container_name_key=Constants.ADDITIONAL_DATA_CONTAINER)


@ad_bp.route(f'{PREFIX}/create', methods=['POST'])
def create():
    data = request.json
    item = service.create_item(data)
    return jsonify(item), 201


@ad_bp.route(f'{PREFIX}/read/<item_id>', methods=['GET'])
def read(item_id):
    item = service.read_item(item_id)
    return jsonify(item)


@ad_bp.route(f'{PREFIX}/update/<item_id>', methods=['PUT'])
def update(item_id):
    data = request.json
    item = service.update_item(item_id, data)
    return jsonify(item)


@ad_bp.route(f'{PREFIX}/delete/<item_id>', methods=['DELETE'])
def delete(item_id):
    service.delete_item(item_id)
    return jsonify({'message': 'Item deleted successfully'})