from infra.system.artefacts import artefacts
from .golangprojectdistributionexportedapi import GolangProjectDistributionExportedApiDriver
from .golangprojectdistributionpackages import GolangProjectDistributionPackagesDriver
from .golangipprefixtopackagename import GolangIpprefixToPackageNameDriver
from .golangprojectexportedapi import GolangProjectExportedApiDriver
from .golangprojectpackages import GolangProjectPackagesDriver
from .golangprojectinfofedora import GolangProjectInfoFedoraDriver
from .golangprojectapidiff import GolangProjectApiDiffDriver
from .golangprojecttopackagename import GolangProjectToPackageNameDriver
from .golangprojectcontentmetadata import GolangProjectContentMetadataDriver
from .golangprojectrepositoryinfo import GolangProjectRepositoryInfoDriver
from .golangprojectrepositorycommit import GolangProjectRepositoryCommitDriver
from .golangprojectdistributioninfo import GolangProjectDistributionInfoDriver
from .golangprojectdistributionbuild import GolangProjectDistributionBuildDriver

class ArtefactDriverFactory:

	def build(self, artefact):

		if artefact == artefacts.ARTEFACT_GOLANG_PROJECT_DISTRIBUTION_EXPORTED_API:
			return GolangProjectDistributionExportedApiDriver()

		if artefact == artefacts.ARTEFACT_GOLANG_PROJECT_DISTRIBUTION_PACKAGES:
			return GolangProjectDistributionPackagesDriver()

		if artefact == artefacts.ARTEFACT_GOLANG_IPPREFIX_TO_PACKAGE_NAME:
			return GolangIpprefixToPackageNameDriver()

		if artefact == artefacts.ARTEFACT_GOLANG_PROJECT_EXPORTED_API:
			return GolangProjectExportedApiDriver()

		if artefact == artefacts.ARTEFACT_GOLANG_PROJECT_PACKAGES:
			return GolangProjectPackagesDriver()

		if artefact == artefacts.ARTEFACT_GOLANG_PROJECT_INFO_FEDORA:
			return GolangProjectInfoFedoraDriver()

		if artefact == artefacts.ARTEFACT_GOLANG_PROJECTS_API_DIFF:
			return GolangProjectApiDiffDriver()

		if artefact == artefacts.ARTEFACT_GOLANG_PROJECT_TO_PACKAGE_NAME:
			return GolangProjectToPackageNameDriver()

		if artefact == artefacts.ARTEFACT_GOLANG_PROJECT_CONTENT_METADATA:
			return GolangProjectContentMetadataDriver()

		if artefact == artefacts.ARTEFACT_GOLANG_PROJECT_REPOSITORY_INFO:
			return GolangProjectRepositoryInfoDriver()

		if artefact == artefacts.ARTEFACT_GOLANG_PROJECT_REPOSITORY_COMMIT:
			return GolangProjectRepositoryCommitDriver()

		if artefact == artefacts.ARTEFACT_GOLANG_PROJECT_DISTRIBUTION_INFO:
			return GolangProjectDistributionInfoDriver()

		if artefact == artefacts.ARTEFACT_GOLANG_PROJECT_DISTRIBUTION_BUILD:
			return GolangProjectDistributionBuildDriver()

		raise ValueError("Invalid artefact: %s" % artefact)