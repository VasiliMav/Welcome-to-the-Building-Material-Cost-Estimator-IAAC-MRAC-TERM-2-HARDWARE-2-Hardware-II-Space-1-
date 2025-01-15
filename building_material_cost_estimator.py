# Welcome to the Building Material Cost Estimator!

#EXERCISE FOR PYTHON (HARDWARE_2)

#GOALS_OF_THE_EXERCISE
#1. CALCULATE ROOM AREA
#2  CHOOSE FLOORING MATERIAL
#3  CALCULATE TOTAL COST
#4  SAVE PROJECT DETAILS 



#1.  CALCULATE ROOM AREA

#Enter the length of the room 

length=input("Enter the length of the room")
             
if length:float(length)
else:
    print("Please enter a NUMBER")

#Enter the width of the room 

width=input("Enter the width of the room ")

if width:float(width)
else:
 print("Please enter a NUMBER")

#Calculate the total area of the room

print ("The total area of the room is", float(length)*float(width),"square feet.")



#2.  CHOOSE FLOORING MATERIAL

material=input("Choose material for the floor:\n1. Wood ($8/sq ft)\n2. Concrete ($12/sq ft) \n 3. Brick ($10/sq ft) \n 4. Tiles ($5/sq ft)")
material_price = 0
if material in {"Wood", "Concrete", "Brick", "Tiles"}: 
    if material == "Wood":
        material_price = 8 
    elif material == "Concrete":
        material_price = 12 
    elif material == "Brick":
        material_price = 10 
    elif material == "Tiles": 
        material_price = 5 
else:
     print ("Please enter a NAME out of those 4")


#3.  CALCULATE TOTAL COST

total_cost  = float(material_price) * float(length) * float(width) 
print(material, "has a cost of $", material_price,"/sq ft.")
print ("In conclusion the total cost for the floor is $", total_cost)

#4. SAVE PROJECT DETAILS 

save=input("Do you want to save this project? Type y for yes and n for no")
if save in {"y", "n"}: 
    if save == "y":
        def csv(csv_file="building material cost estimator.csv"):
            with (csv_file) as csv_file:
                write = csv.write(csv_file)
                write("Material:","Material cost=",material,material_price,"/sq ft.","Total Cost=",total_cost)
                print("Project saved successfully!")
    elif save =="n": 
        print ('Thank you for using the estimator!') 

else: input ("Please type the letter y to SAVE the result or the letter n to NOT SAVE")


#Thank you for using the estimator!
