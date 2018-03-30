import threading, time, random
count = 0
lock = threading.Lock()
def doAdd():
    '''@summary: 将全局变量count 逐一的增加10000。
    '''
    global count, lock
    lock.acquire()
    for i in range(10000):
        count = count + 1

    lock.release()
for i in range(5):
    threading.Thread(target = doAdd, args = (), name = 'thread-' + str(i)).start()
    time.sleep(2)	#确保线程都执行完毕
    print(count)