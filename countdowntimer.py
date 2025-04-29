import time
usr_input = int(input("Enter the time period: "))
for i in reversed(range(1,usr_input + 1)):
    seconds = i % 60
    minutes = int(i / 60) % 60
    hours = int(i / 3600) % 60
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("Timer expired!!!!")