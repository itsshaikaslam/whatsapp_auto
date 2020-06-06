from apscheduler.schedulers.blocking import BlockingScheduler


def job_function():
    print("Hello World")


from whatsapp import send_mess

sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(send_mess, 'interval', seconds=10)

sched.start()