# user input which was intially in the functions which had to be taken out of to be called later
# variable true_city was declared so that format in which data is captured from variable city is always correct
user_nightStay = int(input("Enter how many nights you will be staying : "))
city = input("Where will you be flying to examples :capetown / portelizabeth / pretoria : ")
true_city = city.lower().replace(" ","")
car_days = int(input("How many days will the vehicle be hired : "))

# declared a function called hotel_cost 
# which contains declared integer varaibles and fomulars
# return is used to hold the data which can be called later
def hotel_cost():
    hotel_price = 890.00
    total = hotel_price * user_nightStay
    return total
    

hotel_cost()

# declared a function called plane_cost
# declared a dictionary which has capture data needed for the function to run
# declared if statements which refers if variable true_city is equal to selected string
# return cost value of data recieved
def plane_cost():
    cost = {"CapeTown":780.00,"PortElizabeth":650.00,"Pretoria":800.00}

    if true_city == "capetown":
        return cost["CapeTown"]
    
    if true_city == "portelizabeth":
        return cost["PortElizabeth"]
        
    if true_city == "pretoria":
        return cost["Pretoria"]   
        
    
    
plane_cost()

# declared integer variable 
# delcared variables containing formulars
# return data which needs to be held
def car_rental():
    car_price = 450.00
    total = car_days * car_price
    return total

car_rental()

# all declared variables in the begining nested in the function holiday_cost brackets
# declared varaibles with captured functions 
# total_holiday variable contains a formular needed to gain total cost
# neatlty print statements which contains string called functions and variables which is easy read
def holiday_cost(true_city,user_nightStay,car_days):
    plane = plane_cost()
    hotel = hotel_cost()
    car = car_rental()
    total_holiday = plane + hotel + car
    print("City                  : " + str(city))
    print("Flight Ticket         : R" + str(plane_cost()))
    print("Nights stayed         : " + str(user_nightStay))
    print("Hotel cost            : R" + str(hotel_cost()))
    print("Car hired duration    : " + str(car_days))
    print("Car hired cost        : R" + str(car_rental()))
    print("Total Holiday cost    : R" + str(total_holiday))



car_rental()
plane_cost()
hotel_cost()
holiday_cost(true_city,user_nightStay,car_days)

