#northwest-corner method

import numpy as np

# Function to make cost assignments for each cell
def CellAssignment(source_rows,destination_columns):
    for i in range(0,source_rows):
        r =i
        for j in range(0,destination_columns):
            matrix[r,j] = input("Please enter the costs of cell [{},{}] :".format(r,j))

# Function to assign supply and demand quantities
def SupplyDemandAssignment(source_rows,destination_columns):
    # supply assignment
    for i in range(0,source_rows):
            supply_value_column[i,0] = input("Please enter the quantity of supply from the {}. supplier: ".format(i+1))
    #demand assignment
    for i in range(0,destination_columns):
            demand_value_row[0,i] = input("Please enter the demand quantity for the {}. demander: ".format(i+1))         

# User inputs for the number of suppliers and demanders
source_rows = int(input("Enter the number of suppliers: "))
destination_columns = int(input("Enter the number of demanders: "))

# Initializing matrices for cost, supply, and demand
matrix = np.zeros(((source_rows),(destination_columns)))
supply_value_column = np.zeros((destination_columns+1,1))
demand_value_row = np.zeros((1,source_rows+1))

# Cell assignments
print("____ASSIGNMENT OF CELLS____")
CellAssignment(source_rows,destination_columns)

# Supply and demand assignments
print("____ASSIGNMENT OF SUPPLY AND DEMAND QUANTITIES____")
SupplyDemandAssignment(source_rows,destination_columns)
print(matrix)

# Variables for tracking total cost and assignments made
total_cost = 0
assignments_made = []
starting_row=0
starting_column=0

# Loop until the bottom right corner is reached           
while(starting_row !=(source_rows) and starting_column !=(destination_columns) ):

     # if supply>demand
     if supply_value_column[starting_row,0] >= demand_value_row[0,starting_column] :
          total_cost += matrix[starting_row,starting_column] * demand_value_row[0,starting_column]
          assignments_made.append("matrix[{},{}] -> {}".format(starting_row,starting_column,demand_value_row[0,starting_column]))
          supply_value_column[starting_row,0] -= demand_value_row[0,starting_column]
          starting_column +=1
     
     # if demand>supply 
     else:
          total_cost += matrix[starting_row,starting_column] * supply_value_column[starting_row,0]
          assignments_made.append("matrix[{},{}] -> {}".format(starting_row,starting_column,supply_value_column[starting_row,0]))
          demand_value_row[0,starting_column] -= supply_value_column[starting_row,0]
          starting_row +=1

# Printing assignments made
print("---------ASSINGMENTS MADE-------- ")
for i in range(len(assignments_made)):
     print(assignments_made[i])

# Printing the initial feasible solution for the given problem
print("The initial solution for the given problem is : {} ".format(total_cost))

