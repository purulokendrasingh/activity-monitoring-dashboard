from azure.appconfiguration import AzureAppConfigurationClient
from utils import Constants
from data.DatabaseClient import DatabaseClient


class DataService:
    def __init__(self, container_name_key):
        app_config_cs = Constants.APP_CONFIG_CONNECTION_STRING
        app_config_client = AzureAppConfigurationClient.from_connection_string(app_config_cs)

        app_config_label = Constants.APP_CONFIG_LABEL
        container_name = app_config_client.get_configuration_setting(key=container_name_key,
                                                                     label=app_config_label).value
        self.database_client = DatabaseClient(container_name=container_name)

    def create_item(self, data):
        item = self.database_client.create_item(data)
        return item

    def read_item(self, item_id):
        item = self.database_client.read_item(item_id)
        return item

    def update_item(self, item_id, data):
        item = self.database_client.update_item(item_id, data)
        return item

    def delete_item(self, item_id):
        self.database_client.delete_item(item_id)

    def fetch_records(self, device_id, page, page_size):
        response = self.database_client.fetch_records(device_id, page, page_size)
        return response
