# Threading allows us to speed up programs by executing multiple tasks at the same time.
# Each task will run on its own thread.
# Each therad can run simultaneuiosl and share data with each other.

# Every thread when you start it must do SOMETHING, which we can define with a function.
# Our threads will then target these functions.
# When we start the threads, the target functions will be run.
import threading

def func1():
    for i in range(5):
        print("Function 1")

def func2():
    for i in range(5):
        print("Function 2")

def func3():
    for i in range(5):
        print("Function 3")

# Call functions
# func1()
# func2()     
# func3()

# Create threads
thread1 = threading.Thread(target=func1) # call function name no parentheses
thread2 = threading.Thread(target=func2)
thread3 = threading.Thread(target=func3)

thread1.start() # start the thread
thread2.start()
thread3.start()

# Threads can only be started once.
# thread1.start() # will give an error
# you would need to create a new thread object to start again.
thread1 = threading.Thread(target=func1)
thread1.start()
thread1.join() # wait for thread1 to finish before moving on
