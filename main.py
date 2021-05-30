itemName = []
price = []
quantity = []
purchaseItems = []
purchaseQuantity = []
purchaseAmount = []    
def read():
    fName = "Itemstock.txt"
    with open(fName) as f:
        stock = f.readlines()
        stock = [x.strip("\n") for x in stock]
        length = len(stock)
        a = 0
        while(a<length):
            index = 0
            #intLength = len(stock[a].split(","))
            for username in stock[a].split(","):
                if(index == 0):
                    itemName.append(username)
                elif(index == 1):
                     price.append(username)
                elif(index == 2):
                     quantity.append(username)
                index = index + 1
            a = a + 1

    
       
            
       


    print("               Welcome to the Inventory Management System of Pokhara Electronics Store\n")
    print("*******************************************************************************************************")
    while(True):
        print("Please choose one of the following:")
        print("1)Products Detail")
        print("2)To Purchase item")
        print("3)Exit\n")
        choice = input()
        print()

        if(choice == "1"):
            details()
            print("\n")
        elif(choice == "2"):
            purchase()
            print("\n")
        elif(choice == "3"):
            print("Thank You! Keep visiting again!")
            break;
        else:
            print("Invalid number")
            from again import askAgain
            askAgain()
            
            
def details():
     print("Available products and its details:\n")
     print("Product Name"+"\t"+"Price"+"\t"+"Quantity")
     for i in range(3):
         print(itemName[i],"\t","\t",price[i],"\t",quantity[i])
  
def purchase():
    name = input("Enter the name of the item you want to buy:\n")
    if name.lower() in itemName:
        print(name, "is available in our stock\n")
        global indexN
        indexN = itemName.index(name.lower())
        #print(name,"is in index",indexN)
        qtyValidation()

        purchaseItems.append(indexN)
        purchaseQuantity.append(qty)
        
        if(qty > int(quantity[indexN])):
            print("Sorry, our stock doesnt meet your quantity.\n")
            from again import askAgain
            askAgain()
        else:
            global totalMoney
            totalMoney = qty * float(price[indexN])
            print("Your total purchase amount is:",totalMoney)
            purchaseAmount.append(totalMoney)
            quantity[indexN] = int(quantity[indexN]) - qty
            print("Remaining quantity in stock = ", quantity[indexN])
            with open("Itemstock.txt","w+") as f:
                for i in range(3):
                    f.write(str(itemName[i])+","+str(price[i])+","+str(quantity[i])+"\n") 
            purchase2()
            
    else:
        print("Please enter the correct product name.\n")
        from again import askAgain
        askAgain()
def purchase2():
    ask = input("Do you want to purchase again?   Y/N?")
    if(ask.lower() == "y"):
         purchase()
    else:
        generateInvoice()

                    
def qtyValidation():
    try:
        global qty
        qty = int(input("How much quantity you want to buy?\n"))
        print("You want to buy", qty,itemName[indexN])
    except ValueError:
        print("This is not a integer value. Please enter only integer value")
        qtyValidation()
                    
                    
def generateInvoice():
    
    name = input("Enter the customer name:\n")
    print("Thank You for purchasing from our store!!. Your invoice is ready. Please take it.\n")
    fName = name+".txt"
    with open(fName,"w+") as f:
        f.write("        Pokhara Electronic Store\n")
        f.write("_________________________________________________________\n")
        f.write("Customer Name:{0}\n".format(name))
        from date import impDate
        f.write("Date:{0}\n".format(impDate()))
        from nowtime import impTime
        f.write("Time:{0}\n".format(impTime()))
        from billnum import bill
        f.write("Bill No:{0}\n".format(bill()))
        f.write("_________________________________________________________\n")
        f.write("SN"+"\t"+"Product Name"+"\t"+"Quantity"+"\t"+"Total Price\n")
        total = 0
        for i in range(len(purchaseItems)):
            ind = purchaseItems[i]
            f.write(str(i + 1) +"\t"+ str(itemName[ind]) + "\t"+"\t" + str(purchaseQuantity[i]) + "\t"+"\t" + str(purchaseAmount[i])+"\n")
            total = total + purchaseAmount[i]
        f.write("__________________________________________________________\n")
        f.write("Grand Total:\t\t\t\t{0}".format(total))
        f.write("\n")
        f.write("__________________________________________________________\n")
        f.write("\n"+"\n"+"\n")
        f.write("************Thank You*************")
    f = open(fName,"r")
    message = f.read()
    print(message)
    f.close()
    from again import askAgain
    askAgain()
                    

                


        
                

        
        


                 

    


read()



