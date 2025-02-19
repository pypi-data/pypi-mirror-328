# Bareos REST API Client

`Bareos REST API` 에 대한 파이썬 클라이언트 모듈입니다.

## 설치

```bash
pip install bareos_restapi_client
```

## 사용법

```py
# e.g.
from bareos_restapi_client import models
from bareos_restapi_client import BareosRestApiClient

client = BareosRestApiClient(base_url='', username='', password='')

client_data = models.clientResource(
    name="testuser",
    address="10.0.0.1",
    password="supersecret",
    connectionfromclienttodirector="yes",
    connectionfromdirectortoclient="no",
    heartbeatinterval="60",
    tlsenable="no",
    tlsrequire="no",
    enabled="yes"
)

response = client.create_client(client_data=client_data)
```
