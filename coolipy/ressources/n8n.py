from coolipy.requests import CoolifySession, ProjectService, ServiceService, ResourceService


class N8nService:
    def __init__(self, session: CoolifySession):
        if not isinstance(session, CoolifySession):
            raise TypeError(f"session must be CoolifySession, got {type(session).__name__}")
        self._projectService = ProjectService(session)
        self._serviceService = ServiceService(session)
        self._resourceService = ResourceService(session)

    def build_n8n(self, project_name='n8n_default_project', service_name='n8n_default_service'):

        if not self._projectService.get_project_by_name(project_name):
            self._projectService.create_project({
                'name': service_name
            })

        project = self._projectService.get_project_by_name(project_name)[0]

        self._serviceService.create_service({
            "name": "n8n-cli",
            "type": "n8n",
            "project_uuid": project['uuid'],
            "environment_name": "test",
            "environment_uuid": "gowkokgks8woog88w8og44wc",
            "server_uuid": "ncskowskwwwkcok0k0wokc4g",
            "instant_deploy": False
        })

        self._serviceService.update_env(uuid="ks44ggkko080ow000og0wg4s", payload={
            "key": "SERVICE_URL_N8N",
            "value": "cli-n8n.agentsmithery.de"
        })
