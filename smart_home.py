command = ""
lights_on = False
locked = True

lights_status = "lights are off"
lock_status = "door is locked"
temp = "temperature is "
number = "22"

print("Welcome to Smart Home")

while True:

    command = input("> ").lower()

    if command == "lights on":

        if lights_on:

            print("Lights are already on!")


        else:
 
            print("Lights are turned on.")

            lights_on = True

            lights_status = "lights are on"
   

    elif command == "lights off":

        if not lights_on:

            print("Lights are already off!")


        else:

            print("Lights are turned off!")

            lights_on = False

            lights_status = "lights are off"



    elif command == "lock door":

        if locked:

            print("Door is already locked!")

            lock_status = "door is locked"

        else:

            print("Door locked.")

            locked = True

            lock_status = "door is locked"

    
    elif command == "unlock door":

        if not locked:

            print("Door is already unlocked!")

            lock_status = "door is unlocked"

        else:

            print("Door unlocked.")

            locked = False

            lock_status = "door is unlocked"

    
    elif "set temp" in command:

            print("Thermostat set to" , command[9: ])

            number = command[9: ]


    
    elif command == "status":

        print(lights_status.title())
        print(lock_status.title())
        print((temp + number).title())

    elif command == "help":

        print("""
Here's a list of commands you can use:

> lights on - to turn on lights
> lights off - to turn off lights
> unlock door - to unlock door
> lock door - to lock door
> set temp (any number) - to change temperature
> status - to check status of Smart Home
> quit - to exit the program
""")
        
    elif command == "quit":

        print("Smart Home Exited.")

        break
