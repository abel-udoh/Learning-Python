print("This is a car game, have fun playing")

command = ""
started = False
while True:
    command = input(">> ").lower()
    if command == "start":
        print("Car Started...")
    elif command == "stop":
        print("Car Stopped.")
    elif command == "help":
        print("""
start - to start the car
stop - to Stop the car
quit - quit the game
    """)
    elif command == "quit":
        break
    else:
        print("I dont understand you")
