from influxdb_client.client.flux_table import FluxRecord
from influxdb_client.client.influxdb_client_async import InfluxDBClientAsync

def process(record: FluxRecord, client: InfluxDBClientAsync):
    """Process data from InfluxDB"""
    return None