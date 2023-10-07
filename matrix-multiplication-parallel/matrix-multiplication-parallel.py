import numpy as np
import time
from multiprocessing import Pool, cpu_count

# Sequential matrix multiplication
def sequential_matrix_multiplication(A, B):
    return np.dot(A, B)

# Parallel matrix multiplication using multiprocessing.Pool
def parallel_matrix_multiplication(args):
    A, B = args
    return np.dot(A, B)

if __name__ == '__main__':
    # Generate random large matrices (you can replace these with your own matrices)
    size = 1000  # Adjust the size as needed
    A = np.random.rand(size, size)
    B = np.random.rand(size, size)

    # Sequential multiplication
    start_time = time.time()
    result_seq = sequential_matrix_multiplication(A, B)
    seq_time = time.time() - start_time

    # Parallel multiplication
    num_processes = cpu_count()  # Number of available CPU cores
    pool = Pool(processes=num_processes)
    args_list = [(A, B)] * num_processes  # Splitting the task for parallel processing
    start_time = time.time()
    results_parallel = pool.map(parallel_matrix_multiplication, args_list)
    pool.close()
    pool.join()
    result_parallel = sum(results_parallel)
    parallel_time = time.time() - start_time

    # Compare results
    assert np.allclose(result_seq, result_parallel)

    print(f"Sequential Multiplication Time: {seq_time} seconds")
    print(f"Parallel Multiplication Time: {parallel_time} seconds")
