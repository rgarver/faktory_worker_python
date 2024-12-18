class Job:
  def __init__(self, job:dict) -> None:
    # Required fields
    self.jid = job.get("jid")
    self.jobtype = job.get("jobtype")
    self.args = job.get("args")
    
    # Optional fields
    self.queue = job.get("queue", "default")
    self.reserve_for = job.get("reserve_for", 1800)
    self.at = job.get("at", None)
    self.retry = job.get("retry", 25)
    self.backtrace = job.get("backtrace", 0)
    self.created_at = job.get("created_at", None)
    self.custom = job.get("custom", None)
    self.enqueued_at = job.get("enqueued_at", None)
    self.failure = job.get("failure", None)

  def perform(self, *args) -> None:
    raise NotImplementedError("You must implement the perform() method in your job class")
