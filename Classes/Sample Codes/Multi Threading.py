import time
import threading
a, b, p, q, r, s = 0, 0, 0, 0, 0, 0

def single():
    global b
    for i in range(4000):
        for j in range(20000):
            b += 1

def thread_process0(start, end):
    global p
    for i in range(start, end):
        for j in range(20000):
            p += 1


def thread_process1(start, end):
    global q
    for i in range(start, end):
        for j in range(20000):
            q += 1


def thread_process2(start, end):
    global r
    for i in range(start, end):
        for j in range(20000):
            r += 1

def thread_process3(start, end):
    global s
    for i in range(start, end):
        for j in range(20000):
            s += 1

time.sleep(5)

# Single Threaded
start_time = time.time()
single()
print("single-- %s seconds ---" % (time.time() - start_time))

# Multi Threaded
start_time = time.time()

t1 = threading.Thread(target=thread_process0, args=(0, 1000))
t2 = threading.Thread(target=thread_process1, args=(1000, 2000))
t3 = threading.Thread(target=thread_process2, args=(2000, 3000))
t4 = threading.Thread(target=thread_process3, args=(3000, 4000))

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()

print("multi-- %s seconds ---" % (time.time() - start_time))


# 80000000
# single -- 4.122913837432861 seconds ---
# 80000000
# multi-- 5.886220693588257 seconds ---
