
#<_____________ Created by @ParsaRoidd on github ___________________>
#<I recently started coding, so enjoy! 

import os, json, time 

home = os.path.expanduser("~")

width = os.get_terminal_size().columns

ward = { 
    "test":"45"
}


path2 = os.path.join(home, "Documents", "sql.json")
with open(path2, "r") as f:
    ward = json.load(f)


def login():

    global path

    print("\n \n","👋welcome here, I can take care of your BS!".center(width),"of course no one can keep up with your BS but i meant bloodsugar 💞💕".center(width))
    print("  __________________________________________________________________________ \n".center(width), 
          "| Just wanted to say that you are carrying so much, and i'm proud of you... | \n",
         "| _________________________________________________________________________ | \n \n \n".center(width),)
    length = width
    for y in range (length + 1):
        bar = "#" * y + "." * (length - 1)
        print(f"\r {bar}"[:width], end='', flush=True)
        time.sleep(0.025)
    print()
    print("you should have the file sql.json for this program to work., you can get it in my git hub @parsaroidd".center(width))
    choice = input("login/sign up: ".center(width))
    if "login" in choice:
        pass
    else:
        usernam = input("give me ur name cutie: ".center(width))
        if " " in usernam:
            print("no spaces R allowed babe ♥, try again".center(width))
        if "." in usernam:
            print("No dots my friend!".center(width))
        if 32 < len(usernam):
            print("woah woah this is too much cutie!".center(width))
        else:
            pasword = input("set a password for urself: ".center(width))
            ward[usernam] = pasword
            file = f"{usernam}.json"
            path = os.path.join(home, "Documents", file)
            with open(path2, "w") as f:
                json.dump(ward, f, indent=4)



    while True:
        username = input("This is login page! enter ur username: ".center(width))
        if " " in username:
            print("no spaces R allowed babe ♥, try again".center(width))
        if "." in username:
            print("No dots my friend!".center(width))
        if 32 < len(username):
            print("woah woah this is to much cutie!".center(width))
        elif "quit" in username:
            break 
        else:
            password = input("gimme ur password <3: ".center(width))
            try:
                if ward[username] == password:
                    name = f"{username}.json"
                    path = os.path.join(home, "Documents", name)
                    print(f"welcome back dear {username} <3 !".center(width))
                    interface()
                    break 

                else:
                    print("wrong password or username, try again: ".center(width))
            except KeyError:
                    print("something went wrong! try again. we can not" \
                    " find data that matches your descriptions".center(width))






def save():
    with open(path, "w") as f:
        json.dump(DataBase, f, indent=4)
        if os.path.exists(path):
            print("\n ✅ data was saved successfully!")
        else:
            print("❌No data stored")

#def load(): this was my first attempt 
#    with open(path, "r") as f:
#        DataBase = json.load(f)
#        for i in DataBase: 
#            hey = iter(DataBase)
#            print(f"| {next(hey)} |", end='')
#            for i in DataBase[i]:
#                print(f" {i} |", end='')

def load():
    with open(path, "r") as f:
        DataBase = json.load(f)
        key_list = list(DataBase.keys())
        for i in DataBase:
            print("\n",f"| {i} |", end='')
            for e in DataBase[i]:
                print(f" {e} |", end='')


DataBase = {
    "1404/6/16": ["145(14:20)", "146(15:50)"]
}


def interface():

    x = input("how many data you want to enter?".center(width))
    try:
        if int(x) == int:
            pass  

    except Exception:
        print("please enter a number!".center(width))


    for i in range(int(x)):

        print("")

        date = None
        while not date:
            date = input(" \n tell me the date: ")
            if len(date) == 1:
                break
            elif len(date) < 3:
                print(" \n the date should have at least 2 digits seprated by a character, \n e.g: 2/3 or 3.4 \n " \
                "but for more readability, i recommend the full date like 2025/9/8...")
            else:
                bs = None
                while not bs:
                    bs = input("what was your blood sugar, baby? ") #no bullshit! blood suger 
                    if len(bs) == 1:
                        break 
                    elif len(bs) < 5:
                        print(" \n enter the hours in paranthesis, in 24-hour format \n"
                              "e.g: 123(23:13)  {123} is bloodsugar, and (23:13) is the hours !")
                    else:
                        if date in DataBase:
                            DataBase[date].append(bs)
                            save()
                            load()
                        else:
                            DataBase[date] = [] 
                            DataBase[date].append(bs)
                            save()
                            load()
    


login()





