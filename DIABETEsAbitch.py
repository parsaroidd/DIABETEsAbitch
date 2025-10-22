import os, json, time

home = os.path.expanduser("~")

width = os.get_terminal_size().columns

ward = { 
    "test":"45"
}
def login():
    print("\n \n","👋welcome here, I can take care of your BS!".center(width),"of course no one can keep up with your BS but i meant bloodsugar 💞💕".center(width))
    print("  __________________________________________________________________________ \n".center(width), 
          "| Just wanted to say that you are carrying so much, and i'm proud of you... | \n", #.center(width),
         "| _________________________________________________________________________ | \n".center(width),) #.center(width) )
    length = width
    for y in range (length + 1):
        bar = "#" * y + "." * (length - 1)
        print(f"\r {bar}"[:width], end='', flush=True)
        time.sleep(0.025)
    print()
    choice = input("login/sign up: ")
    if "login" in choice:
        pass
    else:
        add_account()
    while True:
        username = input("give me ur name cutie: ".center(width))
        if " " in username:
            print("no spaces R allowed babe ♥, try again".center(width))
        if "." in username:
            print("No dots my friend!".center(width))
        if 32 < username:
            print("woah woah this is to much cutie!".center(width))
        else: break 
    while True:
        password = input("gimme ur password <3: ")
        if ward[username] == password:
            name = f"{username}.json"
            path = os.path.join(home, "Documents", name)
            print(f"welcome back dear {username} <3 !".center(width))
            break 
        else:
            print("something is wrong")

def add_account():
    while True:
        username = input("give me ur name cutie: ".center(width))
        if " " in username:
            print("no spaces R allowed babe ♥, try again".center(width))
        if "." in username:
            print("No dots my friend!".center(width))
        if 32 < username:
            print("woah woah this is to much cutie!".center(width))
        else: 
            password = input("gimme ur password <3: ")
            ward[username] = password
            print("welcome aboard!".center(width))



def save():
   
    
    with open(path, "w") as f:
        json.dump(DataBase, f, indent=4)
        if os.path.exists(path):
            print("✅ File was saved successfully!")
        else:
            print("❌ File not found.")

#def load1(): this was my first attempt 
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

    while True:

        print("")

        date = None
        while not date:
            date = input("tell me the date: ")
            if len(date) >= 3:
                break 
            else:
                print("the date should have at least 2 digits seprated by a character, \n e.g: 2/3 or 3.4 \n " \
                "but for more readability, i recommend the full date like 2025/9/8...")
        bs = None
        while not bs:
            bs = input("what was your blood sugar, baby? ") #no bullshit! blood suger!
            if len(bs) < 5:
                print("enter the hours in paranthesis, in 24-hour format \n"
                 "e.g: 123(23:13)  {123} is bloodsugar, and (23:13) is the hours !")
            else:
                break 
        
            
        if date in DataBase:
            DataBase[date].append(bs)
            save()
        elif date == "off":
            break 
        else:
            DataBase[date] = [] 
            DataBase[date].append(bs)
            save()
    

#load()
#interface()
login()







