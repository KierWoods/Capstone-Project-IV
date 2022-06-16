# Capstone-Project-IV

## Description
This application mimics a basic stock system for a Nike warehouse. Programmed in python, the application allows the user to search products, add new product lines
mark highest inventory as sale and view all items in inventory. 
I utilised the tabulate module to display all items in a readable easy to digest table for the user.
The purpose of this Project was to enhance my learning of python OOP.


## Requirements
1.An IDE that runs python programming lanugauge i.e VSCode or the python IDE
2.Tabulate module installation. 

## How to use
Copy inventory.txt into your folder, and again copy inventory.py to the same folder. From here run the .py file. follow the instructions that appear on screen.

Below are the following functions within the program; 

▪ read_shoes_data - this function will open the file
inventory.txt and read the data from this file the create shoes
object and append this object into the shoes list. one line in
this file represents data to create one object of shoes. You
must use the try except in this function for error handling.
▪ capture_shoes - this function will allow a user to capture
data about a shoe and use this data to create a shoe object
and append this object inside the shoe list.
▪ view_all - this function will iterate over all the shoes list and
print the details of the shoes that you return from the __str__
function. (Optional: You can organise you data in a table
format by using Python’s tabulate module )
▪ re_stock - this function will find the shoe object with the
lowest quantity, which is the shoes that need to be
restocked. Ask the user if he wants to add the quantity of
these shoes and then update it. This quantity should be
updated on the file for this shoe.
▪ seach_shoe - This function will search for a shoe from the list
using the shoe code and return this object so that it will be
printed
▪ value_per_item - this function will calculate the total value
for each item . (Please keep the formula for value in mind;
value = cost * quantity). Print this information on the
console for all the shoes.
▪ highest_qty - Write code to determine the product with the
highest quantity and print this shoe as being for sale.


##Credits 

This task was issued by HyperionDev 
https://www.hyperiondev.com/
reviewed by: Ikenna Tshabalala
