# declare week() function
# day variable stored string
# output all string data
def week():
    days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    print(days)

# declare hello() function
# declared empty string
# say variable stored string
# user input requested
# split functioned used for more managability
# this for loop runs through "len(remove)" starting on 2
# the if statement allows the code to only call "remove" data that is divisable by 2 
# everytime in the loop if the data is acceptable the empty string will capture the data declared
# else the empty string captures which ever i string its on
def hello():
    speak_world = ""
    say = "hello"
    user_inp = input("Enter a sentance : ")
    remove = user_inp.split()
    
    for i in range(1,len(remove)):
        
        if i % 2 == 0:
            speak_world += say + " "
            

        else:
            speak_world += remove[i]

    print(speak_world)
           
hello()
week()