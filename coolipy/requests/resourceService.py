from ._client import CoolifySession


class ResourceService:
    def __init__(self, session: CoolifySession):
        if not isinstance(session, CoolifySession):
            raise TypeError(f"session must be CoolifySession, got {type(session).__name__}")
        self._client = session

    def list_resources(self):
        return self._client.request("GET", f"/api/v1/resources")
