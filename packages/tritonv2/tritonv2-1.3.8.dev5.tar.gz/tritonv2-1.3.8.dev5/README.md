# tritonv2
A client library for promote triton official client

## Installation

```bash
pip install tritonv2==1.3.8.dev5
```

## Usage

First, you need to create a client object.

```python
from tritonv2.client_factory import TritonClientFactory
server_url = "localhost:8000"

http_client = TritonClientFactory.create_grpc_client(server_url)
or
async with TritonClientFactory.create_http_aio_client(server_url) as http_aio_client
or 
grpc_client = TritonClientFactory.create_grpc_client(server_url)
or
async with TritonClientFactory.create_grpc_aio_client(server_url) as grpc_aio_client
```
In addition, you can set retry for grpc client:<br>
```python
client = TritonClientFactory.create_grpc_client(server_url, num_retries=3,max_interval_secs=20,base_interval_secs=0.3)
```
for http client we have default setting:<br>
```python
NUMBER_RETRIES = 3
MAX_INTERVAL_SECS = 20
BASE_INTERVAL_SECS = 0.3
```

Now you can easy use the client to send requests to the server.

for server:

```python
client.server_live()
client.server_ready()
client.server_metadata()
```

for model:

```python
client.model_metadata(model_name)
client.model_config(model_name)
client.model_ready(model_name)
client.model_statistics(model_name)
```

for infer:
```python
client.model_infer(model_name, inputs, model_version, outputs)
client.stream_infer(inputs_iterator)
```

for repository:
```python
client.repository_index()
client.repository_model_load(model_name)
client.repository_model_unload(model_name)
```

for system shared memory:
```python
client.system_shared_memory_status()
client.system_shared_memory_register()
client.system_shared_memory_unregister()
```

for cuda shared memory:
```python
client.cuda_shared_memory_status()
client.cuda_shared_memory_register()
client.cuda_shared_memory_unregister()
```

for trace setting:
```python
client.trace_setting()
client.get_trace_settings()
```



