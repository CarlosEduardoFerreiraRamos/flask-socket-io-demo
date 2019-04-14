from celery import Celery
import time as tim

app = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost')

@app.task(bind=True)
def app_task(self, t):
    tim.sleep(t)
    return 'Work Done'

def task_switch(taskType):
    return task_dic.get(taskType)

task_dic = {
    'DELAY': app_task
}