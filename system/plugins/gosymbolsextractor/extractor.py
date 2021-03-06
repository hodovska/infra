from infra.system.core.meta.metaprocessor import MetaProcessor
from infra.system.artefacts.artefacts import ARTEFACT_GOLANG_PROJECT_PACKAGES, ARTEFACT_GOLANG_PROJECT_EXPORTED_API
import logging
from infra.system.helpers.artefact_schema_validator import ArtefactSchemaValidator
from infra.system.helpers.utils import getScriptDir
from gofed_lib import gosymbolsextractor

CONFIG_SOURCE_CODE_DIRECTORY = "resource"
CONFIG_SKIPPED_DIRECTORIES = "directories_to_skip"
DATA_PROJECT = "project"
DATA_COMMIT = "commit"
DATA_IPPREFIX = "ipprefix"

class GoSymbolsExtractor(MetaProcessor):
	"""
	Input:
	 - directory to parse
	 - directories to skip
	Input(json):
	 {
	 "source_code_directory": "...",
	 "skipped_directories": "...,...,..."
	 }
	Output:
	 - exported API
	 - imported packages
	 - occurence of imported packages
	 - test directories
	 - main packages
	 - is Godeps directory present (an others)?
	Configuration:
	 - verbose mode
	 - log directory
	 To make the class config indepenent, all flags
	 are passed via class methods.
	"""

	def __init__(self, input_schema = "%s/input_schema.json" % getScriptDir(__file__)):
		MetaProcessor.__init__(
			self,
			input_schema
		)

		"""Setting implicit flags"""
		self.verbose = False
		self.skip_errors = False

		"""set implicit output"""
		# project
		self.project = ""
		# commit
		self.commit = ""
		# ipprefix
		self.ipprefix = ""

		"""set implicit states"""
		self.directory = ""
		self.noGodeps = []

		self.gosymbolsextractor = None

	def setVerbose(self):
		self.verbose = True

	def setSkipErrors(self):
		self.skip_errors = True

	def setData(self, data):
		self.data = data

		if not self._validateInput(data):
			return False

		# set directory with source codes to parse
		self.directory = data[CONFIG_SOURCE_CODE_DIRECTORY]

		# optional, set a list of directories to be skipped during parsing
		if CONFIG_SKIPPED_DIRECTORIES in data:
			self.noGodeps = data[CONFIG_SKIPPED_DIRECTORIES]

		# optional, project, commit, ipprefix
		if DATA_PROJECT in data:
			self.project = data[DATA_PROJECT]

		if DATA_COMMIT in data:
			self.commit = data[DATA_COMMIT]

		if DATA_IPPREFIX in data:
			self.ipprefix = data[DATA_IPPREFIX]

		self.gosymbolsextractor = gosymbolsextractor.GoSymbolsExtractor(
			self.directory,
			self.noGodeps,
			self.ipprefix,
			verbose = self.verbose,
			skip_errors = self.skip_errors
		)

		return True

	def getData(self):
		data = []

		data.append(self._generateGolangProjectPackagesArtefact())
		# TODO(jchaloup): move validation to unit-tests
		validator = ArtefactSchemaValidator(ARTEFACT_GOLANG_PROJECT_PACKAGES)
		if not validator.validate(data[0]):
			logging.error("%s is not valid" % ARTEFACT_GOLANG_PROJECT_PACKAGES)
			return {}

		data.append(self._generateGolangProjectExportedAPI())
		# TODO(jchaloup): move validation to unit-tests
		validator = ArtefactSchemaValidator(ARTEFACT_GOLANG_PROJECT_EXPORTED_API)
		if not validator.validate(data[1]):
			logging.error("%s is not valid" % ARTEFACT_GOLANG_PROJECT_EXPORTED_API)
			return {}

		return data

	def _generateGolangProjectPackagesArtefact(self):
		artefact = {}

		# set artefact
		artefact["artefact"] = ARTEFACT_GOLANG_PROJECT_PACKAGES

		# project credentials
		artefact["project"] = self.project
		artefact["commit"] = self.commit
		artefact["ipprefix"] = self.ipprefix

		data = self.gosymbolsextractor.getProjectPackages()

		artefact["data"] = data

		return artefact

	def _generateGolangProjectExportedAPI(self):
		data = {}

		# set artefact
		data["artefact"] = ARTEFACT_GOLANG_PROJECT_EXPORTED_API

		# project credentials
		data["project"] = self.project
		data["commit"] = self.commit

		data["packages"] = self.gosymbolsextractor.getProjectExportedAPI()

		return data

	def execute(self):
		return self.gosymbolsextractor.extract()

