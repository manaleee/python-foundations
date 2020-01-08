cashier_item = {}
cashier_history = []

stop = False

while not stop:
    name = input("\nenter the item or type done to exit  \n ")

    if name == 'done':
        stop = True
        break 

    price = input("price per item:  ")
    quantity = input("quantity purchased:   ")
    

    cashier_item = {'item_name':name, 
                    'quantity':int(quantity),
                    'price':float(price)}

    cashier_history.append(cashier_item)
    
    print ("\n---------------\n")
    
    

   


print ("\n\n---------------\n")
print("receipt\n")
print("--------------\n")

price_total = 0 
for item in cashier_history:
   item_total = item['quantity'] * item['price'] 
   price_total += item_total
   print("%d   %s     %.3f KD"  %(item['quantity'], item['item_name'] ,item_total)) 

   item_total = 0
   

print("\n-------------------\n")   
print("total price  : %.3f KD"  % price_total) 




