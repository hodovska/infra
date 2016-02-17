from artefactdriver import ArtefactDriver
from infra.system.artefacts.artefacts import ARTEFACT_GOLANG_PROJECT_INFO_FEDORA

class GolangProjectInfoFedoraDriver(ArtefactDriver):

	def __init__(self):

		ArtefactDriver.__init__(self, ARTEFACT_GOLANG_PROJECT_INFO_FEDORA)
