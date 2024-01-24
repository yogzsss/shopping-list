products=[]

def additem(item,price):
    products.append((item,price))
    
while(True):
    
    a=int(input("enter your choice: "))
    if(a==1):
        for i in range(2):
            item=input("enter the product name: ")
            price=int(input("enter the product price: "))
            additem(item,price)
            print(products)
        
    elif(a==2):
            total_price= sum(items[1]for items in products)
            print(total_price)
    elif(a==3):
        print(products)
        
    else:
        break
    

    

