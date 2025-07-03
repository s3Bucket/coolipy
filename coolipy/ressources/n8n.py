from coolipy.requests import CoolifySession, ProjectService, ServiceService, ResourceService


class N8nService:
    def __init__(self, session: CoolifySession):
        if not isinstance(session, CoolifySession):
            raise TypeError(f"session must be CoolifySession, got {type(session).__name__}")
        self._projectService = ProjectService(session)
        self._serviceService = ServiceService(session)
        self._resourceService = ResourceService(session)

    def foo(self):
        print(self._projectService.list_projects())
        response = self._resourceService.list_resources()

        for r in response:
            print(f"Name: {r['name']}, ID: {r['id']}")

        self._serviceService.create_service({
            "type": "n8n",
            "project_uuid": "fk844wwwsgc8wokowg4gk44g",
            "environment_name": "test",
            "environment_uuid": "gowkokgks8woog88w8og44wc",
            "server_uuid": "ncskowskwwwkcok0k0wokc4g",
            "instant_deploy": False
        })

        self._serviceService.update_env(uuid="ks44ggkko080ow000og0wg4s", payload={
            "key": "SERVICE_URL_N8N",
            "value": "cli-n8n.agentsmithery.de"
        })
