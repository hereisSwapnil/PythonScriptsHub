def radix_sort(arr):
    # Find the maximum number to determine the number of digits
    max_num = max(arr)
    num_digits = len(str(max_num))
    
    # Perform counting sort for each digit, starting from the least significant digit
    for i in range(num_digits):
        counting_sort(arr, i)

def counting_sort(arr, digit):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Count the occurrences of each digit
    for i in range(n):
        index = arr[i] // 10**digit
        count[index % 10] += 1

    # Calculate cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    for i in range(n - 1, -1, -1):
        index = arr[i] // 10**digit
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1

    # Copy the output array back to the original array
    for i in range(n):
        arr[i] = output[i]
