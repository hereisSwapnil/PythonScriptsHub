import time

def countdown(duration):
    while duration > 0:
        print(f"Time remaining: {duration} seconds")
        time.sleep(1)
        duration -= 1
    print("Time's up!")

def main():
    try:
        duration = int(input("Enter the duration in seconds: "))
        if duration <= 0:
            print("Please enter a positive integer for the duration.")
            return
        print(f"Counting down from {duration} seconds...")
        countdown(duration)
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    main()
