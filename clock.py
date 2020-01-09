from bot import tweet
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()
sched.start() 
@sched.scheduled_job('interval', minutes=60)
def timed_job():
    tweet()
@sched.scheduled_job('interval', minutes=1)
def r_timed_job():
    print("\n" + 1)
sched.print_jobs()