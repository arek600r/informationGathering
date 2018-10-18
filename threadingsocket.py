import threading
from queue import Queue
import time
import socket

'''
print_lock is what is used to prevent "double" modification of shared variables
this is used so while one thread is using a variable, others cannot acces it.
Once done, the thread releases the prinit_lock.
to use it, you wont to specify a print_lock per thing you wish to print_lock'''

print_lock = threading.Lock()

target = 'jakwpracy.pl'
#ip = socket.gethostbyname(target)


def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((target, port))
        with print_lock:
            print('Port', port)
        con.close()
    except:
        pass

#the threader thread pulls an worker from the queue and process it
def threader():
    while True:
        #gets an worker from the queue
        worker = q.get()
    # run the example job with the avail worker in queue
        portscan(worker)
    #completed with the job
        q.task_done()

# create the queue and threader

q = Queue()

# how meny threads are we going to allow for
for x in range(1, 100):
    t = threading.Thread(target=threader)

    #classifying as a daemon, so the will die when the main dies
    t.daemon = True
    #begins, must come after daemon definition
    t.start()

start = time.time()
#100 jobs assigned
for worker in range(1,100):
    q.put(worker)

q.join()