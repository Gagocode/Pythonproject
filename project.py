import datetime as dt

Nike = {
    "Air Jordan 1 Mid" : 7_090,
    "Air Jordan 1 Low" : 6_195,
    "Nike Air Force 1 \'07" : 5_495,
    "Nike Air Force 1 \'07 EasyOn" : 6_195,
    "Nike Air Force 1 \'07 LV8" : 6_195,
    "Nike Air Force 1 \'07 Pro Tech" : 8_395,
    "Nike Air Max 1" : 7_895,
    "Nike Air Max 90" : 7_395,
    "Nike Air Max Solo" : 5_495,
    "Nike Air Max Pulse" : 8_395,
    "Nike Air Huarache Runner" : 7_895,
    "Nike Dunk Low" : 5_495,
    "Nike Dunk Low Retro" : 5_495,
    "Nike Dunk Low Retro Premium" : 6_895,
    "Nike Dunk Low Jumbo" : 7_095,
    "Nike Go FlyEase" : 7_095,
    "Nike Vomero 5" : 8_895
}

Adidas = {
    "Adifom Climacool Shoes" : 5_500,
    "Adifom Supernova Shoes" : 3_600,
    "Campus 00s Shoes" : 5_000,
    "Campus 80s Shoes" : 6_500,
    "Country XLG Shoes" : 6_000,
    "Gazelle Shoes" : 5_000,
    "Gazelle AVD Shoes" : 6_000,
    "Samba Decon Shoes" : 8_500,
    "Samba Shoes" : 8_000,
    "Stan Smith Shoes" : 5_300,
    "Stan Smith Lux Shoes" : 8_000,
    "Suprestar Shoes" : 5_300,
    "Superstar XLG Shoes" : 6_500,
    "Forum Low Shoes" : 5_500,
    "Humanrace Samba Shoes" : 9_000,
    "OZMORPH Shoes" : 8_000
}

NewBalance = {
    "New Balance 237" : 5_995,
    "New Balance 327"  : 5_995,
    "New Balance 413" : 4_295,
    "New Balance 574" : 5_795,
    "New Balance U327V1" : 6_995,
    "New Balance Men DynaSoft FLASH v6" : 4_995, 
    "New Balance Men MS327V1" : 6_295,
    "New Balance Men 373v2" : 5_295,
    "New Balance Fresh Foam UA700" : 4_315,
    "New Balance Fresh Foam X EVOZ V3" : 5_436,
}

Vans = {
    "Vans Authentic" : 3_994,
    "Vans Ave" : 6_197,
    "Vans Anaheim" : 4_789,
    "Vans Kevin Peraza BMX" : 5_352,
    "Vans Lowland" : 5_352,
    "Vans Old Skool" : 4_789,
    "Vans Sk8-Hi" : 5_352,
    "Vans Skate Chukka" : 3_944,
    "Vans Skate Old Skool" : 4_789,
    "Vans Wayvee" : 5_352,
    "Vans Woodland Wash" : 3_380,
    "Vans UltraRange Exo" : 6_197, 
}

Converse = {
    "Chuck 70" : 4_390,
    "Chuck 70 AT-CX" : 5_790,
    "Chuck 70 AT-CX Mono" : 5_790,
    "Chuck 70 AT-CX Platform" : 5_790,
    "Chuck 70 OX" : 3_350,
    "Chuck 70 Vintage Canvas" : 4_390,
    "Chuck Taylor All Star" : 3_190,
    "Chuck Taylor All Star Construct": 4_490,
    "Chuck Taylor All Star Lugged 2.0" : 4_290,
    "Converse X ADER ERROR Chuck 70" : 6_790,
    "Run Star Legacy CX" : 5_590,
    "Run Star Legacy CX Platform Tortoise" : 5_832,
    "Star Player 76 Shoes Green" : 4_790,
    "Star Player 76 Premium Canvas" : 4_490
}

FILA = {
    "FILA Arigato Jogger" : 3_299,
    "FILA DayOff Jogger" : 3_299,
    "FILA Deck Jogger" : 3_499,
    "FILA Flow Victory" : 5_398,
    "FILA Heritage Amadeo" : 3_149,
    "FILA Heritage Bello" : 3_149,
    "FILA Heritage Giovane" : 3_149,
    "FILA Heritage Moderno" : 3_149,
    "FILA Heritage Salvatore" : 3_149,
    "FILA Heritage Summit" : 2_699,
    "FILA Hybrid Crosscut" : 2_699
}

def Merge(dict1, dict2, dict3, dict4, dict5, dict6):
    mergedbrands = {**dict1, **dict2, **dict3, **dict4, **dict5, **dict6, }
    return mergedbrands

brands = [Nike, Adidas, NewBalance, Vans, Converse, FILA]
brandOnText = ['Nike', 'Adidas', 'NewBalance', 'Vans', 'Converse', 'FILA']
conbinedBrands = Merge(Nike, Adidas, NewBalance, Vans, Converse, FILA)
S = dict()
M = dict()
L = dict()
XL = dict()

def start():
    print("\n~~~~~~~~~~~ MENU ~~~~~~~~~~~")
    print(">>> [1] Shopping Cart")
    print(">>> [2] See available shoes")
    print(">>> [3] Go to Counter")
    print(">>> [4] Exit")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
def cart():
    cartin = {**S, **M, **L, **XL}
    return cartin

def TotalCost(Oncart):
    AllCost = 0
    
    if len(Oncart) > 0:
        for shoe, quantity in Oncart.items():
            AllCost += conbinedBrands[shoe] * quantity
        return AllCost
    else:
        return 0

def Oncartprint(readCart):
    for shoe in readCart:
        if shoe in S:
            print(f"S\tPHP{conbinedBrands[shoe]}\t\t{readCart[shoe]}\t\t{shoe}")
        elif shoe in M:
            print(f"M\tPHP{conbinedBrands[shoe]}\t\t{readCart[shoe]}\t\t{shoe}")
        elif shoe in L:
            print(f"L\tPHP{conbinedBrands[shoe]}\t\t{readCart[shoe]}\t\t{shoe}")
        elif shoe in XL:
            print(f"XL\tPHP{conbinedBrands[shoe]}\t\t{readCart[shoe]}\t\t{shoe}")

def shoppingcart():

    def printCart():
        print("\n------------------- Your Cart -------------------")
        print("Size\t  Price\t\tQuantity\tShoes")
        if len(cart()) >= 1:
            Oncartprint(cart())
        else:
            print("NONE\tNONE\t\tNONE\t\tNone")
        print(f"\nTotal cost: {TotalCost(dict(cart()))}")
        print("-------------------------------------------------")
    
    printCart()
    
    if len(cart()) == 0:
        print("Looks like you haven't filled your cart")
        while True:
            Goback = str(input("Would you like to go back? [Y/N] >>> "))
            
            if Goback == 'N':
                print("Okay!")
            elif Goback == 'Y':
                print("Alright Then")
                break
            else:
                ("Invaid input")
                
    else:
        while True:
            remove = str(input("Would you like to remove an item or go back? [Y/Back] >>> "))
            
            if remove == 'Back':
                break
            elif remove == 'Y':
                while True:
                    ShoetoRemove = ''
                    SizetoRemove = ''
                    Quantitytoremove = 0
                    
                    while True:
                        ShoetoRemove = str(input("What Shoe would you like to remove >>> "))
                        if ShoetoRemove not in cart():
                            print("The Shoe you want to remove is not on the cart")
                        else:
                            break
                    
                    while True:
                        SizetoRemove = str(input(f"What size of {ShoetoRemove} would you like to remove? [S/M/L/XL]"))
                        
                        if SizetoRemove in ('S','M','L','XL'):
                             match SizetoRemove:
                                case 'S':
                                    if ShoetoRemove not in list(S.keys()):
                                        print(f"You dont have {ShoetoRemove} with {SizetoRemove} size in your cart")
                                    else:
                                        break
                                case 'M':
                                    if ShoetoRemove not in list(M.keys()):
                                        print(f"You dont have {ShoetoRemove} with {SizetoRemove} size in your cart")
                                    else:
                                        break
                                case 'L':
                                    if ShoetoRemove not in list(L.keys()):
                                        print(f"You dont have {ShoetoRemove} with {SizetoRemove} size in your cart")
                                    else:
                                        break
                                case 'XL':
                                    if ShoetoRemove not in list(XL.keys()):
                                        print(f"You dont have {ShoetoRemove} with {SizetoRemove} size in your cart")
                                    else:
                                        break
                        else:
                            print(f"Size {SizetoRemove} is invalid Size ")

                    while True:
                        try:
                            Quantitytoremove = int(input("How many would you like to remove? "))
                        except ValueError:
                            print("Invalid input")
                        else:
                            break
                    
                    match SizetoRemove:
                        case 'S':
                            newValue = S[ShoetoRemove] - Quantitytoremove
                            
                            if newValue <=0:
                                S.pop(ShoetoRemove)
                            else:
                                S[ShoetoRemove] = newValue
                        case 'M':
                            newValue = M[ShoetoRemove] - Quantitytoremove
                            
                            if newValue <=0:
                                M.pop(ShoetoRemove)
                            else:
                                M[ShoetoRemove] = newValue
                        case 'L':
                            newValue = L[ShoetoRemove] - Quantitytoremove
                            
                            if newValue <=0:
                                L.pop(ShoetoRemove)
                            else:
                                L[ShoetoRemove] = newValue
                        case 'XL':
                            newValue = XL[ShoetoRemove] - Quantitytoremove
                            
                            if newValue <=0:
                                XL.pop(ShoetoRemove)
                            else:
                                XL[ShoetoRemove] = newValue
                    
                    printCart()
                    break
 
def AvailableShoes():
    
    def shoeMenu():
        Count = 0
        print("\n~~~~~~~~~~~~~~~~ Shoe Brands ~~~~~~~~~~~~~~~~")
        for x in range(3):
            if len(brandOnText[x+Count]) < len(brandOnText[4])+4:
                print(f"~~> {brandOnText[x+Count]} \t\t|\t ~~> {brandOnText[x+Count+1]}")
            else:
                print(f"~~> {brandOnText[x+Count]} \t|\t ~~> {brandOnText[x+Count+1]}")
            Count += 1
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    def showingBrand(Thebrand):
        print("\n  Price\t\tShoes")
        for shoe, price in Thebrand.items():
            print(f"PHP {price}\t{shoe}")
                       
        while True:
            Size = ''
            Quantity = 0
            More = ''
            
            AddToCart = str(input("Choose a shoe to add to your cart or go [Back] >>> "))
                
            if AddToCart in Thebrand:
                pass
            elif AddToCart == 'Back':
                break
            else:
                print(f"{AddToCart} is not on the list")
                continue
                
            while True:
                Size = str(input("What Size would you like? [S/M/L/XL] >>> "))

                if Size in ('S', 'M', 'L', 'XL'):
                    break
                else:
                    print("Invalid Size")
                    continue

            while True:
                try:
                    Quantity = int(input("How many would you like? >>> "))
                except ValueError:
                    print("Invalid input of Quantity")
                else:
                    break
            
            if Size == 'S':
                S[AddToCart] = Quantity
            elif Size == 'M':
                M[AddToCart] = Quantity
            elif Size == 'L':
                L[AddToCart] = Quantity
            elif Size == 'XL':
                XL[AddToCart]= Quantity
            
            print(f"~~~~~~~~~~ {Quantity} {AddToCart} size {Size} is Added to your cart ~~~~~~~~~~")
            
            while True:
                More = str(input("Would you like to add more? [Y/N] "))
                
                if More == 'Y' or More == 'N':
                    break
                else:
                    print("Please Enter [Y/N] ")
                    continue

            if More == 'N':
                break
            else:
                continue
            
    shoeMenu()
    
    while True:
        ChoosenBrand = str(input("Please type a Brand or go [Back] >>> "))
        
        if ChoosenBrand == "Back":
            break
        elif ChoosenBrand in brandOnText:
            match ChoosenBrand:
                case 'Nike':
                    showingBrand(Nike)
                case 'Adidas':
                    showingBrand(Adidas)
                case 'NewBalance':
                    showingBrand(NewBalance)
                case 'Vans':
                    showingBrand(Vans)
                case 'Converse':
                    showingBrand(Converse)
                case 'FILA':
                    showingBrand(FILA)
            shoeMenu()    
        else:
            print("Invalid brand input")

def Counter():
    
    if len(cart()) == 0:
        print("\n>>>You havent filled your shopping cart yet<<<")
    else:
        print(f"Your Total Cost will be {TotalCost(cart())}")
        while True:
            Goback = str(input("Would you like to check-out? [Y/Back] >>> "))

            if Goback == 'Back':
                break
            elif Goback == 'Y':
                pay = 0.00
                while True:
                    try:
                        pay = float(input("How much money would you like to pay? >>> "))
                    except ValueError:
                        print("Your input is invalid")
                    else:
                        break
                
                if pay < TotalCost(cart()):
                    print("It seems that you dont have enough money")
                    
                    while True:
                        GoToCart = str(input("Would you like remove some items in your cart? [Y/N] >>> "))
                        
                        if GoToCart == 'Y':
                            AvailableShoes()
                            break
                        elif GoToCart == 'N':
                            break
                        else:
                            print("Invalid input")
                
                else:
                    TodayTime = dt.datetime.now()
                    print("\n~~~~~~~~~~~~~~~~~~~~ Receipt ~~~~~~~~~~~~~~~~~~~~")
                    print(TodayTime.strftime("Date of purchase: %m-%d-%Y  As of: %I:%M\n"))
                    print("Size\tPrice/pair\tQuantity\t  Shoe(s)")
                    Oncartprint(cart())
                    print("\n==================================================")
                    print(f"\t\t\t\t\t  Totalcost:{TotalCost(cart())}")
                    print(f"\t\t\t\t\tGiven Money:{pay}")
                    print(f"\t\t\t\t\t     Change:{pay - TotalCost(cart())}")
                    print("\tTHANK YOU FOR PURCHASING!")
                    
                    S.clear()
                    M.clear()
                    L.clear()
                    XL.clear()
                    break            
            else:
                print("Invald Input")           

def main():
    print("~~~~~ >>> Welcome to New Class Shoestore <<< ~~~~~")
    start()
                
    while True:
        user_input = str(input(">>>> "))
        
        if user_input in ('1', '2', '3', '4'):
            match user_input:
                case '1':
                    shoppingcart()
                    start()
                case '2':
                    AvailableShoes()
                    start()
                case '3':
                    Counter()
                    start()
                case '4':
                    while True:
                        user_input2 = str(input("Are you sure you want to exit? [Y/N] >>> "))
                        
                        if user_input2 == 'Y' or user_input2 == 'N':
                            break
                        else:
                            print("Invalid input, Please enter \'Y\' for yes or \'N\' for no")
                            
                    match user_input2:
                        case 'Y':
                            print("Thank you for coming!")
                            break
                        case 'N':
                            print('Alright!')
            
        else:
            print("Invalid Input, Please enter the numbers that are shown in the menu")
            
main()