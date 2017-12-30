import threading
import time
import queue

EXIT_FLAG = 0

class exampleThread(threading.Thread):
    
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q

    def run(self):
        print("Starting ", self.name)
        process_data(self.name, self.q)
        print("Exiting ", self.name)


def process_data(threadName, q):
    while not EXIT_FLAG:
        lock.acquire()
        if not wordsQueue.empty():
            data = q.get()
            lock.release()
            print("%s processing %s" % (threadName, data))
            time.sleep(1)
        else: 
            lock.release()
            time.sleep(1)

threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight"]
lock = threading.Lock()

wordsQueue = queue.Queue(10)

threads = []
threadID = 1

for thread_name in threadList:
    thread = exampleThread(threadID, thread_name, wordsQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

lock.acquire()

for word in nameList:
    wordsQueue.put(word)
lock.release()

while not wordsQueue.empty():
    pass

EXIT_FLAG = 1

for t in threads:
    t.join()
print("Exiting Main thread")