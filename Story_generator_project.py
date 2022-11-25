import random


def story():
    print('Hello Reader! This is your story generator.')

    readername = input("Enter your name here:")

    print('Hello ' + readername)
    names = ["Kapil", "Mohit", "Abhishek", "Sumit", "Vikas", "Sachin", "Prince"]

    places = ["Delhi", "Jaipur", "Bhiwani", "Hisar", "Sikar", "Udaipur", "Mumbai", "Chennai", "Jhunjhunu", "Pilani",
              "Gurugaon", "Jalandhar", "Chandigarh"]

    quests = ["arrive to a grand building and take a photograph", "go to meet a celebraty", "drie in a large jeep",
          "Eat pizza at the Taj Hostel", "travel on the Delhi Eye in the middle of the night",
          "Buy 20 expensive things in the most extravagant shop they see along the street",
          "Go to the most beautiful area they search up in Canada"]
    roles = ["normal boy", "men", "old man", "teenager boy", "child", "secondary student",
         "worker at harrods", "university student", "intelligent boy"]

    weather = ["a sunny day", "a very humid and hot day", "a cold night", "a cloudy day", "a rainy day"]

    print(" Once upon a time a " + random.choice(roles) + " named " + random.choice(names) + " lived in a beautiful area "
    "called " + random.choice(places) + " where it was " + random.choice(weather) + " and in this place " + random.choice(names)
    + " will have to " + random.choice(quests) + " they return to their home at " + random.choice(places))


def Menu():
    print(" 1 for Story","\n","2 for exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        story()
        print("\n")
        Menu()
    elif choice == 2:
        exit()
    else:
        print("Enter right choice")
        Menu()

Menu()
