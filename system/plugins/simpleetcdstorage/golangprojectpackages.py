from artefactdriver import ArtefactDriver
from system.artefacts.artefacts import ARTEFACT_GOLANG_PROJECT_PACKAGES

class GolangProjectPackagesDriver(ArtefactDriver):

	def __init__(self):

		ArtefactDriver.__init__(self, ARTEFACT_GOLANG_PROJECT_PACKAGES)