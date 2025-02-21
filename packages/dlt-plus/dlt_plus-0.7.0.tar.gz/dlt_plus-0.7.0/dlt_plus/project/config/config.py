import os
from typing import Any, ClassVar, Dict, Iterable, List, Mapping, Optional

import dlt
from dlt.common.configuration.providers import CustomLoaderDocProvider
from dlt.common.utils import exclude_keys

from dlt_plus.cache.config import CacheConfig

from dlt_plus.project.exceptions import ProjectException
from dlt_plus.project.config.typing import (
    ProjectConfig,
    SourceConfig,
    DestinationConfig,
    PipelineConfig,
    DatasetConfig,
    ProfileConfig,
    ProjectSettingsConfig,
)


def exclude_keys_from_nested(data: Mapping[str, Any], keys: Iterable[str]) -> Dict[str, Any]:
    return {
        nested_key: {
            key: value if not isinstance(value, Mapping) else exclude_keys(value, keys)
            for key, value in nested_mapping.items()
        }
        for nested_key, nested_mapping in data.items()
        if isinstance(nested_mapping, Mapping)
    }


class Project:
    DEFAULT_PROVIDER_NAME: ClassVar[str] = "dlt_project"

    def __init__(
        self,
        config: ProjectConfig,
        settings: ProjectSettingsConfig,
    ):
        self._config = config
        self._settings = settings

    @property
    def settings(self) -> ProjectSettingsConfig:
        return self._settings

    @property
    def config(self) -> ProjectConfig:
        return self._config

    @property
    def current_profile(self) -> str:
        return self._settings["current_profile"]

    @property
    def project_dir(self) -> str:
        return self._settings["project_dir"]

    @property
    def name(self) -> str:
        return self._settings.get("name") or os.path.basename(self.project_dir.rstrip(os.path.sep))

    @property
    def default_profile(self) -> str:
        return self._settings.get("default_profile")

    def provider(self, provider_name: Optional[str] = None) -> CustomLoaderDocProvider:
        provider_name = provider_name or self.DEFAULT_PROVIDER_NAME
        return CustomLoaderDocProvider(provider_name, lambda: self._to_provider_config_doc())

    def register(self, provider_name: Optional[str] = None) -> None:
        dlt.config.register_provider(self.provider(provider_name))

    def _to_provider_config_doc(self) -> Dict[str, Any]:
        """Converts the ProjectConfig to document compatible with dlt configuration layout.
        ProjectConfig is a provider config doc with a few extra fields. We also
        rename "destinations" to "destination" (which we should do in OSS).
        """
        # this also clones the dictionary
        filtered = exclude_keys(self._config, ["profiles", "project"])
        # rename the destination to destinations
        if "destinations" in filtered:
            filtered["destination"] = filtered.pop("destinations")
        return exclude_keys_from_nested(filtered, {"type"})

    @property
    def sources(self) -> Dict[str, SourceConfig]:
        return self._config.get("sources") or {}

    @property
    def destinations(self) -> Dict[str, DestinationConfig]:
        return self._config.get("destinations") or {}

    @property
    def profiles(self) -> Dict[str, ProfileConfig]:
        return self._config.get("profiles") or {}

    @property
    def pipelines(self) -> Dict[str, PipelineConfig]:
        return self._config.get("pipelines") or {}

    @property
    def transformations(self) -> Dict[str, Any]:
        return self._config.get("transformations") or {}

    @property
    def caches(self) -> Dict[str, CacheConfig]:
        return self._config.get("caches") or {}

    @property
    def datasets(self) -> Dict[str, DatasetConfig]:
        return self._config.get("datasets") or {}

    def resolve_dataset_destinations(self, dataset_name: str) -> List[str]:
        """Infers possible destinations from the pipelines if not explicitly limited"""
        dataset_config = self.datasets.get(dataset_name) or {}
        available_destinations = dataset_config.get("destination")

        # if no explicit destinations, take them from defined pipelines
        # TODO: move this to entity manager so we can also check dataseta and pipleine
        # not explicitly defined in config
        if available_destinations is None:
            available_destinations = []
            for pipeline_config in self.pipelines.values():
                if pipeline_config:
                    if dataset_name == pipeline_config.get("dataset_name"):
                        if destination_name := pipeline_config.get("destination"):
                            available_destinations.append(destination_name)

        if not available_destinations:
            raise ProjectException(
                self.project_dir,
                f"Destination(s) are not specified for dataset '{dataset_name}' and cannot be "
                "inferred from pipelines. Please use `destination` property to define a list of "
                "destinations where dataset may be present.",
            )
        return list(set(available_destinations))
