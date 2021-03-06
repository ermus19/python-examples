import threading
import time

EXIT_FLAG = 0

class exampleThread (threading.Thread):

    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        
    def run(self):
        print("Starting ", self.name)
        lock.acquire()
        print_time(self.name, self.counter, 5)
        lock.release()
        print("Exiting " + self.name)
    
def print_time(threadName, delay, counter):
    while counter:
        if EXIT_FLAG:
            threadName.exit()
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1
    
lock = threading.Lock()
#threads = []


thread1 = exampleThread(1, "Thread-1", 1)
thread2 = exampleThread(2, "Thread-2", 2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

#threads.append(thread1)
#threads.append(thread2)

#for t in threads:
#   t.join()

print("Exiting main thread")
