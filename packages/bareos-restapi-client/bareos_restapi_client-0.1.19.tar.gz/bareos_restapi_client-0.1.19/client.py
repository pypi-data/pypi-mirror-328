import requests
from bareos_restapi_client.models import *

class BareosRestApiClient:
    def __init__(self, base_url: str, username: str, password: str):
        self.base_url = base_url
        self.username = username
        self.password = password
        self.token = None
        self.headers = {
            "Content-Type": "application/json"
        }
        self.login_for_access_token()

    def login_for_access_token(self):
        url = f"{self.base_url}/token"
        data = {
            "username": self.username,
            "password": self.password,
            "grant_type": "password"
        }
        response = requests.post(url, data=data, headers={"Content-Type": "application/x-www-form-urlencoded"})
        response.raise_for_status()
        token_data = response.json()
        self.token = token_data['access_token']
        self.headers["Authorization"] = f"Bearer {self.token}"

    def _request(self, method, url, **kwargs):
        # NOTE(sean): pathlib.Path를 문자열로 변환하는 전처리 필요
        if "json" in kwargs:
            for key, value in kwargs["json"].items():
                if isinstance(value, pathlib.Path):
                    kwargs["json"][key] = str(value)
        if "headers" not in kwargs:
            kwargs["headers"] = self.headers
        response = requests.request(method, url, **kwargs)
        if response.status_code == 401:  # Unauthorized
            self.login_for_access_token()
            kwargs["headers"]["Authorization"] = f"Bearer {self.token}"
            response = requests.request(method, url, **kwargs)
        response.raise_for_status()
        return response.json()


    #
    # Reload
    #
    def read_director_time(self):
        url = f"{self.base_url}/control/directors/reload"
        return self._request("PUT", url)


    #
    # Client
    #
    def create_client(self, client_data: clientResource):
        url = f"{self.base_url}/configuration/clients"
        return self._request("POST", url, json=client_data.dict())

    def delete_client(self, client_name: str):
        url = f"{self.base_url}/configuration/clients/{client_name}"
        return self._request("DELETE", url)

    def get_clients(self):
        url = f"{self.base_url}/configuration/clients"
        return self._request("GET", url)


    #
    # Fileset
    #
    def create_fileset(self, fileset_data: filesetResource):
        url = f"{self.base_url}/configuration/filesets"
        return self._request("POST", url, json=fileset_data.dict())

    def delete_fileset(self, fileset_name: str):
        url = f"{self.base_url}/configuration/filesets/{fileset_name}"
        return self._request("DELETE", url)

    def get_filesets(self):
        url = f"{self.base_url}/configuration/filesets"
        return self._request("GET", url)


    #
    # Job
    #
    def create_job(self, job_data: jobResource):
        url = f"{self.base_url}/configuration/jobs"
        return self._request("POST", url, json=job_data_dict)

    def delete_job(self, job_name: str):
        url = f"{self.base_url}/configuration/jobs/{job_name}"
        return self._request("DELETE", url)

    def get_jobs(self):
        url = f"{self.base_url}/configuration/jobs"
        return self._request("GET", url)


    #
    # Pool
    #
    def create_pool(self, pool_data: poolResource):
        url = f"{self.base_url}/configuration/pools"
        return self._request("POST", url, json=pool_data.dict())

    def delete_pool(self, pool_name: str):
        url = f"{self.base_url}/configuration/pools/{pool_name}"
        return self._request("DELETE", url)

    def get_pools(self):
        url = f"{self.base_url}/configuration/pools"
        return self._request("GET", url)


    #
    # Schedule
    #
    def create_schedule(self, schedule_data: scheduleResource):
        url = f"{self.base_url}/configuration/schedules"
        return self._request("POST", url, json=schedule_data.dict())

    def delete_schedule(self, schedule_name: str):
        url = f"{self.base_url}/configuration/schedules/{schedule_name}"
        return self._request("DELETE", url)

    def get_schedules(self):
        url = f"{self.base_url}/configuration/schedules"
        return self._request("GET", url)


    #
    # Storage
    #
    def create_storage(self, storage_data: storageResource):
        url = f"{self.base_url}/configuration/storage"
        return self._request("POST", url, json=storage_data.dict())

    def delete_storage(self, storage_name: str):
        url = f"{self.base_url}/configuration/storages/{storage_name}"
        return self._request("DELETE", url)

    def get_storages(self):
        url = f"{self.base_url}/configuration/storages"
        return self._request("GET", url)
