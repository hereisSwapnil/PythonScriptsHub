import multiprocessing

# Define the function to process a chunk of data
def process_chunk(chunk, result_queue):
    result = sum(x**2 for x in chunk)
    result_queue.put(result)

# Define the main function
def main():
    # Generate a large dataset
    data = list(range(1, 100001))  # Example dataset of numbers from 1 to 100,000

    # Split the data into chunks (adjust chunk size as needed)
    chunk_size = len(data) // multiprocessing.cpu_count()
    chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]

    # Create a queue to store results
    result_queue = multiprocessing.Queue()

    # Create and start processes
    processes = []
    for chunk in chunks:
        p = multiprocessing.Process(target=process_chunk, args=(chunk, result_queue))
        processes.append(p)
        p.start()

    # Wait for all processes to finish
    for p in processes:
        p.join()

    # Aggregate results
    total_result = 0
    while not result_queue.empty():
        total_result += result_queue.get()

    print(f'The sum of squares is: {total_result}')

if __name__ == '__main__':
    main()
