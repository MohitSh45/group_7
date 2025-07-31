import time
import threading

def long_task(name):
    """Simulate a long task by looping and sleeping."""
    for _ in range(100_000):
        time.sleep(0.000_1)
    print(f"Task {name} completed.")

def sequential_execution(times):
    """Execute the long_task function sequentially and measure time."""
    start_time = time.time()
    for i in range(times):
        long_task(f"Sequential-{i+1}")
    elapsed_time = time.time() - start_time
    print(f"Sequential execution took {elapsed_time:.4f} seconds.")

def threaded_execution(times):
    """Execute the long_task function using threads and measure time."""
    threads = []
    start_time = time.time()
    
    for i in range(times):
        thread = threading.Thread(target=long_task, args=(f"Threaded-{i+1}",))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    elapsed_time = time.time() - start_time
    print(f"Threaded execution took {elapsed_time:.4f} seconds.")

# Running the functions 10 times
times_to_run = 10
print("Starting sequential execution...")
sequential_execution(times_to_run)

print("Starting threaded execution...")
threaded_execution(times_to_run)
