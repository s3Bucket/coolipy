import requests
from exceptions import CoolifyAPIError


class CoolifyClient:
    def __init__(self, base_url, api_key):
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/json"
        })

    def _request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.session.request(method, url, **kwargs)
        if not response.ok:
            raise CoolifyAPIError(response.status_code, response.text)
        return response.json()

    def list_projects(self):
        return self._request("GET", "/api/v1/projects")

#    def get_project(self, project_id):
#        return self._request("GET", f"/api/v1/projects/{project_id}")

#    def create_deployment(self, project_id, payload):
#        return self._request("POST", f"/api/v1/projects/{project_id}/deployments", json=payload)

#    def get_deployment_status(self, deployment_id):
#        return self._request("GET", f"/api/v1/deployments/{deployment_id}")