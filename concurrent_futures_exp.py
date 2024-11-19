import concurrent.futures
import time

def io_bound_task(seconds, task_name):
    print(f"Task {task_name} starting... Sleeping for {seconds} seconds.")
    time.sleep(seconds)
    print(f"Task {task_name} done.")
    return f"Result of {task_name}"

# Using ThreadPoolExecutor for I/O-bound tasks
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    tasks = ['task1', 'task2', 'task3', 'task4', 'task5']
    seconds_to_sleep = [2, 4, 3, 1, 2]
    
    # Submitting multiple tasks concurrently
    futures = [executor.submit(io_bound_task, sec, task) for sec, task in zip(seconds_to_sleep, tasks)]
    
    # Processing the results as tasks complete
    for future in concurrent.futures.as_completed(futures):
        print(future.result())
        

#or if you want all the results at once 
import concurrent.futures
import time

def io_bound_task(seconds, task_name):
    print(f"Task {task_name} starting... Sleeping for {seconds} seconds.")
    time.sleep(seconds)
    print(f"Task {task_name} done.")
    return f"Result of {task_name}"

# Using ThreadPoolExecutor for I/O-bound tasks
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    tasks = ['task1', 'task2', 'task3', 'task4', 'task5']
    seconds_to_sleep = [2, 4, 3, 1, 2]
    
    # Submitting multiple tasks concurrently
    futures = [executor.submit(io_bound_task, sec, task) for sec, task in zip(seconds_to_sleep, tasks)]
    
    # Processing the results as tasks complete
    for future in concurrent.futures.as_completed(futures):
        print(future.result())