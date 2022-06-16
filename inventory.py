from tabulate import tabulate


# Shoe class
class Shoe():

# Constructor.
    def __init__(self):
        self.products = []        

# Method to return the cost of the shoe. 
    def get_cost():
        return self.cost

# Method to return the quantity of shoe.
    def get_quantity():
        return self.quantity

# Method for returning string representation of a class.
    def __str__(self):
        info = self.country + "\n"
        info += self.code + "\n"
        info += self.product + "\n"
        info += self.cost + "\n"
        info += self.quantity
        return info

           



# Function to read inventory.txt file and creating Shoe objects
    def read_shoes_data(self):
            
# Try-except block to handle file error
        try:

# Open file inventory.txt and read the data and create shoe object.
            infile = open("inventory.txt", 'r')

# Iterate through file and create keys variable.
            keys = next(infile).strip().split(",")
            

# Read lines in text file store within dictionary "self.products".
            for line in infile:
                self.products.append(dict(zip(keys, line.strip().split(","))))


# Error message if file does not exist. 
        except FileNotFoundError:
            print("Text file not found.")
        

# Allow user to capture data about a shoe, store as shoe object then add to shoe list.
    def capture_shoes(self):
        with open ("inventory.txt", "a") as f:
            new_product = input("Enter new product details as follows: Country,Code,Product,Cost,Quantity\n")
            
            f.write(new_product)
        shoe.read_shoes_data()
        
        
        


# Iterate over shoe list and print the details of each shoes returned form the __str__ function.
    def view_all(self):
        shoe = Shoe()
        shoe.read_shoes_data()
        shoes.append(shoe)
        print(tabulate(self.products, headers={"Country": "Country","Code": "Code", "Product": "Product", "Cost": "Cost", "Quantity": "Quantity"}, tablefmt = "fancy_grid"))
        
        

# Function to find the shoe with the lowest quantity, ask user to add quantity, update this in file.
    def re_stock(self):

# Set variables to none. 
        lowest_quantity = None
        lowest_product = None

# For loop to determine lowest product; shoe object with lowest quantity.
        for product in self.products:
            if lowest_quantity is None or int(product["Quantity"]) < lowest_quantity:
                lowest_quantity = int(product["Quantity"])
                lowest_product = product

# If lowest_product does not equal none, print to user and ask user to restock product.
        if lowest_product != None:
            print("Code: ",(lowest_product["Code"]))
            print("Product: ",(lowest_product["Product"]))
            print("Quantity: ", (lowest_product["Quantity"]))
            lowest_product["Quantity"] = input("Please input level to restock product to: ") 
            print("Code: ",(lowest_product["Code"]))
            print("Product: ",(lowest_product["Product"]))
            print("Quantity: ", (lowest_product["Quantity"]))
 


# Function to calculate total item value, print this info for all shoes. 
    def value_per_item(self):
        for product in self.products:
            product["Value"] = float(product["Cost"]) * int(product["Quantity"])
            print(product["Product"], product["Value"])
            


# Function to determine shoe with highest quantity and print shoe as "On Sale".
    def highest_qty(self):
        highest_quantity = None
        highest_product = None
        for product in self.products:
            if highest_quantity is None or int(product["Quantity"]) > highest_quantity:
                highest_quantity = int(product["Quantity"])
                highest_product = product

# If highest_product does not equal none, print to user and ask user and mark as sale.
        if highest_product != None:
            print("Code: ",(highest_product["Code"]))
            print("Product: ",(highest_product["Product"]))
            print("Quantity: ", (highest_product["Quantity"]))
            print("Cost: ", (highest_product["Cost"]))
            product_discount = input("Please choose a % to discount this item for sale: ")
            product_discount = int(product_discount) / 100
            highest_product["Cost"] = float(highest_product["Cost"]) * float(product_discount)
            print("Code: ",(highest_product["Code"]))
            print("Product: ",(highest_product["Product"]))
            print("Quantity: ", (highest_product["Quantity"]))
            print("SALE PRICE: ", round((highest_product["Cost"]), 2))



# Function to search for shoe in shoe list using shoe code and print object. 
    def search_shoe(self):
        search = input("Please input SKU: ")
        for product in shoe.products:
            item = {}
            if product["Code"] == search:
                item["Code"] = search
                print(product["Code"])
                print(product["Product"])
                print(product["Cost"])
                print(product["Quantity"])
        if item:
            pass
        else:
            print("SKU does not exist")
                    
# Empty list variable to append class object.
shoes = []
for i in range(5):
    shoe = Shoe()
    shoe.read_shoes_data()
    shoes.append(shoe)

# Main menu that calls the above methods from shoe class.
while True:
    menu =input("""\t\t\tNike Trainer Inventory System

\t\t\tMain Menu

New\t\t - Add new product to inventory list.
View\t\t - View stock on hand.
Restock\t\t - Find product with lowest stock and replenish.
Item search\t - Search for specific product.
Item value\t - Display all product values for each product line.
Sale item\t - Find product with highest quantity and markdown price.
Quit\t\t - Exit Inventory system.\n""").lower()

# Call function capture_shoes
    if menu == "new":
        shoe.capture_shoes()
        
# Call function view_all.
    elif menu == "view":
        shoe.view_all()
        

# Call function re_stock.
    elif menu == "restock":
        shoe.re_stock()

# Call function search_shoe
    elif menu == "item search":
        shoe.search_shoe()

# Call function value_per_item.
    elif menu == "item value":
        shoe.value_per_item()
        

# Call function highest_qty.
    elif menu == "sale item":
        shoe.highest_qty()

# Exit program.
    elif menu == "quit":
        print("Goodbye!")
        exit()

# Error message for user when input not valid.
    else:
        print("Input not recognised, Please try again.")

