from coolipy.requests import CoolifySession, ProjectService, ServiceService


class UtilService:
    def __init__(self, session: CoolifySession):
        if not isinstance(session, CoolifySession):
            raise TypeError(f"session must be CoolifySession, got {type(session).__name__}")
        self._projectService = ProjectService(session)
        self._serviceService = ServiceService(session)

    def prune_services_from_environment(self, project_name,
                                        project_env_name):

        env = self._projectService.get_projects_environment_by_name(project_name, project_env_name)[0]

        for service in self._serviceService.list_services():
            if service['environment_id'] == env['id']:
                self._serviceService.delete_service(service['uuid'])
