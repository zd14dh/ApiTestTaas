import os
from conf.settings import BASE_DIR

from apscheduler.schedulers.blocking import BlockingScheduler


def runner_test():
    file=os.path.join(BASE_DIR,'start','start.py')
    print(file)
    os.system("python {}".format(file))
if __name__ == '__main__':
    # BlockingScheduler：在进程中运行单个任务，调度器是唯一运行的东西
    scheduler = BlockingScheduler()
    # # 采用阻塞的方式
    #
    # # 采用date的方式，在特定时间只执行一次.
    scheduler.add_job(runner_test, 'date', run_date='2022-05-30 19:27:41')
    scheduler.start()
