cmd = ""
car_started = False
while True:
    cmd = input("> ").lower()
    if cmd == "start":
        if car_started:
           print("Car is already started.")
        else:
            car_started = True
            print("Car started...Ready to go!")
    elif cmd == "stop":
        if not car_started:
            print("Car is already stopped.")
        else:
            car_started = False
            print("Car stopped.")
    elif cmd == "help":
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to exit")
    elif cmd == "quit":
        break
    else:
        print("I dont understand...")
print("Thanks for playing!")