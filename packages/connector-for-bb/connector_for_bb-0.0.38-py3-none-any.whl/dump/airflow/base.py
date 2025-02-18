from abc import abstractmethod
from datetime import datetime, timedelta, timezone
from typing import Any

from airflow.exceptions import AirflowSkipException
from airflow.models import BaseOperator
from airflow.sensors.base import BaseSensorOperator
from airflow.utils.context import Context


class AirflowBaseSensor(BaseSensorOperator):
    def __init__(self, is_optional=False, **kwargs):
        super().__init__(**kwargs)
        self.is_optional = is_optional

    def __init_context(self, context: Context):
        self.execution_date = context["execution_date"]
        self.execution_date_moscow = self.execution_date + timedelta(hours=3)
        self.execution_date_moscow_tz = self.execution_date_moscow.replace(
            tzinfo=timezone(timedelta(hours=3))
        )
        self.task_instance = context["task_instance"]

    def _poke(self) -> Any:
        raise NotImplementedError

    def poke(self, context):
        self.__init_context(context)
        output = self._poke()
        if (
            not output
            and self.is_optional
            and (
                datetime.now(timezone.utc) - self.task_instance.start_date
            ).total_seconds()
            >= self.timeout
        ):
            raise AirflowSkipException(
                "Sensor has timed out. Option 'is_optional' = True, so current and following tasks are going to be skipped."
            )
        self.task_instance.xcom_push(key="sensor_data", value=output)
        return output


class AirflowBaseOperator(BaseOperator):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sensor_metadata: Any = None

    def __init_context(self, context: Context):
        self.execution_date = context["execution_date"]
        self.execution_date_moscow = self.execution_date + timedelta(hours=3)
        self.execution_date_moscow_tz = self.execution_date_moscow.replace(
            tzinfo=timezone(timedelta(hours=3))
        )

        self.task_instance = context["task_instance"]
        self.upstream_metadata = {}
        for task_id in self.upstream_task_ids:
            self.upstream_metadata[task_id] = self.task_instance.xcom_pull(
                task_ids=task_id, key="task_data"
            )
            self.sensor_metadata = self.task_instance.xcom_pull(
                task_ids=task_id, key="sensor_data"
            )

    @abstractmethod
    def _execute(self) -> Any:
        raise NotImplementedError

    def execute(self, context: Context) -> Any:
        self.__init_context(context)
        data = self._execute()
        self.task_instance.xcom_push(key="task_data", value=data)

        return data
