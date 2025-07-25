
from coolipy.requests import CoolifySession


class ApplicationService:
    def __init__(self, session: CoolifySession):
        if not isinstance(session, CoolifySession):
            raise TypeError(f"session must be CoolifySession, got {type(session).__name__}")
        self._client = session

    def list_applications(self):
        return self._client.request("GET", "/api/v1/applications")

    def create_application_public(self, payload):
        return self._client.request("POST", "/api/v1/applications", json=payload)

    def create_application_private_gh_app(self, payload):
        return self._client.request("POST", "/api/v1/applications/private-gh-app", json=payload)

    def create_application_private_deploy_key(self, payload):
        return self._client.request("POST", "/api/v1/applications/private-deploy-key", json=payload)

    def create_application_dockerfile(self, payload):
        return self._client.request("POST", "/api/v1/applications/dockerfile", json=payload)

    def create_application_docker_image(self, payload):
        return self._client.request("POST", "/api/v1/applications/dockerimage", json=payload)

    def create_application_docker_compose(self, payload):
        return self._client.request("POST", "/api/v1/applications/dockercompose", json=payload)

    def get_application(self, uuid):
        return self._client.request("GET", f"/api/v1/applications/{uuid}")

    def delete_application(self, uuid):
        return self._client.request("DELETE", f"/api/v1/applications/{uuid}")

    def update_application(self, uuid, payload):
        return self._client.request("PATCH", f"/api/v1/applications/{uuid}", json=payload)

    def get_application_logs(self, uuid):
        return self._client.request("GET", f"/api/v1/applications/{uuid}/logs")

    def list_application_envs(self, uuid):
        return self._client.request("GET", f"/api/v1/applications/{uuid}/envs")

    def create_application_env(self, uuid, payload):
        return self._client.request("POST", f"/api/v1/applications/{uuid}/envs", json=payload)

    def update_application_env(self, uuid, env_id, payload):
        return self._client.request("PATCH", f"/api/v1/applications/{uuid}/envs/{env_id}", json=payload)

    def update_application_envs_bulk(self, uuid, payload):
        return self._client.request("PATCH", f"/api/v1/applications/{uuid}/envs", json=payload)

    def delete_application_env(self, uuid, env_id):
        return self._client.request("DELETE", f"/api/v1/applications/{uuid}/envs/{env_id}")

    def start_application(self, uuid):
        return self._client.request("GET", f"/api/v1/applications/{uuid}/start")

    def stop_application(self, uuid):
        return self._client.request("GET", f"/api/v1/applications/{uuid}/stop")

    def restart_application(self, uuid):
        return self._client.request("GET", f"/api/v1/applications/{uuid}/restart")
