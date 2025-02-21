import mlflow
from typing import Any, Dict, Optional
import numpy as np


class MLflowManager:
    def __init__(self, experiment_name: str, **kwargs) -> None:
        self.url = "http://mlflow.internal.sais.com.cn"
        mlflow.set_tracking_uri(self.url)
        mlflow.set_experiment(experiment_name)

        ml_config = kwargs

        print(ml_config)

        mlflow.autolog()

        # run mlflow
        with mlflow.start_run():

            # using system_tracing
            self.system_tracing(ml_config.get("system_tracing"))

            # using log_params
            self.log_params(ml_config.get("parameters"))

            # using log_model
            self.log_model(ml_config.get("model_repo"))

            # using log_artifacts
            self.log_artifacts(ml_config.get("artifacts"))

    def system_tracing(self, enabled: bool) -> None:
        if enabled:
            mlflow.enable_system_metrics_logging()
            print("System Metrics is Enabled")
        else:
            print("System Metrics is Disabled")

    def log_model(self, params: Dict[str, Any]) -> None:
        required_fields = {"model_uri", "name", "version"}
        if missing := required_fields - params.keys():
            raise ValueError(f"Missing required fields: {missing}")
        model_uri = params["model_uri"].format(run_id=mlflow.active_run().info.run_id)

        mlflow.register_model(
            model_uri=model_uri,
            name=params["name"],
            tags={
                **params.get("tag", {}),
                "version": params["version"],
                "registered": str(params.get("registered", True)),
            },
            await_registration_for=params.get("await_registration_for", 300),
        )

    def log_params(self, params: Dict[str, Any]) -> None:
        """记录模型参数"""
        mlflow.log_params(params)

    def log_metrics(self, metrics: Dict[str, float], step: int = 0) -> None:
        """记录评估指标"""
        mlflow.log_metrics(metrics, step=step)

    def log_artifacts(self, artifact: Dict[str, Any]) -> None:
        for i in artifact:
            mlflow.log_artifacts(i)

    def set_log_artifacts(self, obj_str: str) -> None:
        mlflow.log_artifacts(obj_str)

    def set_log_params(self, key: str, val: str) -> None:
        mlflow.log_params(key, val)

    def _instance_of_ml_(self) -> mlflow:
        return mlflow

    def _ml_termination_(self) -> None:
        mlflow.end_run()


def initialize(experiment_name: str, **kwargs) -> MLflowManager:
    global client
    client = MLflowManager(experiment_name, **kwargs)
    return client
