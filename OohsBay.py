# OOHSbay.com - Online Shopping Portal

"""
This program is about an online shopping portal which asks the user to enter the number of products the user wants to buy. It then asks the number of products
he/she wants to buy. The it aks the user to choose the genre of product, brand, budget and the product he/she wants to buy. It also gives choice for the
shipping details and the finally prints the bill.
"""

def genre_of_product(): # This prints menu for the genre of the products
    print "\n"
    genre_list=['Home Appliances', 'Electronics', 'Clothing', 'Stationary']
    print "Printing the genre list"
    print "SL NO.", "\t\t", "PRODUCT"
    for i in range(4):
        print i+1, "\t\t", genre_list[i]
    global choice # makes the later created variable 'choice' global scope
    choice=input("Enter your choice: ") # Allows user to enter choice of the genre of products listed

def product_menu(choice):
    print "\n"
    global product_choice # makes the later created variable 'product_choice' global scope
    if choice==1: # prints menu for the category of the products for choice=1
        home_appliances_list=["Vaccum Cleaners", "Juicers", "Mixers"]
        print "SL NO.", "\t\t", "ITEMS"
        for i in range(3):
                print i+1, "\t\t", home_appliances_list[i]
        product_choice=input("Enter your item choice: ") # allows user to choose the category of product from the given list

    elif choice==2: # prints menu for the category of the products for choice=2
        electronics_list=["Televisions", "Mobiles", "Laptops"]
        print "SL NO.", "\t\t", "ITEMS"
        for i in range(3):
                print i+1, "\t\t", electronics_list[i]
        product_choice=input("Enter your item choice: ") # allows user to choose the category of product from the given list

    elif choice==3: # prints menu for the category of the products for choice=3
        clothing_list=["Shirts", "Pants", "Hoodies"]
        print "SL NO.", "\t\t", "ITEMS"
        for i in range(3):
                print i+1, "\t\t", clothing_list[i]
        product_choice=input("Enter your item choice: ") # allows user to choose the category of product from the given list

    elif choice==4: # prints menu for the category of the products for choice=4
        stationary_list=["Pencils", "Pens", "Erasers"]
        print "SL NO.", "\t\t", "ITEMS"
        for i in range(3):
                print i+1, "\t\t", stationary_list[i]
        product_choice=input("Enter your item choice: ") # allows user to choose the category of product from the given list

    else:
        print "Invalid Choice"

def brand(choice, product_choice): # Allows user  to choose the product brand
    print "\n"
    global brand_choice # makes the later created variable 'brand_choice' global scope
    if choice==1: # prints menu for the product brand for choice=1
        if product_choice==1: # prints menu for the product brand for product_choice=1
            print "Choose the item brand: "
            print "1. BOSCH"
            print "2. SIEMENS"
            print "3. SHARP"
            brand_choice=input("Enter the brand serial number: ") # Allows user to choose product brand
            if brand_choice>3 or brand_choice<1:
                print "Invalid Choice"

        elif product_choice==2: # prints menu for the product brand for product_choice=2
            print "Choose the item brand: "
            print "1. LG"
            print "2. PANASONIC"
            print "3. KENWOOD"
            brand_choice=input("Enter the brand serial number: ") # Allows user to choose product brand
            if brand_choice>3 or brand_choice<1:
                print "Invalid Choice"

        elif product_choice==3: # prints menu for the product brand for product_choice=3
            print "Choose the item brand: "
            print "1. KENWOOD"
            print "2. PANASONIC"
            print "3. PHILIPS"
            brand_choice=input("Enter the brand serial number: ") # Allows user to choose product brand
            if brand_choice>3 or brand_choice<1:
                print "Invalid Choice"

    elif choice==2: # prints menu for the product brand for choice=2
        if product_choice==1: # prints menu for the product brand for product_choice=1
            print "Choose the item brand: "
            print "1. SONY"
            print "2. SAMSUNG"
            print "3. LG"
            brand_choice=input("Enter the brand serial number: ") # Allows user to choose product brand
            if brand_choice>3 or brand_choice<1:
                print "Invalid Choice"

        elif product_choice==2: # prints menu for the product brand for product_choice=2
            print "Choose the item brand: "
            print "1. APPLE"
            print "2. SAMSUNG"
            print "3. HTC"
            brand_choice=input("Enter the brand serial number: ") # Allows user to choose product brand
            if brand_choice>3 or brand_choice<1:
                print "Invalid Choice"

        elif product_choice==3: # prints menu for the product brand for product_choice=3
            print "Choose the item brand: "
            print "1. LENOVO"
            print "2. HP"
            print "3. DELL"
            brand_choice=input("Enter the brand serial number: ") # Allows user to choose product brand
            if brand_choice>3 or brand_choice<1:
                print "Invalid Choice"

    elif choice==3: # prints menu for the product brand for choice=3
        if product_choice==1: # prints menu for the product brand for product_choice=1
            print "Choose the item brand: "
            print "1. OCTAVE"
            print "2. GIORDANO"
            print "3. LEE COOPER"
            brand_choice=input("Enter the brand serial number: ") # Allows user to choose product brand
            if brand_choice>3 or brand_choice<1:
                print "Invalid Choice"

        elif product_choice==2: # prints menu for the product brand for product_choice=2
            print "Choose the item brand: "
            print "1. SPLASH"
            print "2. BEING HUMAN"
            print "3. MAX"
            brand_choice=input("Enter the brand serial number: ") # Allows user to choose product brand
            if brand_choice>3 or brand_choice<1:
                print "Invalid Choice"

        elif product_choice==3: # prints menu for the product brand for product_choice=3
            print "Choose the item brand: "
            print "1. MAX"
            brand_choice=input("Enter the brand serial number: ") # Allows user to choose product brand
            if brand_choice>1 or brand_choice<1:
                print "Invalid Choice"

    elif choice==4: # prints menu for the product brand for choice=4
        if product_choice==1: # prints menu for the product brand for product_choice=1
            print "Choose the item brand: "
            print "1. HELIX"
            brand_choice=input("Enter the brand serial number: ") # Allows user to choose product brand
            if brand_choice>1 or brand_choice<1:
                print "Invalid Choice"

        elif product_choice==2: # prints menu for the product brand for product_choice=2
            print "Choose the item brand: "
            print "1. UNI BALL"
            print "2. FABER CASTELL"
            brand_choice=input("Enter the brand serial number: ")
            if brand_choice>2 or brand_choice<1: # Allows user to choose product brand
                print "Invalid Choice"

        elif product_choice==3: # prints menu for the product brand for product_choice=3
            print "Choose the item brand: "
            print "1. FABER CASTELL"
            brand_choice=input("Enter the brand serial number: ") # Allows user to choose product brand
            if brand_choice>1 or brand_choice<1:
                print "Invalid Choice"

def budget(choice, product_choice):
    print "\n"
    global budget_choice # makes the later created variable 'budget_choice' global scope
    if choice==1: # prints menu for the product budget range for choice=1
        if product_choice==1: # prints menu for the product budget range for product_choice=1
            print "Select Budget Choice: "
            print "1. AED 30 - AED 40"
            print "2. AED 40 - AED 55"
            budget_choice=input("Enter your Budget Serial Number: ")
            if budget_choice>2 or budget_choice<1:
                print "Invalid Choice"

        elif product_choice==2: # prints menu for the product budget range for product_choice=2
            print "Select Budget Choice: "
            print "1. AED 100 - AED 135"
            print "2. AED 135 - AED 150"
            budget_choice=input("Enter your Budget Serial Number: ")
            if budget_choice>2 or budget_choice<1:
                print "Invalid Choice"

        elif product_choice==3: # prints menu for the product budget range for product_choice=3
            print "Select Budget Choice: "
            print "1. AED 30 - AED 40"
            print "2. AED 40 - AED 55"
            budget_choice=input("Enter your Budget Serial Number: ")
            if budget_choice>2 or budget_choice<1:
                print "Invalid Choice"

    elif choice==2: # prints menu for the product budget range for choice=2
        if product_choice==1: # prints menu for the product budget range for product_choice=1
            print "Select Budget Choice: "
            print "1. AED 4850 - AED 5000"
            print "2. AED 5000 - AED 5290"
            budget_choice=input("Enter your Budget Serial Number: ")
            if budget_choice>2 or budget_choice<1:
                print "Invalid Choice"

        elif product_choice==2: # prints menu for the product budget range for product_choice=2
            print "Select Budget Choice: "
            print "1. AED 1699 - AED 1945"
            print "2. AED 1945 - AED 2235"
            budget_choice=input("Enter your Budget Serial Number: ")
            if budget_choice>2 or budget_choice<1:
                print "Invalid Choice"

        elif product_choice==3: # prints menu for the product budget range for product_choice=3
            print "Select Budget Choice: "
            print "1. AED 2450 - AED 3000"
            print "2. AED 3000 - AED 3569"
            budget_choice=input("Enter your Budget Serial Number: ")
            if budget_choice>2 or budget_choice<1:
                print "Invalid Choice"

    elif choice==3: # prints menu for the product budget range for choice=3
        if product_choice==1: # prints menu for the product budget range for product_choice=1
            print "Select Budget Choice: "
            print "1. AED 35 - AED 55"
            print "2. AED 55 - AED 70"
            budget_choice=input("Enter your Budget Serial Number: ")
            if budget_choice>2 or budget_choice<1:
                print "Invalid Choice"

        elif product_choice==2: # prints menu for the product budget range for product_choice=2
            print "Select Budget Choice: "
            print "1. AED 35 - AED 50"
            print "2. AED 50 - AED 75"
            budget_choice=input("Enter your Budget Serial Number: ")
            if budget_choice>2 or budget_choice<1:
                print "Invalid Choice"

        elif product_choice==3: # prints menu for the product budget range for product_choice=3
            print "Select Budget Choice: "
            print "1. AED 45 - AED 60"
            budget_choice=input("Enter your Budget Serial Number: ")
            if budget_choice>1 or budget_choice<1:
                print "Invalid Choice"

    elif choice==4: # prints menu for the product budget range for choice=4
        if product_choice==1: # prints menu for the product budget range for product_choice=1
            print "Select Budget Choice: "
            print "1. AED 1 - AED 2"
            budget_choice=input("Enter your Budget Serial Number: ")
            if budget_choice>1 or budget_choice<1:
                print "Invalid Choice"

        elif product_choice==2: # prints menu for the product budget range for product_choice=2
            print "Select Budget Choice: "
            print "1. AED 1 - AED 3"
            print "2. AED 3 - AED 5"
            budget_choice=input("Enter your Budget Serial Number: ")
            if budget_choice>3 or budget_choice<1:
                print "Invalid Choice"

        elif product_choice==3: # prints menu for the product budget range for product_choice=3
            print "Select Budget Choice: "
            print "1. AED 1 - AED 2"
            budget_choice=input("Enter your Budget Serial Number: ")
            if budget_choice!=1:
                print "Invalid Choice"

def specific_item(choice, product_choice, brand_choice, budget_choice):
    print "\n"
    global item_choice # makes the later created variable 'item_choice' global scope
    global item # makes the later created variable 'item' global scope
    global sum # makes the later created variable 'sum' global scope
    global warranty # makes the later created variable 'warranty' global scope
    global k # makes the later created variable 'k' global scope
    global s # makes the later created variable 's' global scope
    global d # makes the later created variable 'd' global scope
    global x # makes the later created variable 'x' global scope
    item=warranty="" # creates empty string named 'item' and 'warranty' 
    sum=0
    if choice==1:
        if product_choice==1:
            if brand_choice==1:
                if budget_choice==1: # createss Vaccum Cleaner product list for brand choice 1 budget choice 1
                    print "SL NO.", "\t\t", "ITEMS", "\t\t\t\t", "Warranty", "\t\t", "Price"
                    print "1", "\t\t", "Bosch Model A03 red","\t\t", "2 Years", "\t\t", "AED 32"
                    print "2", "\t\t", "Bosch Model A03 blue","\t\t", "2 Years", "\t\t", "AED 32"
                    print "3", "\t\t", "Bosch Model C35 white","\t\t", "1 Year", "\t\t\t", "AED 38"
                    item_choice=input("Enter your item choice: ")
                    if item_choice==1:
                        sum+=32
                        item+="Bosch Model A03 red"
                        warranty+="2 Years"
                    elif item_choice==2:
                        sum+=32
                        item+="Bosch Model A03 blue"
                        warranty+="2 Years"
                    elif item_choice==3:
                        sum+=38
                        item+="Bosch Model C35 White"
                        warranty+="1 Year"

                elif budget_choice==2: # creates Vaccum Cleaner product list for for brand choice 1 budget choice 2
                    print "SL NO.", "\t\t", "ITEMS", "\t\t\t\t", "Warranty", "\t\t", "Price"
                    print "1", "\t\t", "Bosch Model F23 green","\t\t", "1 Year", "\t\t", "AED 45"
                    print "2", "\t\t", "Bosch Model A12 blue","\t\t", "1 Year", "\t\t", "AED 52"
                    print "3", "\t\t", "Bosch Model A12 white","\t\t", "1 Year", "\t\t", "AED 52"
                    item_choice=input("Enter your item choice: ")
                    if item_choice==1:
                        sum+=45
                        item+="Bosch Model F23 green"
                        warranty+="1 Year"
                    elif item_choice==2:
                        sum+=52
                        item+="Bosch Model A12 blue"
                        warranty+="1 Year"
                    elif item_choice==3:
                        sum+=52
                        item+="Bosch Model A12 white"
                        warranty+="1 Year"

            elif brand_choice==2:
                if budget_choice==1: # creates Vaccum Cleaner product list for for brand choice 2 budget choice 1
                    print "SL NO.", "\t\t", "ITEMS", "\t\t\t\t", "Warranty", "\t\t", "Price"
                    print "1", "\t\t", "Siemens Model E34 red","\t\t", "2 Years", "\t\t", "AED 34"
                    print "2", "\t\t", "Siemens Model B45 blue","\t\t", "1 Year", "\t\t", "AED 34"
                    print "3", "\t\t", "Siemens Model B45 black","\t\t", "1 Year", "\t\t", "AED 37"
                    item_choice=input("Enter your item choice: ")
                    if item_choice==1:
                        sum+=34
                        item+="Siemens Model E34 red"
                        warranty+="2 Years"
                    elif item+_choice==2:
                        sum+=34
                        item+="Siemens Model B45 blue"
                        warranty+="1 Year"
                    elif item+_choice==3:
                        sum+=37
                        item+="Siemens Model B45 black"
                        warranty+="1 Year"

                elif budget_choice==2: # creates Vaccum Cleaner product list for for brand choice 2 budget choice 2
                    print "SL NO.", "\t\t", "ITEMS", "\t\t\t\t", "Warranty", "\t\t", "Price"
                    print "1", "\t\t", "Siemens Model J27 red","\t\t", "2 Years", "\t\t", "AED 49"
                    print "2", "\t\t", "Siemens Model J27 blue","\t\t", "2 Years", "\t\t", "AED 49"
                    print "3", "\t\t", "Siemens Model W12 white","\t\t", "1 Year", "\t\t", "AED 53"
                    item_choice=input("Enter your item choice: ")
                    if item_choice==1:
                        sum+=49
                        item+="Siemens Model J27 red"
                        warranty+="2 Years"
                    elif item_choice==2:
                        sum+=49
                        item+="Siemens Model J27 blue"
                        warranty+="2 Years"
                    elif item_choice==3:
                        sum+=53
                        item+="Siemens Model W12 white"
                        warranty+="1 Year"

            elif brand_choice==3:
                if budget_choice==1: # creates Vaccum Cleaner product list for for brand choice 3 budget choice 1
                    print "SL NO.", "\t\t", "ITEMS", "\t\t\t\t", "Warranty", "\t\t", "Price"
                    print "1", "\t\t", "Sharp Model E34 red","\t\t", "1 Year", "\t\t", "AED 38"
                    print "2", "\t\t", "Sharp Model B45 blue","\t\t", "2 Years", "\t\t", "AED 37"
                    print "3", "\t\t", "Sharp Model B45 black","\t\t", "2 Years", "\t\t", "AED 37"
                    item_choice=input("Enter your item choice: ")
                    if item_choice==1:
                        sum+=38
                        item+="Sharp Model E34 red"
                        warranty+="1 Year"
                    elif item_choice==2:
                        sum+=37
                        item+="Sharp Model B45 blue"
                        warranty+="2 Years"
                    elif item_choice==3:
                        sum+=37
                        item+="Sharp Model B45 black"
                        warranty+="2 Years"

                elif budget_choice==2: # creates Vaccum Cleaner product list for for brand choice 3 budget choice 2
                    print "SL NO.", "\t\t", "ITEMS", "\t\t\t\t", "Warranty", "\t\t", "Price"
                    print "1", "\t\t", "Sharp Model J27 red","\t\t", "1 Year", "\t\t", "AED 47"
                    print "2", "\t\t", "Sharp Model J27 blue","\t\t", "1 Year", "\t\t", "AED 47"
                    print "3", "\t\t", "Sharp Model W12 white","\t\t", "2 Years", "\t\t", "AED 51"
                    item_choice=input("Enter your item choice: ")
                    if item_choice==1:
                        sum+=47
                        item+="Sharp Model J27 red"
                        warranty+="1 Year"
                    elif item_choice==2:
                        sum+=47
                        item+="Sharp Model J27 blue"
                        warranty+="1 Year"
                    elif item_choice==3:
                        sum+=51
                        item+="Sharp Model W12 white"
                        warranty+="2 Years"
                        
        elif product_choice==2:
            if brand_choice==1:
                if budget_choice==1: # creates Juicer product list for for brand choice 1 budget choice 1
                    print "SL NO.", "\t\t", "ITEMS", "\t\t\t\t", "Warranty", "\t\t", "Price"
                    print "1", "\t\t", "LG Model A03 red","\t\t", "2 Years", "\t\t", "AED 120"
                    print "2", "\t\t", "LG Model A03 blue","\t\t", "2 Years", "\t\t", "AED 120"
                    print "3", "\t\t", "LG Model C35 white","\t\t", "1 Year", "\t\t", "AED 117"
                    item_choice=input("Enter your item choice: ")
                    if item_choice==1:
                        sum+=120
                        item+="LG Model A03 red"
                        warranty+="2 Years"
                    elif item_choice==2:
                        sum+=120
                        item+="LG Model A03 blue"
                        warranty+="2 Years"
                    elif item_choice==3:
                        sum+=117
                        item+="LG Model C35 white"
                        warranty+="1 Year"

                elif budget_choice==2: # creates Juicer product list for for brand choice 1 budget choice 2
                    print "SL NO.", "\t\t", "ITEMS", "\t\t\t\t", "Warranty", "\t\t", "Price"
                    print "1", "\t\t", "LG Model I23 blue","\t\t", "1 Year", "\t\t", "AED 140"
                    print "2", "\t\t", "LG Model K82 red","\t\t", "1 Year", "\t\t", "AED 145"
                    print "3", "\t\t", "LG Model K82 white","\t\t", "1 Year", "\t\t", "AED 145"
                    item_choice=input("Enter your item choice: ")
                    if item_choice==1:
                        sum+=140
                        item+="LG Model I23 blue"
                        warranty+="1 Year"
                    elif item_choice==2:
                        sum+=145
                        item+="LG Model K82 red"
                        warranty+="1 Year"
                    elif item_choice==3:
                        sum+=145
                        item+="LG Model K82 white"
                        warranty+="1 Year"

            elif brand_choice==2:
                if budget_choice==1: # creates Juicer product list for for brand choice 2 budget choice 1
                    print "SL NO.", "\t\t", "ITEMS", "\t\t\t\t" "Warranty", "\t\t" "Price"
                    print "1", "\t\t", "Panasonic Model G38 white","\t\t", "2 Years", "\t\t", "AED 119"
                    print "2", "\t\t", "Panasonic Model H45 blue","\t\t", "1 Year", "\t\t", "AED 124"
                    print "3", "\t\t", "Panasonic Model H45 black","\t\t", "1 Year", "\t\t", "AED 124"
                    item_choice=input("Enter your item choice: ")
                    if item_choice==1:
                        sum+=119
                        item+="Panasonic Model G38 white"
                        warranty+="2 Years"
                    elif item_choice==2:
                        sum+=124
                        item+="Panasonic Model H45 blue"
                        warranty+="1 Year"
                    elif item_choice==3:
                        sum+=124
                        item+="Panasonic Model H45 black"
                        warranty+="1 Year"

                elif budget_choice==2: # creates Juicer product list for for brand choice 2 budget choice 2
                    print "SL NO.", "\t\t", "ITEMS", "\t\t\t\t", "Warranty", "\t\t", "Price"
                    print "1", "\t\t", "Panasonic Model L07 red","\t\t", "2 Years", "\t\t", "AED 145"
                    print "2", "\t\t", "Panasonic Model L07 blue","\t\t", "2 Years", "\t\t", "AED 145"
                    print "3", "\t\t", "Panasonic Model M52 white","\t\t", "1 Year", "\t\t", "AED 138"
                    item_choice=input("Enter your item choice: ")
                    if item_choice==1:
                        sum+=145
                        item+="Panasonic Model L07 red"
                        warranty+="2 Years"
                    elif item_choice==2:
                        sum+=145
                        item+="Panasonic Model L07 blue"
                        warranty+="2 Years"
                    elif item_choice==3:
                        sum+=138
                        item+="Panasonic Model M52 white"
                        warranty+="1 Year"

            elif brand_choice==3: # creates Juicer product list for for brand choice 3 budget choice 1
                if budget_choice==1:
                    print "SL NO.", "\t\t", "ITEMS", "\t\t\t\t", "Warranty", "\t\t", "Price"
                    print "1", "\t\t", "Kenwood Model U84 red","\t\t", "2 Years", "\t\t", "AED 120"
                    print "2", "\t\t", "Kenwood Model E95 blue","\t\t", "1 Year", "\t\t", "AED 125"
                    print "3", "\t\t", "Kenwood Model E95 black","\t\t", "1 Year", "\t\t", "AED 125"
                    item_choice=input("Enter your item choice: ")
                    if item_choice==1:
                        sum+=120
                        item+="Kenwood Model U84 red"
                        warranty+="2 Years"
                    elif item_choice==2:
                        sum+=125
                        item+="Kenwood Model E95 blue"
                        warranty+="1 Year"
                    elif item_choice==3:
                        sum+=125
                        item+="Kenwood Model E95 black"
                        warranty+="1 Year"

                elif budget_choice==2:# creates Juicer product list for for brand choice 3 budget choice 1
                    print "SL NO.", "\t\t", "ITEMS", "\t\t\t\t", "Warranty", "\t\t", "Price"
                    print "1", "\t\t", "Kenwood Model Y47 red","\t\t", "1 Year", "\t\t", "AED 150"
                    print "2", "\t\t", "Kenwood Model Y47 blue","\t\t", "1 Year", "\t\t", "AED 150"
                    print "3", "\t\t", "Kenwood Model Q17 white","\t\t", "2 Years", "\t\t", "AED 140"
                    item_choice=input("Enter your item choice: ")
                    if item_choice==1:
                        sum+=150
                        item+="Kenwood Model Y47 red"
                        warranty+="1 Year"
                    elif item_choice==2:
                        sum+=150
                        item+="Kenwood Model Y47 blue"
                        warranty+="1 Year"
                    elif item_choice==3:
                        sum+=140
                        item+="Kenwood Model Q17 white"
                        warranty+="2 Years"
                        
        elif product_choice==3:
            if brand_choice==1:
                if budget_choice==1: # creates mixer product list for for brand choice 1 budget choice 1
                    print "SL NO.", "\t\t", "ITEMS", "\t\t\t\t", "Warranty", "\t\t", "Price"
                    print "1", "\t\t", "Kenwood Model A03 red","\t\t", "2 Years", "\t\t", "AED 120"
                    print "2", "\t\t", "Kenwood Model A03 blue","\t\t", "2 Years", "\t\t", "AED 120"
                    print "3", "\t\t", "Kenwood Model C35 white","\t\t", "1 Year", "\t\t", "AED 135"
                    item_choice=input("Enter your item choice: ")
                    if item_choice==1:
                        sum+=120
                        item+="Kenwood Model A03 red"
                        warranty+="2 Years"
                    elif item_choice==2:
                        sum+=120
                        item+="Kenwood Model A03 blue"
                        warranty+="2 Years"
                    elif item_choice==3:
                        sum+=135
                        item+="Kenwood Model Q17 white"
                        warranty+="1 Year"

                elif budget_choice==2:
                    print "SL NO.", "\t\t", "ITEMS", "\t\t\t\t", "Warranty", "\t\t", "Price"
                    print "1", "\t\t", "Kenwood Model I23 blue","\t\t", "1 Years", "\t\t", "AED 140"
                    print "2", "\t\t", "Kenwood Model K82 red","\t\t", "1 Years", "\t\t", "AED 145"
                    print "3", "\t\t", "Kenwood Model K82 white","\t\t", "1 Year", "\t\t", "AED 145"
                    item_choice=input("Enter your item choice: ")
                    if item_choice==1:
                        sum+=140
                        item+="Kenwood Model A03 red"
                        warranty+="1 Year"
                    elif item_choice==2:
                        sum+=140
                        item+="Kenwood Model A03 blue"
                        warranty+="1 Year"
                    elif item_choice==3:
                        sum+=145
                        item+="Kenwood Model Q17 white"
                        warranty+="1 Year"

            elif brand_choice==2:
                if budget_choice==1:
                    print "SL NO.", "\t\t", "ITEMS", "\t\t\t\t", "Warranty", "\t\t", "Price"
                    print "1", "\t\t", "Panasonic Model G38 white","\t\t", "2 Years", "\t\t", "AED 119"
                    print "2", "\t\t", "Panasonic Model H45 blue","\t\t", "1 Years", "\t\t", "AED 124"
                    print "3", "\t\t", "Panasonic Model H45 black","\t\t", "1 Year", "\t\t", "AED 124"
                    item_choice=input("Enter your item choice: ")
                    if item_choice==1:
                        sum+=140
                        item+="Panasonic Model G38 white"
                        warranty+="2 Years"
                    elif item_choice==2:
                        sum+=140
                        item+="Panasonic Model H45 blue"
                        warranty+="1 Year"
                    elif item_choice==3:
                        sum+=145
                        item+="Panasonic Model H45 black"
                        warranty+="1 Year"

                elif budget_choice==2:
                    print "SL NO.", "\t\t", "ITEMS", "\t\t\t\t", "Warranty", "\t\t", "Price"
                    print "1", "\t\t", "Panasonic Model L07 red","\t\t", "2 Years", "\t\t", "AED 145"
                    print "2", "\t\t", "Panasonic Model L07 blue","\t\t", "2 Years", "\t\t", "AED 145"
                    print "3", "\t\t", "Panasonic Model M52 white","\t\t", "1 Year", "\t\t", "AED 150"
                    item_choice=input("Enter your item choice: ")
                    if item_choice==1:
                        sum+=145
                        item+="Panasonic Model L07 red"
                        warranty+="2 Years"
                    elif item_choice==2:
                        sum+=145
                        item+="Panasonic Model L07 blue"
                        warranty+="2 Years"
                    elif item_choice==3:
                        sum+=150
                        item+="Panasonic Model M52 white"
                        warranty+="1 Year"

            elif brand_choice==3:
                if budget_choice==1:
                    print "SL NO.", "\t\t", "ITEMS", "\t\t\t\t", "Warranty", "\t\t", "Price"
                    print "1", "\t\t", "Philips Model U84 red","\t\t", "2 Years", "\t\t", "AED 120"
                    print "2", "\t\t", "Philips Model E95 blue","\t\t", "1 Year", "\t\t", "AED 125"
                    print "3", "\t\t", "Philips Model E95 black","\t\t", "1 Year", "\t\t", "AED 125"
                    item_choice=input("Enter your item choice: ")
                    if item_choice==1:
                        sum+=120
                        item+="Philips Model U84 red"
                        warranty+="2 Years"
                    elif item_choice==2:
                        sum+=125
                        item+="Philips Model E95 blue"
                        warranty+="1 Year"
                    elif item_choice==3:
                        sum+=125
                        item+="Philips Model E95 black"
                        warranty+="1 Year"

                elif budget_choice==2:
                    print "SL NO.", "\t\t", "ITEMS", "\t\t\t\t", "Warranty", "\t\t", "Price"
                    print "1", "\t\t", "Philips Model Y47 red","\t\t", "1 Year", "\t\t", "AED 150"
                    print "2", "\t\t", "Philips Model Y47 blue","\t\t", "1 Year", "\t\t", "AED 150"
                    print "3", "\t\t", "Philips Model Q17 white","\t\t", "2 Years", "\t\t", "AED 143"
                    if item_choice==1:
                        sum+=150
                        item+="Philips Model Y47 red"
                        warranty+="1 Year"
                    elif item_choice==2:
                        sum+=150
                        item+="Philips Model Y47 blue"
                        warranty+="1 Year"
                    elif item_choice==3:
                        sum+=143
                        item+="Philips Model Q17 white"
                        warranty+="2 Years"
    elif choice==2:
        if product_choice==1:
            if brand_choice==1:
                if budget_choice==1:
                    print "SL NO.", "\t\t", "ITEMS", "\t\t\t\t", "Warranty", "\t\t", "Price"
                    print "1", "\t\t", "Sony TV Black","\t\t", "2 Years", "\t\t", "AED 4999"
                    print "2", "\t\t", "Sony TV Grey","\t\t", "2 Years", "\t\t", "AED 4999"
                    item_choice=input("Enter your item choice: ")
                    if item_choice==1:
                        sum+=4999
                        item+="Sony TV Black"
                        warranty+="2 Years"
                    elif item_choice==2:
                        sum+=4999
                        item+="Sony TV Grey"
                        warranty+="2 Years"                   

                elif budget_choice==2:
                    print "SL NO.", "\t\t", "ITEMS", "\t\t\t\t", "Warranty", "\t\t", "Price"
                    print "1", "\t\t", "Sony HD TV Black","\t\t", "1 Year", "\t\t", "AED 5000"
                    print "2", "\t\t", "Sony Curve TV Black","\t\t", "1 Year", "\t\t", "AED 5199"
                    print "3", "\t\t", "Sony Curve TV Grey","\t\t", "1 Year", "\t\t", "AED 5199"
                    item_choice=input("Enter your item choice: ")
                    if item_choice==1:
                        sum+=5000
                        item+="Sony HD TV Black"
                        warranty+="1 Year"
                    elif item_choice==2:
                        sum+=5199
                        item+="Sony Curve TV Black"
                        warranty+="1 Year"
                    elif item_choice==3:
                        sum+=5199
                        item+="Sony Curve TV Grey"
                        warranty+="1 Year"

            elif brand_choice==2:
                if budget_choice==1:
                    print "SL NO.", "\t\t", "ITEMS", "\t\t\t\t", "Warranty", "\t\t", "Price"
                    print "1", "\t\t", "Samsung TV Black","\t\t", "2 Years", "\t\t", "AED 4850"
                    print "2", "\t\t", "Samsung TV Grey","\t\t", "1 Year", "\t\t", "AED 4850"
                    item_choice=input("Enter your item choice: ")
                    if item_choice==1:
                        sum+=4850
                        item+="Samsung TV Black"
                        warranty+="2 Years"
                    elif item_choice==2:
                        sum+=4850
                        item+="Samsung TV Grey"
                        warranty+="1 Year"

                elif budget_choice==2:
                    print "SL NO.", "\t\t", "ITEMS", "\t\t\t\t", "Warranty", "\t\t", "Price"
                    print "1", "\t\t", "Samsung HD TV Black","\t\t", "1 Year", "\t\t", "AED 5290"
                    print "2", "\t\t", "Samsung Curve TV Black","\t\t", "1 Year", "\t\t", "AED 5000"
                    print "3", "\t\t", "Samsung Curve TV Grey","\t\t", "2 Years", "\t\t", "AED 5000"
                    item_choice=input("Enter your item choice: ")
                    if item_choice==1:
                        sum+=5290
                        item+="Samsung HD TV Black"
                        warranty+="1 Year"
                    elif item_choice==2:
                        sum+=5000
                        item+="Samsung Curve TV Black"
                        warranty+="1 Year"
                    elif item_choice==3:
                        sum+=5000
                        item+="Samsung Curve TV Grey"
                        warranty+="2 Years"

            elif brand_choice==3:
                if budget_choice==1:
                    print "SL NO.", "\t\t", "ITEMS", "\t\t\t\t", "Warranty", "\t\t", "Price"
                    print "1", "\t\t", "LG TV Black","\t\t", "1 Year", "\t\t", "AED 4999"
                    print "2", "\t\t", "LG TV Grey","\t\t", "2 Years", "\t\t", "AED 4999"
                    item_choice=input("Enter your item choice: ")
                    if item_choice==1:
                        sum+=4999
                        item+="LG TV Black"
                        warranty+="1 Year"
                    elif item_choice==2:
                        sum+=4999
                        item+="LG TV Grey"
                        warranty+="2 Years"

                elif budget_choice==2:
                    print "SL NO.", "\t\t", "ITEMS", "\t\t\t\t", "Warranty", "\t\t", "Price"
                    print "1", "\t\t", "LG HD TV Black","\t\t", "1 Years", "\t\t", "AED 5100"
                    print "2", "\t\t", "LG Curve TV Black","\t\t", "1 Years", "\t\t", "AED 5200"
                    print "3", "\t\t", "LG Curve TV Grey","\t\t", "2 Year", "\t\t", "AED 5200"
                    item_choice=input("Enter your item choice: ")
                    if item_choice==1:
                        sum+=5100
                        item+="LG HD TV Black"
                        warranty+="1 Year"
                    elif item_choice==2:
                        sum+=5200
                        item+="LG Curve TV Black"
                        warranty+="1 Year"
                    elif item_choice==3:
                        sum+=5200
                        item+="LG Curve TV Grey"
                        warranty+="2 Years"
                        
        elif product_choice==2:
            if brand_choice==1:
                if budget_choice==1:
                    print "SL NO.", "\t\t", "ITEMS", "\t\t\t\t", "Warranty", "\t\t", "Price"
                    print "1", "\t\t", "Apple iPhone 4","\t\t", "2 Years", "\t\t", "AED 1799"
                    print "2", "\t\t", "Apple iPhone 4s","\t\t", "2 Years", "\t\t", "AED 1899"
                    print "3", "\t\t", "Apple iPhone 5s","\t\t", "1 Year", "\t\t", "AED 1945"
                    item_choice=input("Enter your item choice: ")
                    if item_choice==1:
                        sum+=1799
                        item+="Apple iPhone 4"
                        warranty+="2 Years"
                    elif item_choice==2:
                        sum+=1899
                        item+="Apple iPhone 4s"
                        warranty+="2 Years"
                    elif item_choice==3:
                        sum+=1945
                        item+="Apple iPhone 5s"
                        warranty+="1 Year"

                elif budget_choice==2:
                    print "SL NO.", "\t\t", "ITEMS", "\t\t\t\t", "Warranty", "\t\t", "Price"
                    print "1", "\t\t", "Apple iPhone 6","\t\t", "1 Year", "\t\t", "AED 2000"
                    print "2", "\t\t", "Apple iPhone 6+","\t\t", "1 Year", "\t\t", "AED 2100"
                    print "3", "\t\t", "Apple iPhone 7","\t\t", "1 Year", "\t\t", "AED 2235"
                    item_choice=input("Enter your item choice: ")
                    if item_choice==1:
                        sum+=2000
                        item+="Apple iPhone 6"
                        warranty+="1 Year"
                    elif item_choice==2:
                        sum+=2100
                        item+="Apple iPhone 6+"
                        warranty+="1 Year"
                    elif item_choice==3:
                        sum+=2235
                        item+="Apple iPhone 7"
                        warranty+="1 Year"

            elif brand_choice==2:
                if budget_choice==1:
                    print "SL NO.", "\t\t", "ITEMS", "\t\t\t\t", "Warranty", "\t\t", "Price"
                    print "1", "\t\t", "Samsung galaxy S4","\t\t", "2 Years", "\t\t", "AED 1845"
                    print "2", "\t\t", "Samsung galaxy S5","\t\t", "1 Years", "\t\t", "AED 1945"
                    item_choice=input("Enter your item choice: ")
                    if item_choice==1:
                        sum+=1845
                        item+="Samsung galaxy S4"
                        warranty+="2 Years"
                    elif item_choice==2:
                        sum+=1945
                        item+="Samsung galaxy S5"
                        warranty+="1 Year"

                elif budget_choice==2:
                    print "SL NO.", "\t\t", "ITEMS", "\t\t\t\t", "Warranty", "\t\t", "Price"
                    print "1", "\t\t", "Samsung galaxy S6","\t\t", "1 Years", "\t\t", "AED 2000"
                    print "2", "\t\t", "Samsung galaxy S7","\t\t", "1 Years", "\t\t", "AED 2135"
                    print "3", "\t\t", "Samsung galaxy S7 Edge","\t\t", "2 Year", "\t\t", "AED 2235"
                    item_choice=input("Enter your item choice: ")
                    if item_choice==1:
                        sum+=2000
                        item+="Samsung galaxy S6"
                        warranty+="1 Year"
                    elif item_choice==2:
                        sum+=2135
                        item+="Samsung galaxy S7"
                        warranty+="1 Year"
                    elif item_choice==3:
                        sum+=2235
                        item+="Samsung galaxy S7 Edge"
                        warranty+="2 Years"

            elif brand_choice==3:
                if budget_choice==1:
                    print "SL NO.", "\t\t", "ITEMS", "\t\t\t\t", "Warranty", "\t\t", "Price"
                    print "1", "\t\t", "HTC 10 Silver","\t\t", "2 Years", "\t\t", "AED 1799"
                    print "2", "\t\t", "HTC One X9","\t\t", "1 Year", "\t\t", "AED 1899"
                    item_choice=input("Enter your item choice: ")
                    if item_choice==1:
                        sum+=1799
                        item+="HTC 10 Silver"
                        warranty+="2 Years"
                    elif item_choice==2:
                        sum+=1899
                        item+="HTC One X9"
                        warranty+="1 Year"

                elif budget_choice==2:
                    print "SL NO.", "\t\t", "ITEMS", "\t\t\t\t", "Warranty", "\t\t", "Price"
                    print "1", "\t\t", "HTC One A9","\t\t", "1 Year", "\t\t", "AED 1995"
                    print "2", "\t\t", "HTC One A9s","\t\t", "1 Year", "\t\t", "AED 2135"
                    item_choice=input("Enter your item choice: ")
                    if item_choice==1:
                        sum+=1995
                        item+="HTC One A9"
                        warranty+="1 Year"
                    elif item_choice==2:
                        sum+=2135
                        item+="HTC One A9s"
                        warranty+="1 Year"
                        
        elif product_choice==3:
            if brand_choice==1:
                if budget_choice==1:
                    print "SL NO.", "\t\t", "ITEMS", "\t\t\t\t", "Warranty", "\t\t", "Price"
                    print "1", "\t\t", "Lenovo ideapad 300","\t\t", "2 Years", "\t\t", "AED 2550"
                    print "2", "\t\t", "Lenovo ideapad 500","\t\t", "2 Years", "\t\t", "AED 2570"
                    item_choice=input("Enter your item choice: ")
                    if item_choice==1:
                        sum+=2550
                        item+="Lenovo ideapad 300"
                        warranty+="2 Years"
                    elif item_choice==2:
                        sum+=2570
                        item+="Lenovo ideapad 500"
                        warranty+="2 Years"

                elif budget_choice==2:
                    print "SL NO.", "\t\t", "ITEMS", "\t\t\t\t", "Warranty", "\t\t", "Price"
                    print "1", "\t\t", "Lenovo ideapad 700","\t\t", "1 Year", "\t\t", "AED 5190"
                    print "2", "\t\t", "Lenovo Thinkpad Yoga","\t\t", "2 Years", "\t\t", "AED 5290"
                    item_choice=input("Enter your item choice: ")
                    if item_choice==1:
                        sum+=5190
                        item+="Lenovo ideapad 700"
                        warranty+="1 Year"
                    elif item_choice==2:
                        sum+=5290
                        item+="Lenovo Thinkpad Yoga"
                        warranty+="2 Years"

            elif brand_choice==2:
                if budget_choice==1:
                    print "SL NO.", "\t\t", "ITEMS", "\t\t\t\t", "Warranty", "\t\t", "Price"
                    print "1", "\t\t", "HP Pavilion X2","\t\t", "2 Years", "\t\t", "AED 2450"
                    print "2", "\t\t", "HP 250 Notebook","\t\t", "1 Years", "\t\t", "AED 2850"
                    item_choice=input("Enter your item choice: ")
                    if item_choice==1:
                        sum+=2450
                        item+="HP Pavilion X2"
                        warranty+="2 Years"
                    elif item_choice==2:
                        sum+=2850
                        item+="HP 250 Notebook"
                        warranty+="1 Year"

                elif budget_choice==2:
                    print "SL NO.", "\t\t", "ITEMS", "\t\t\t\t", "Warranty", "\t\t", "Price"
                    print "1", "\t\t", "HP Stream 13","\t\t", "2 Years", "\t\t", "AED 3100"
                    print "2", "\t\t", "HP Probook 450","\t\t", "2 Years", "\t\t", "AED 3569"
                    item_choice=input("Enter your item choice: ")
                    if item_choice==1:
                        sum+=3100
                        item+="HP Stream 13"
                        warranty+="2 Years"
                    elif item_choice==2:
                        sum+=3569
                        item+="HP Probook 450"
                        warranty+="2 Years"

            elif brand_choice==3:
                if budget_choice==1:
                    print "SL NO.", "\t\t", "ITEMS", "\t\t\t\t", "Warranty", "\t\t", "Price"
                    print "1", "\t\t", "Dell Inspiron 3558","\t\t", "2 Years", "\t\t", "AED 2699"
                    print "2", "\t\t", "Dell Inspiron 5559","\t\t", "1 Years", "\t\t", "AED 2899"
                    item_choice=input("Enter your item choice: ")
                    if item_choice==1:
                        sum+=2699
                        item+="Dell Inspiron 3558"
                        warranty+="2 Years"
                    elif item_choice==2:
                        sum+=2899
                        item+="Dell Inspiron 5559"
                        warranty+="1 Year"

                elif budget_choice==2:
                    print "SL NO.", "\t\t", "ITEMS", "\t\t\t\t", "Warranty", "\t\t", "Price"
                    print "1", "\t\t", "Dell Inspiron 7559","\t\t", "1 Year", "\t\t", "AED 3000"
                    print "2", "\t\t", "Dell Inspiron 7568","\t\t", "1 Year", "\t\t", "AED 3200"
                    item_choice=input("Enter your item choice: ")
                    if item_choice==1:
                        sum+=3000
                        item+="Dell Inspiron 7559"
                        warranty+="1 Year"
                    elif item_choice==2:
                        sum+=3200
                        item+="Dell Inspiron 7568"
                        warranty+="1 Year"

    elif choice==3:
        if product_choice==1:
            if brand_choice==1:
                if budget_choice==1:
                    print "SL NO.", "\t\t", "ITEMS", "\t\t\t\t", "Price"
                    print "1", "\t\t", "Octave Cowboy Shirt black","\t\t", "AED 37"
                    print "2", "\t\t", "Octave Cowboy Shirt yellow","\t\t", "AED 37"
                    print "3", "\t\t", "Octave blue t-shirt","\t\t", "AED 41"
                    item_choice=input("Enter your item choice: ")
                    if item_choice==1:
                        sum+=37
                        item+="Octave Cowboy Shirt black"
                        warranty+="-"
                    elif item_choice==2:
                        sum+=37
                        item+="Octave Cowboy Shirt yellow"
                        warranty+="-"
                    elif item_choice==3:
                        sum+=41
                        item+="Octave blue t-shirt"
                        warranty+="-"

                elif budget_choice==2:
                    print "SL NO.", "\t\t", "ITEMS", "\t\t\t\t", "Price"
                    print "1", "\t\t", "Octave full sleves Shirt Blue","\t\t", "AED 65"
                    print "2", "\t\t", "Octave brown t-shirt","\t\t", "AED 52"
                    item_choice=input("Enter your item choice: ")
                    if item_choice==1:
                        sum+=65
                        item+="Octave full sleves Shirt Blue"
                        warranty+="-"
                    elif item_choice==2:
                        sum+=52
                        item+="Octave brown t-shirt"
                        warranty+="-"

            elif brand_choice==2:
                if budget_choice==1:
                    print "SL NO.", "\t\t", "ITEMS", "\t\t\t\t", "Price"
                    print "1", "\t\t", "Giordano Cowboy Shirt black","\t\t", "AED 44"
                    print "2", "\t\t", "Giordano Cowboy Shirt brown","\t\t", "AED 44"
                    item_choice=input("Enter your item choice: ")
                    if item_choice==1:
                        sum+=44
                        item+="Giordano Cowboy Shirt black"
                        warranty+="-"
                    elif item_choice==2:
                        sum+=44
                        item+="Giordano Cowboy Shirt brown"
                        warranty+="-"

                elif budget_choice==2:
                    print "SL NO.", "\t\t", "ITEMS", "\t\t\t\t", "Price"
                    print "1", "\t\t", "Giordano full sleves Shirt Orange","\t", "AED 62"
                    print "2", "\t\t", "Giordano brown t-shirt","\t\t", "AED 53"
                    print "3", "\t\t", "Giordano blue t-shirt","\t\t", "AED 53"
                    item_choice=input("Enter your item choice: ")
                    if item_choice==1:
                        sum+=62
                        item+="Giordano full sleves Shirt Orange"
                        warranty+="-"
                    elif item_choice==2:
                        sum+=53
                        item+="Giordano brown t-shirt"
                        warranty+="-"
                    elif item_choice==3:
                        sum+=53
                        item+="Giordano blue t-shirt"
                        warranty+="-"

            elif brand_choice==3:
                if budget_choice==1:
                    print "SL NO.", "\t\t", "ITEMS", "\t\t\t\t", "Price"
                    print "1", "\t\t", "Lee Cooper Cowboy Shirt black","\t\t", "AED 38"
                    print "2", "\t\t", "Lee Cooper Cowboy Shirt brown","\t\t", "AED 37"
                    print "3", "\t\t", "Lee Cooper brown t-shirt","\t", "AED 37"
                    item_choice=input("Enter your item choice: ")
                    if item_choice==1:
                        sum+=38
                        item+="Lee Cooper Cowboy Shirt black"
                        warranty+="-"
                    elif item_choice==2:
                        sum+=37
                        item+="Lee Cooper Cowboy Shirt brown"
                        warranty+="-"
                    elif item_choice==3:
                        sum+=37
                        item+="Lee Cooper brown t-shirt"
                        warranty+="-"

                elif budget_choice==2:
                    print "SL NO.", "\t\t", "ITEMS", "\t\t\t\t", "Price"
                    print "1", "\t\t", "Lee Cooper full sleves Shirt Red","\t\t", "AED 59"
                    print "2", "\t\t", "Lee Cooper blue t-shirt","\t\t", "AED 66"
                    item_choice=input("Enter your item choice: ")
                    if item_choice==1:
                        sum+=59
                        item+="Lee Cooper full sleves Shirt red"
                        warranty+="-"
                    elif item_choice==2:
                        sum+=66
                        item+="Lee Cooper blue t-shirt"
                        warranty+="-"
                        
        elif product_choice==2:
            if brand_choice==1:
                if budget_choice==1:
                    print "SL NO.", "\t\t", "ITEMS", "\t\t\t\t", "Price"
                    print "1", "\t\t", "Splash Jeans Black","\t\t", "AED 40"
                    print "2", "\t\t", "Splash Jeans Blue","\t\t", "AED 40"
                    item_choice=input("Enter your item choice: ")
                    if item_choice==1:
                        sum+=40
                        item+="Splash Jeans Black"
                        warranty+="-"
                    elif item_choice==2:
                        sum+=40
                        item+="Splash Jeans Blue"
                        warranty+="-"

                elif budget_choice==2:
                    print "SL NO.", "\t\t", "ITEMS", "\t\t\t\t", "Price"
                    print "1", "\t\t", "Splash pant Black","\t\t", "AED 51"
                    print "2", "\t\t", "Splash pant Brown","\t\t", "AED 51"
                    print "3", "\t\t", "Splash pant Blue","\t\t" "AED 51"
                    item_choice=input("Enter your item choice: ")
                    if item_choice==1:
                        sum+=51
                        item+="Splash pant Black"
                        warranty+="-"
                    elif item_choice==2:
                        sum+=51
                        item+="Splash pant Brown"
                        warranty+="-"
                    elif item_choice==3:
                        sum+=51
                        item+="Splash pant Blue"
                        warranty+="-"

            elif brand_choice==2:
                if budget_choice==1:
                    print "SL NO.", "\t\t", "ITEMS", "\t\t\t\t", "Price"
                    print "1", "\t\t", "Being Human Jeans Black","\t\t", "AED 45"
                    print "2", "\t\t", "Being Human Jeans Blue","\t\t", "AED 45"
                    item_choice=input("Enter your item choice: ")
                    if item_choice==1:
                        sum+=45
                        item+="Being Human Jeans Black"
                        warranty+="-"
                    elif item_choice==2:
                        sum+=45
                        item+="Being Human Jeans Blue"
                        warranty+="-"

                elif budget_choice==2:
                    print "SL NO.", "\t\t", "ITEMS", "\t\t\t\t", "Price"
                    print "1", "\t\t", "Being Human pant black","\t\t", "AED 59"
                    print "2", "\t\t", "Being Human pant Brown","\t\t", "AED 59"
                    print "3", "\t\t", "Being Human pant Blue","\t\t" "AED 59"
                    item_choice=input("Enter your item choice: ")
                    if item_choice==1:
                        sum+=59
                        item+="Being Human pant Black"
                        warranty+="-"
                    elif item_choice==2:
                        sum+=59
                        item+="Being Human pant Brown"
                        warranty+="-"
                    elif item_choice==3:
                        sum+=59
                        item+="Being Human pant Blue"
                        warranty+="-"

            elif brand_choice==3:
                if budget_choice==1:
                    print "SL NO.", "\t\t", "ITEMS", "\t\t\t\t", "Price"
                    print "1", "\t\t", "Max Jeans Black","\t\t", "AED 43"
                    print "2", "\t\t", "Max Jeans Blue","\t\t", "AED 43"
                    item_choice=input("Enter your item choice: ")
                    if item_choice==1:
                        sum+=43
                        item+="Max Jeans Black"
                        warranty+="-"
                    elif item_choice==2:
                        sum+=43
                        item+="Max Human Jeans Blue"
                        warranty+="-"

                elif budget_choice==2:
                    print "SL NO.", "\t\t", "ITEMS", "\t\t\t\t", "Price"
                    print "1", "\t\t", "Max pant black","\t\t", "AED 57"
                    print "2", "\t\t", "Max pant Brown","\t\t", "AED 57"
                    print "3", "\t\t", "Max pant Blue","\t\t" "AED 57"
                    item_choice=input("Enter your item choice: ")
                    if item_choice==1:
                        sum+=57
                        item+="Max pant Black"
                        warranty+="-"
                    elif item_choice==2:
                        sum+=57
                        item+="Max pant Brown"
                        warranty+="-"
                    elif item_choice==3:
                        sum+=57
                        item+="Max pant Blue"
                        warranty+="-"
                        
        elif product_choice==3:
            if brand_choice==1:
                if budget_choice==1:
                    print "SL NO.", "\t\t", "ITEMS", "\t\t\t\t", "Price"
                    print "1", "\t\t", "Max Hoodie Blue","\t\t", "AED 60"
                    print "2", "\t\t", "Max Hoodie White","\t\t" "AED 60"
                    print "3", "\t\t", "Max Hoodie Black","\t\t", "AED 60"
                    item_choice=input("Enter your item choice: ")
                    if item_choice==1:
                        sum+=60
                        item+="Max Hoodie Blue"
                        warranty+="-"
                    elif item_choice==2:
                        sum+=60
                        item+="Max Hoodie White"
                        warranty+="-"
                    elif item_choice==3:
                        sum+=60
                        item+="Max Hoodie Black"
                        warranty+="-"

    elif choice==4:
        if product_choice==1:
            if brand_choice==1:
                if budget_choice==1:
                    print "SL NO.", "\t\t", "ITEMS", "\t\t\t\t", "Price"
                    print "1", "\t\t", "Helix HP break proof pencil", "\t\t" "AED 2"
                    print "2", "\t\t", "Helix HP pencil","\t\t" "AED 1"
                    item_choice=input("Enter your item choice: ")
                    if item_choice==1:
                        sum+=2
                        item+="Helix HP break proof pencil"
                        warranty+="-"
                    elif item_choice==2:
                        sum+=1
                        item+="Helix HP pencil"
                        warranty+="-"
                        
        elif product_choice==2:
            if brand_choice==1:
                if budget_choice==1:
                    print "SL NO.", "\t\t", "ITEMS", "\t\t\t\t", "Price"
                    print "1", "\t\t", "Uniball Red 0.5 mm","\t\t", "AED 1"
                    print "2", "\t\t", "Uniball Blue 0.5 mm","\t\t" "AED 1"
                    print "3", "\t\t", "Uniball Black 0.5 mm","\t\t", "AED 1"
                    item_choice=input("Enter your item choice: ")
                    if item_choice==1:
                        sum+=1
                        item+="Uniball Red 0.5 mm"
                        warranty+="-"
                    elif item_choice==2:
                        sum+=1
                        item+="Uniball Blue 0.5 mm"
                        warranty+="-"
                    elif item_choice==3:
                        sum+=1
                        item+="Uniball Black 0.5 mm"
                        warranty+="-"

                elif budget_choice==2:
                    print "SL NO.", "\t\t", "ITEMS", "\t\t\t\t", "Price"
                    print "1", "\t\t", "Uniball Red 0.7 mm","\t\t", "AED 3"
                    print "2", "\t\t", "Uniball Blue 0.7 mm","\t\t", "AED 3"
                    print "3", "\t\t", "Uniball Black 0.7 mm","\t\t", "AED 3"
                    item_choice=input("Enter your item choice: ")
                    if item_choice==1:
                        sum+=3
                        item+="Uniball Red 0.7 mm"
                        warranty+="-"
                    elif item_choice==2:
                        sum+=3
                        item+="Uniball Blue 0.7 mm"
                        warranty+="-"
                    elif item_choice==3:
                        sum+=3
                        item+="Uniball Black 0.7 mm"
                        warranty+="-"

            elif brand_choice==2:
                if budget_choice==1:
                    print "SL NO.", "\t\t", "ITEMS", "\t\t\t\t", "Price"
                    print "1", "\t\t", "Faber Castell Red 0.5 mm","\t\t", "AED 1"
                    print "2", "\t\t", "Faber Castell Blue 0.5 mm","\t\t" "AED 1"
                    print "3", "\t\t", "Faber Castell Black 0.5 mm","\t\t", "AED 1"
                    item_choice=input("Enter your item choice: ")
                    if item_choice==1:
                        sum+=1
                        item+="Faber Castell Red 0.5 mm"
                        warranty+="-"
                    elif item_choice==2:
                        sum+=1
                        item+="Faber Castell Blue 0.5 mm"
                        warranty+="-"
                    elif item_choice==3:
                        sum+=1
                        item+="Faber Castell Black 0.5 mm"
                        warranty+="-"

                elif budget_choice==2:
                    print "SL NO.", "\t\t", "ITEMS", "\t\t\t\t", "Price"
                    print "1", "\t\t", "Faber Castell Red 0.7 mm","\t\t", "AED 3"
                    print "2", "\t\t", "Faber Castell Blue 0.7 mm","\t\t", "AED 3"
                    print "3", "\t\t", "Faber Castell 0.7 mm","\t", "AED 3"
                    item_choice=input("Enter your item choice: ")
                    if item_choice==1:
                        sum+=3
                        item+="Faber Castell Red 0.7 mm"
                        warranty+="-"
                    elif item_choice==2:
                        sum+=3
                        item+="Faber Castell Blue 0.7 mm"
                        warranty+="-"
                    elif item_choice==3:
                        sum+=3
                        item+="Faber Castell Black 0.7 mm"
                        warranty+="-"
                        
        elif product_choice==3:
            if brand_choice==1:
                if budget_choice==1:
                    print "SL NO.", "\t\t", "ITEMS", "\t\t\t\t", "Price"
                    print "1", "\t\t", "Faber Castell Eraser", "\t\t", "AED 1"
                    item_choice=input("Enter your item choice: ")
                    if item_choice==1:
                        sum+=1
                        item+="Faber Castell Eraser"
                        warranty+="-"
    k=item
    s=warranty
    d=str(sum)
    x=sum

def process():
    print "\n"
    print "Choose your item: "
    genre_of_product()
    product_menu(choice)
    brand(choice, product_choice)
    budget(choice, product_choice)
    specific_item(choice, product_choice, brand_choice, budget_choice)

def shipping_detials():
    print "\n"
    global reference_number
    global shipping_choice
    import random
    print "How do you want to get your product(s)?"
    print "1. Cash on delivery"
    print "2. Come and collect"
    shipping_choice=input("Enter your choice: ")
    if shipping_choice==1:
        address=raw_input("Enter you Address(in one line): ")
        reference_number=random.randint(1,10000)
        print "Your Extra Charge for delivery is AED 60"
        reference_number=random.randint(1,10000)
    elif shipping_choice==2:
        reference_number=random.randint(1,10000)
        print "Please give this booking reference number when you get the delivery"
        print "\nYour Booking Reference Number is", reference_number

def main():
    print "Welcome to 'OOHSbay.com'"
    print "\n"
    n=input("Enter the number of items you want to buy: ")
    total_price=0
    overall_items=[]
    overall_warranty=[]
    overall_price=[]
    for i in range(n):
        process()
        q=overall_items.append(k)
        w=overall_warranty.append(s)
        e=overall_price.append(d)
        total_price+=x

    shipping_detials()
    print "\n\n\n"

    print "NEXT -"
    print "1. Print Bill"
    print "\nEnter '1' to print your bill"
    print "\nREMEMBER: SHOW PRINTED COPY OF YOUR BILL WHEN YOU SHIP YOUR PRODUCTS"
    bill_choice=input("Enter your choice: ")

    print "SLNO", "\t\t\t\t\t", "ITEM", "\t\t\t\t\t", "WARRANTY", "\t\t", "PRICE"
    for i in range(n):
        print " ", i+1, "\t\t\t\t\t", overall_items[i], "\t\t\t\t", overall_warranty[i], "\t\t\t", overall_price[i],"Dhs"

    print "Your Booking Reference Number is :",reference_number

    if shipping_choice==1:
        print "Your total cost is", total_price+60,"Dhs."
        print"Your product will arrive in 3 days!"
    elif shipping_choice==2:
        print "Your total cost is", total_price,"Dhs."

main()
