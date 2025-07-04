from coolipy.requests import CoolifySession, ProjectService, ServiceService, ResourceService


class N8nService:
    def __init__(self, session: CoolifySession):
        if not isinstance(session, CoolifySession):
            raise TypeError(f"session must be CoolifySession, got {type(session).__name__}")
        self._projectService = ProjectService(session)
        self._serviceService = ServiceService(session)
        self._resourceService = ResourceService(session)

    def build_n8n(self, project_name='n8n_default_project',
                  project_env_name = 'production',
                  service_name='n8n_default_service'):

        existing_project = self._projectService.get_project_by_name(project_name)
        if not existing_project:
            new_project = self._projectService.create_project({
                'name': project_name
            })
            project_uuid = new_project['uuid']
        else:
            project_uuid = existing_project[0]['uuid']

        self._serviceService.create_service({
            "name": "n8n-cli",
            "type": "n8n",
            "project_uuid": project_uuid,
            "environment_name": project_env_name,
            "environment_uuid": "gowkokgks8woog88w8og44wc",
            "server_uuid": "ncskowskwwwkcok0k0wokc4g",
            "instant_deploy": False
        })

        self._serviceService.update_env(uuid="ks44ggkko080ow000og0wg4s", payload={
            "key": "SERVICE_URL_N8N",
            "value": "cli-n8n.agentsmithery.de"
        })
