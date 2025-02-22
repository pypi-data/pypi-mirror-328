from .config import ConfigManager
from .exceptions import ConfigurationError
from .service_locator import ServiceLocator


def sais_foundation(cls):
    config = ConfigManager().config

    for section in ["foundation", "unified_data_access", "ml"]:
        if hasattr(config, section):
            setattr(cls, f"_{section}_config", getattr(config, section))

    if not config.foundation.experiment_name:
        raise ConfigurationError("Experiment name is required in foundation config")

    if config.ml.enabled:
        _init_mlflow_integration(cls)

    if config.unified_data_access.enabled:
        _init_data_access_client(cls)

    return cls


def _init_mlflow_integration(cls):
    from ..ml import mlflow_integration

    ml_instance = mlflow_integration.initialize(
        experiment_name=cls._foundation_config.experiment_name, **vars(cls._ml_config)
    )
    ServiceLocator.set_ml_manager(ml_instance)


def _init_data_access_client(cls):
    from ..unified_data_access import client

    data_client = client.initialize(
        **vars(cls._unified_data_access_config)
    )
    ServiceLocator.set_data_client(data_client)
