#C:\Users\silri\anaconda3\python 'C:\Users\silri\Desktop\Applied_AI\Concurrent_Programming\Threading_v_MultiProcessing.py'
import time
import threading
from multiprocessing import Process

def check_value_in_list(x):
    for i in range(10**8):
        i in x

#1. Syntax of multiprocessing is same as of threading
#2. For windows based operating system, we need to use the if __name__ = "__main__" : method to work the multiprocessing properly

def main():
    comparision_list = [1,2,3]
    # num_of_threads = 4
    num_of_process = 4

    start_time = time.time()

    # threads = []
    process = []
    for i in range(num_of_process):
        # t = threading.Thread(target=check_value_in_list,args=(comparision_list,))
        p = Process(target=check_value_in_list,args=(comparision_list,))
        # check_value_in_list(comparision_list)
        # threads.append(t)
        process.append(p)

        # for t in threads:
        #     t.start()

    for p in process:
        p.start()

    for p in process:
        p.join()

    print("Time taken : ", (time.time()- start_time))

if __name__ == "__main__":
    main()
