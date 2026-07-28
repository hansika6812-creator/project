import time

alarm_time = input("Enter alarm time (HH:MM:SS): ")

print("Alarm set for", alarm_time)

while True:
    current_time = time.strftime("%H:%M:%S")
    print("Current Time:", current_time, end="\r")

    if current_time == alarm_time:
        print("\n⏰ Alarm! Wake up!")
        for i in range(5):
            print("\a")  
            time.sleep(1)
        break

    time.sleep(1)