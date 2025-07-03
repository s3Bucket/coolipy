from ._client import CoolifySession


class ServiceService:
    def __init__(self, session: CoolifySession):
        if not isinstance(session, CoolifySession):
            raise TypeError(f"session must be CoolifySession, got {type(session).__name__}")
        self._client = session

    def create_service(self, payload):
        return self._client.request("POST", f"/api/v1/services", json=payload)

    def list_services(self):
        return self._client.request("GET", f"/api/v1/services")

    def update_env(self, uuid, payload):
        return self._client.request("PATCH", f"/api/v1/services/{uuid}/envs", json=payload)
