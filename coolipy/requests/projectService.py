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

    def get_project_by_name(self, name):
        return list(filter(lambda x: x['name'] == name, self.list_projects()))

    def get_projects_environment_by_uuid(self, project_uuid, env_uuid):
        return self._client.request("GET", f"/api/v1/projects/{project_uuid}/{env_uuid}")

    def create_project(self, payload):
        return self._client.request("POST", f"/api/v1/projects", json=payload)
