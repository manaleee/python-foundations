apple_price  = 0.2
carrot_price = 0.1
flour_price  = 1.3
water_price  = 0.05

total = 0.0

print ("\n\n please choose items (apples,carrot,flour,water) \n\n ")


#done   = "true"

#item = input ( " item(enter 'done' when finished):  " )
item = ""

while ( item != "done") :

    item = input ( " item(enter 'done' when finished):  " )
    
    if item == "apples":
        print ( " price: " , apple_price )
        quantity_apple = int(input ("Qusntity:  " )) 
        total_apple = apple_price * quantity_apple
        total += total_apple

    elif item == "carrot" : 
        print ( " price: " , carrot_price )
        quantity_carrot = int(input ("Qusntity:  " )) 	
        total_carrot = carrot_price * quantity_carrot
        total += total_carrot

    elif item == "flour":
        print ( " price: " , flour_price )
        quantity_flour = int(input ("Qusntity:  " ))	
        total_flour = flour_price * quantity_flour
        total += total_flour

    elif item == "water":
        print ( " price: " , water_price )
        quantity_water = int(input ("Qusntity:  " ))	
        total_water = water_price * quantity_water
        total += total_water

    elif item == "done":
        total = total_apple + total_carrot + total_flour + total_water 
        done = "true"
print ("\n\nDone")


print ("\n\n------------------")
print ("     receipt      ")
print ("------------------")

print ( quantity_apple , " apples " , total_apple , " KD \n ")
print ( quantity_carrot , " carrot " , total_carrot , " KD \n ")
print ( quantity_flour , " flour " , total_flour , " KD \n ")
print ( quantity_water , " water " , total_water , " KD \n ")

print ("\n---------------------------------------------------\n")
print ("total price : " , total , " KD " )
