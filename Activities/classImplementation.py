
class Restaurant:
    def __init__(self, serving, closing, checkingstock, stock, restaurantname, amountofstock, openorclose, location):
        self.serving = serving
        self.closing = False
        self.__checkingstock = checkingstock
        self.__updatingstock = stock
        self.restaurantname = restaurantname
        self.__amountofstock = amountofstock
        self.openorclose = openorclose
        self.location = location
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
        print("New amount of stock available:", self.__updatingstock)

restaurant1 = Restaurant("Served", "False", 50, 50, "Bread Talker", 50, "Open", "SM Legazpi")
restaurant2 = Restaurant("Served", "True", 60, 60, "Bread Hater", 54, "Close", "SM Naga")
restaurant1.display_location()
restaurant1.display_serving()
restaurant1.display_closing(True)
restaurant1._Restaurant__change_stock(10, "add")
print("")
restaurant2.display_location()
restaurant2.display_serving()
restaurant2._Restaurant__change_stock(15, "minus")