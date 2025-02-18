import time
import asyncio
from airflow.triggers.base import BaseTrigger, TriggerEvent
from airflow.providers.google.cloud.hooks.dataproc import DataprocHook

class DataprocJobTrigger(BaseTrigger):
    """
    Trigger que consulta el estado de un job de Dataproc.
    """
    def __init__(self, job_id, project_id, region, poke_interval, timeout, hook_conn_id):
        super().__init__()
        self.job_id = job_id
        self.project_id = project_id
        self.region = region
        self.poke_interval = poke_interval
        self.timeout = timeout
        self.hook_conn_id = hook_conn_id

    def serialize(self):
        return (
            "dataproc_custom_trigger.triggers.DataprocJobTrigger",
            {
                "job_id": self.job_id,
                "project_id": self.project_id,
                "region": self.region,
                "poke_interval": self.poke_interval,
                "timeout": self.timeout,
                "hook_conn_id": self.hook_conn_id,
            }
        )

    async def run(self):
        hook = DataprocHook(gcp_conn_id=self.hook_conn_id, region=self.region)
        start_time = time.time()
        while True:
            job = hook.get_job(project_id=self.project_id, region=self.region, job_id=self.job_id)
            state = job.status.state
            self.log.info("Job %s state: %s", self.job_id, state)
            if state in ("ERROR", "CANCELLED"):
                yield TriggerEvent({"status": "failed", "job_id": self.job_id, "state": state})
                return
            elif state == "DONE":
                yield TriggerEvent({"status": "success", "job_id": self.job_id})
                return

            if time.time() - start_time > self.timeout:
                yield TriggerEvent({"status": "timeout", "job_id": self.job_id})
                return

            await asyncio.sleep(self.poke_interval)
