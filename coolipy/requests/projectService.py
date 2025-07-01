class ProjectService:
    def __init__(self, client_session):
        self._client = client_session

    def list_projects(self):
        return self._client.request("GET", "/api/v1/projects")

    def get_project(self, uuid):
        return self._client.request("GET", f"/api/v1/projects/{uuid}")

    def create_project(self, payload):
        return self._client.request("POST", f"/api/v1/projects", json=payload)
