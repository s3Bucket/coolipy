from coolipy.requests import CoolifySession, ProjectService, ServiceService, ResourceService

class N8nService:
    def __init__(self, session: CoolifySession):
        if not isinstance(session, CoolifySession):
            raise TypeError(f"session must be CoolifySession, got {type(session).__name__}")
        self._projectService = ProjectService(session)
        self._projectService = ServiceService(session)
        self._projectService = ResourceService(session)

