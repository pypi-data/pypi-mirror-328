from pydantic import BaseModel, Extra, validator
from typing import Dict, Any, List, Optional, Union
import os
import yaml


class FoundationConfig(BaseModel):
    experiment_name: str = "default_experiment"


class UnifiedDataAccessConfig(BaseModel):
    enabled: bool = False
    cached: bool = True
    token: Optional[str] = None
    data_access: List[Dict[str, Any]] = []


class MLFlowConfig(BaseModel):
    class ModelRepoConfig(BaseModel):
        model_uri: str = ""
        registered: bool = True
        name: str = "default_model"
        tag: Dict[str, str] = {}
        version: str = "0.1.0"

    enabled: bool = True
    auto_log: bool = True
    system_tracing: bool = True
    model_repo: ModelRepoConfig = ModelRepoConfig()
    metrics: Union[Dict[str, List[str]], List[str]] = {}

    @validator("metrics", pre=True)
    def transform_metrics(cls, v):
        if isinstance(v, list):
            return {"metrics": v}
        return v

    artifacts: Union[Dict[str, List[str]], List[str]] = []
    parameters: Dict[str, Any] = {}


class DynamicConfig(BaseModel):
    class Config:
        extra = Extra.allow


class SAISConfig(DynamicConfig):
    foundation: FoundationConfig = FoundationConfig()
    unified_data_access: UnifiedDataAccessConfig = UnifiedDataAccessConfig()
    ml: MLFlowConfig = MLFlowConfig()


class ConfigManager:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance._load_config()
        return cls._instance

    def _load_config(self):
        config_path = os.path.join(os.getcwd(), "sais_foundation.yaml")
        if not os.path.exists(config_path):
            raise FileNotFoundError("sais_foundation.yaml not found in project root")

        with open(config_path) as f:
            raw_config = yaml.safe_load(f)

        self.config = SAISConfig(**raw_config)

    def get(self, key: str, default=None) -> Any:
        return getattr(self.config, key, default)


class DictProxy:
    def __init__(self, data: dict):
        self._data = data

    def __getattr__(self, name: str) -> Any:
        if name in self._data:
            value = self._data[name]
            if isinstance(value, dict):
                return DictProxy(value)
            return value
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")

    def __repr__(self):
        return f"<DictProxy {self._data}>"


class DynamicConfigAccessor:
    def __getattr__(self, name: str) -> Any:
        value = ConfigManager().get(name)
        if isinstance(value, dict):
            return DictProxy(value)
        return value


config = DynamicConfigAccessor()
