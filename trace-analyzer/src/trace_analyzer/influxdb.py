from influxdb_client.client.influxdb_client_async import InfluxDBClientAsync

from trace_analyzer.process import process

async def influxdb_main():
    """Main InfluxDB loop"""
    with InfluxDBClientAsync.from_env_properties() as client:
        if not isinstance(client, InfluxDBClientAsync):
            raise TypeError("Client is not an instance of InfluxDBClientAsync.")
        ready = await client.ping()
        if not ready:
            raise ConnectionError("InfluxDB client is not ready.")
        print("InfluxDB client is ready.")

        version = await client.version()
        print(f"InfluxDB version: {version}")

        async for record in data_stream(client):
            if record:
                write_data(client, record)



async def data_stream(client: InfluxDBClientAsync):
    async for record in client.query_api().query_stream('from(bucket:"otel") |> range(start: -1h)'):
        data = process(record)
        yield data

async def write_data(client: InfluxDBClientAsync, data):
    await client.write_api().write(bucket="otel", record=data)
    print(f"Wrote data: {data}")