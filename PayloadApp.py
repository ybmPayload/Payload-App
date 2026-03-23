import csv
import os
#import tkinter
from io import StringIO

class Sneaker:
    def __init__(self, sku, price = "na"):
        self.sku = sku
        self.price = price

    def updatePrice(self, newPrice):
        self.price = newPrice

# define variables
Sneakers = []
filename = "sneaker_data.csv"
fields = ["sku", "price"]  # Column names
rows = []    # Data rows
fileExisted = False

# Check if the file exists
if os.path.exists(filename):
    fileExisted = True # set file exists to true
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)  # Reader object
        i = 0 # counter for printering number of the item
        fields = next(csvreader)  # Read header
        for row in csvreader:     # Read rows
            rows.append(row)
            Sneakers.append(Sneaker(sku = row[0], price = row[1]))
            print("Sneaker List Item ", i,":", Sneakers[i].sku)
            i = i + 1
            

        print("Total no. of rows: %d" % csvreader.line_num)  # Row count

print('Field names are: ' + ', '.join(fields))
print('First ',len(rows),' rows are:')  #len is used to count how many rows there are
for row in rows:
    for col in row:
        print("%10s" % col, end=" ")
    print('\n')

# define variables for new data
newSneakers = []
newRows = []

# Prompt user input, stop when user hits Enter eithout typing.
while True: 
    sku_input = input("Enter Item SKU:  ")

    if sku_input == "":
        break

    newSneakers.append(Sneaker(sku_input))

# make list of new rows to add to the file  
i = 0
for sneaker in newSneakers:
    i = i + 1
    newRows.append([sneaker.sku, sneaker.price])
    print("New Sneaker List Item ", i,":", sneaker.sku)


# If file does not exist create new file and add rows
if fileExisted == False:
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)        # Create writer object
        csvwriter.writerow(fields)             # Write header
        csvwriter.writerows(newRows)              # Write multiple rows
# else, file exists, so add new rows to file
else:
    with open(filename, 'a') as csvfile:
        csvwriter = csv.writer(csvfile)        # Create writer object
        csvwriter.writerows(newRows)              # Write multiple rows


# Pull Shoe info Using StockX API and SKU entered.

# Sneaker Name, Colorway, Size

# Retail price, Price Now



