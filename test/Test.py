from multiprocessing import Lock, Pool
import time


def function(index):
    print('Start process: ', index)
    time.sleep(2)
    print('End process', index)

if __name__ == '__main__':
    pool = Pool(processes=3)
    for i in range(4):
        pool.apply_async(function, (i,))  #非阻塞

    print("Started processes")
    pool.close() #需要关闭进程池，防止池其他任务的提交，注意！这里不是关闭进程。简单来说就是关掉了屋外的大门，但是各个房间在运行。
    pool.join()  #等待进程池里面的进程运行完
    print("Subprocess done.")
