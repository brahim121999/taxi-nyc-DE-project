from google.cloud import bigquery
from google.cloud.exceptions import NotFound

client = bigquery.Client()

datasets_name = ['taxitrips', 'transformed_data', 'views_fordashboard']
location = 'US'

def create_bigquery_dataset(dataset_name):
    dataset_id = "{}.{}".format(client.project, dataset_name)
    try:
        client.get_dataset(dataset_id)
        print("Dataset {} already exists".format(dataset_id))
    except NotFound:
        dataset = bigquery.Dataset(dataset_id)
        dataset.location = location

        dataset = client.create_dataset(dataset, timeout=30)
        print("Created dataset {}.{}".format(
            client.project, dataset.dataset_id))

for name in datasets_name:
    create_bigquery_dataset(name)