from ._client import CoolifySession


class ProjectService:
    def __init__(self, session: CoolifySession):
        if not isinstance(session, CoolifySession):
            raise TypeError(f"session must be CoolifySession, got {type(session).__name__}")
        self._client = session

    def list_projects(self):
        return self._client.request("GET", "/api/v1/projects")

    def get_project(self, uuid):
        return self._client.request("GET", f"/api/v1/projects/{uuid}")

    def create_project(self, payload):
        return self._client.request("POST", f"/api/v1/projects", json=payload)
