#C:\Users\silri\anaconda3\python 'C:\Users\silri\Desktop\Applied_AI\Concurrent_Programming\Simple_Threading.py'
import time
import threading


def calc_sum_squares(n):
    sum_of_sq = 0
    for i in range(n):
        sum_of_sq+=i**2

    print(sum_of_sq)

def sleep_a_little(seconds):
    time.sleep(seconds)



#To introduce threading -
#1. Identify the functions - calc_sum_squares,sleep_a_little
#2. Identify the arguments - (i+1)*3000000, seconds
#3. Create the threading object ,  t = threading.Thread(target = <funaction name>, args = (<arguments to be passed>)) -Arguments should be in form of tuples
#4. t.start()
#5. Print the messege after finishing  all the threads
#6. Will append all the threads into list and join them - current_thread[i].join() -> Nothing is allowed to happen untill this thread finishes. Basically , this will limit the runtime
    #and make sure all the preious threads are completed before proceeding. ".join()" means the execution is blocked and the loop doesn't continue.

#Q. What happens if we use the .join() inside the previous loop? -- > It will block the execution
#Q. What if we add the daemon = True --> The program will exit , once the main thread is completed


def main():
    start_time = time.time()
    current_thread = []
    for i in range(5):
        max_value = (i+1)*3000000
        t=threading.Thread(target=calc_sum_squares,args=(max_value,),daemon=True)
        t.start()
        current_thread.append(t)

        # calc_sum_squares((i+1)*3000000)

    for i in range(len(current_thread)):
        current_thread[i].join()

    print("Calculating sum of squares took : ", round(time.time()-start_time,1))

    sleep_start_time  = time.time()
    for seconds in range(5):
        current_thread = []
        t=threading.Thread(target=sleep_a_little,args=(seconds,),daemon=True)
        t.start()
        current_thread.append(t)
        # sleep_a_little(seconds)

    for i in range(len(current_thread)):
        current_thread[i].join()

    print("Sleep took : ", round(time.time()-sleep_start_time,1))


if __name__ == "__main__":
    main()
