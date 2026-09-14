class Staff:
    def __init__(self, Name, Age, Profession, Rating, Serving, Closing, Cleaning, Stocking):
        self.Name = Name
        self.Age = Age
        self.Profession = Profession
        self.Rating = Rating
        self.Serving = Serving
        self.Closing = Closing
        self.Cleaning = Cleaning
        self.Stocking = Stocking
    def display_Staff(self):
        print("Staff's Info:", self.Name, "is", self.Age, "and aiming for the", self.Profession, "and a", self.Rating)
    def display_Serving(self, value):
        self.Serving = value
    def display_Closing(self, value):
        self.Closing = value
    def display_StaffsMethod(self):
        print("The staff has", self.Serving, ",", self.Closing, ",", self.Cleaning, "and", self.Stocking)


class Restaurant:
    def __init__(self, serving, closing, checkingstock, stock, restaurantname, amountofstock, openorclose, location):
        self.serving = serving
        self.closing = closing
        self.__checkingstock = checkingstock
        self.__updatingstock = stock
        self.restaurantname = restaurantname
        self.__amountofstock = amountofstock
        self.openorclose = openorclose
        self.location = location
        self.related_objects = []
    def display_restaurantname(self):
        print("Restaurant Name:", self.restaurantname)
    def __display_amountofstock(self):
        print("Amount of Stock:", self.__amountofstock)
    def display_openorclose(self):
        print("Open or Close:", self.openorclose)
    def display_location(self):
        print("Restaurant Location:", self.location)
        self.__display_amountofstock()
        self.display_openorclose()
        self.display_restaurantname()
    def display_closing(self, value):
        self.closing = value
    def __display_checkingstock(self):
        print("Current amount of stock available:", self.__checkingstock)
    def __add_stock(self, number):
        self.__updatingstock += number
        print("New amount of stock available:", self.__updatingstock)
    def __minus_stock(self, number):
        self.__updatingstock -= number
        print("New amount of stock available:", self.__updatingstock)
    def __change_stock(self, number, operation):
        if operation == "add":
            self.__add_stock(number)
        elif operation == "minus":
            self.__minus_stock(number)
    def display_serving(self):
        print("Customer is", self.serving)
        print("The store is now", self.closing)
        self.__display_checkingstock()
    def add_item(self, item):
        self.related_objects.append(item)
    def display_items(self):
        for item in self.related_objects:
            item.display_Staff()
            item.display_StaffsMethod()

restaurant1_1 = Restaurant("Served", "False", 50, 50, "Bread Talker", 50, "Open", "SM Legazpi")
restaurant2_1 = Restaurant("Served", "True", 60, 60, "Bread Hater", 60, "Close", "SM Naga")
item1 = Staff("Annie", 16, "Chef", "8.75/10", False, True, "already cleaned", "done stocking")
item2 = Staff("Frank", 23, "Server", "10/10", False, False, "already cleaned", "is stocking")
item3 = Staff("Josh", 19, "Waiter", "6.5/10", True, False, "already cleaned", "done stocking")
restaurant1_1.add_item(item1)
restaurant2_1.add_item(item2)
restaurant1_1.add_item(item3)
restaurant1_1.display_location()
restaurant1_1.display_serving()
restaurant1_1.display_closing(True)
restaurant1_1._Restaurant__change_stock(10, "add")
print("")
restaurant1_1.display_items()
print("")
restaurant2_1.display_location()
restaurant2_1.display_serving()
restaurant2_1._Restaurant__change_stock(15, "minus")
print("")
restaurant2_1.display_items()
