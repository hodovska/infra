from artefactdriver import ArtefactDriver
from infra.system.artefacts.artefacts import ARTEFACT_GOLANG_PROJECT_DISTRIBUTION_EXPORTED_API

class GolangProjectDistributionExportedApiDriver(ArtefactDriver):

	def __init__(self):

		ArtefactDriver.__init__(self, ARTEFACT_GOLANG_PROJECT_DISTRIBUTION_EXPORTED_API)
