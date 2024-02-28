from azure.appconfiguration import AzureAppConfigurationClient
from azure.cosmos import CosmosClient
from utils import Constants


class DatabaseClient:
    def __init__(self, container_name):
        app_config_cs = Constants.APP_CONFIG_CONNECTION_STRING
        app_config_client = AzureAppConfigurationClient.from_connection_string(app_config_cs)

        app_config_label = Constants.APP_CONFIG_LABEL

        cosmos_db_endpoint = app_config_client.get_configuration_setting(key=Constants.COSMOS_DB_ENDPOINT,
                                                                         label=app_config_label).value
        cosmos_db_key = app_config_client.get_configuration_setting(key=Constants.COSMOS_DB_KEY,
                                                                    label=app_config_label).value
        database_name = app_config_client.get_configuration_setting(key=Constants.DATABASE_NAME,
                                                                    label=app_config_label).value

        self.client = CosmosClient(cosmos_db_endpoint, cosmos_db_key)
        self.database = self.client.get_database_client(database_name)
        self.container = self.database.get_container_client(container_name)

    def create_item(self, data):
        item = self.container.create_item(body=data)
        return item

    def read_item(self, item_id):
        item = self.container.read_item(item_id, partition_key=item_id)
        return item

    def update_item(self, item_id, data):
        item = self.container.replace_item(item_id, body=data)
        return item

    def delete_item(self, item_id):
        self.container.delete_item(item_id, partition_key=item_id)

    def fetch_records(self, device_id, page, page_size):
        skip = (page - 1) * page_size

        query = f"SELECT * FROM c WHERE c.device_id = '{device_id}' ORDER BY c._ts DESC OFFSET {skip} LIMIT {page_size}"
        results = list(self.container.query_items(query=query, enable_cross_partition_query=True))

        # Get total count of records
        total_count = self.container.query_items(
            query=f"SELECT VALUE COUNT(1) FROM c WHERE c.device_id = '{device_id}'",
            enable_cross_partition_query=True).next()

        # Create paginated response
        response = {
            'total_count': total_count,
            'page': page,
            'page_size': page_size,
            'records': results
        }

        return response
