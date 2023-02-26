raining=input("is it raining?")
raining=str.lower(raining)

if raining=="yes":
    windy=input("is it windy?")
    windy=str.lower(windy)
    if windy=="yes":
        print("It is too windy for an umbrella")
    else:
        print("Take umbrella")
else:
    print("Enjoy your day")