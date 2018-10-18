import threading
from queue import Queue
import time

print_lock = threading.Lock()

def exampleJob(worker):
    time.sleep(0.5) #pretend to do some work

    with print_lock:
        print(threading.current_thread().name, worker)

# the threader thread pulls an worker from the queue and process it
def threader():
    while True:
        #gets an worker from the queue
        worker = q.get()
        #run the example job with the avail worker in queue(thread)
        exampleJob(worker)
        #completed with the job
        q.task_done()
#create the queue and threader
q = Queue()

#how many threads are we going to allow for
for x in range(10):
    t = threading.Thread(target = threader)

    t.daemon = True

    t.start()

start = time.time()
for worker in range(20):
    q.put(worker)


q.join()

print('Entire job took:', time.time()-start)