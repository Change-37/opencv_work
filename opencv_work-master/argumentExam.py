def login(msg, time=3, warn="Wrong ID"):
    while True:
        id = input(msg)
        if id in ('usr', 'user', 'User', 'USER'):
            print("success")
            return True
        time -= 1
        if time < 0:
            print("you did too much times")
            return False
        print(warn)

login('#1 : input ID')
login('#2 : input ID', 2)
login('#3 : input ID', 2, 'try again')