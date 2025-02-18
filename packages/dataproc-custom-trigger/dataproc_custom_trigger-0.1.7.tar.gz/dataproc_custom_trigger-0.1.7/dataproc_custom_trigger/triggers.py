import time
import asyncio
from airflow.triggers.base import BaseTrigger, TriggerEvent
from airflow.providers.google.cloud.hooks.dataproc import DataprocHook
from google.cloud.dataproc_v1.types import JobStatus

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
        
        self.log.info("Trigger DataprocJobTrigger inicializado para job: %s", job_id)

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
        iteration = 0
        
        self.log.info("Trigger ha comenzado a ejecutarse.")
        while True:
            iteration += 1
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
            self.log.info("Iteration %s at %s", iteration, current_time)
            job = hook.get_job(project_id=self.project_id, region=self.region, job_id=self.job_id)
            state = job.status.state
            self.log.info("Job %s state: %s", self.job_id, state)
            if state in (JobStatus.State.ERROR, JobStatus.State.CANCELLED):
                yield TriggerEvent({"status": "failed", "job_id": self.job_id, "state": state})
                return
            elif state == JobStatus.State.DONE:
                yield TriggerEvent({"status": "success", "job_id": self.job_id})
                return

            if time.time() - start_time > self.timeout.total_seconds():
                yield TriggerEvent({"status": "timeout", "job_id": self.job_id})
                return

            await asyncio.sleep(self.poke_interval)
