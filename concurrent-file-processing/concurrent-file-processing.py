import threading

def process_line(line):
    result = line.upper()
    return result

def process_file(filename, start, end):
    with open(filename, 'r') as file:
        for i, line in enumerate(file):
            if start <= i < end:
                result = process_line(line.strip())
                print(result)

def main(filename, num_threads):
    with open(filename, 'r') as file:
        total_lines = sum(1 for _ in file)

    lines_per_thread = total_lines // num_threads

    threads = []
    for i in range(num_threads):
        start = i * lines_per_thread
        end = (i + 1) * lines_per_thread if i != num_threads - 1 else total_lines
        thread = threading.Thread(target=process_file, args=(filename, start, end))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    filename = "large_file.txt"
    num_threads = 4

    main(filename, num_threads)
