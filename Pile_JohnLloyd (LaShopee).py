def encrypt(credential):
    encrypted_credential = ""
    for char in credential:
        encrypted_credential += chr((ord(char)-10))
    return encrypted_credential
def decrypt(credential):
    decrypted_credential = ""
    for char in credential:
        decrypted_credential += chr((ord(char)+10))
    return decrypted_credential
def validateLoginInfo(username, password):
    try:
        with open("21-0411.txt", "r") as file:
            datas = [decrypt(data.strip()) for data in file.readlines()]
        if "user"+username in datas and "pass"+password+username in datas:
            return True
        else:
            return False
    except:
        return False
def accountCreator():
    print("\nEnter your desired username: ", end="")
    while True:
        username = input()
        if bool(username) and not username.isspace() and username.isascii() and len(username)<=10:
            try:
                with open("21-0411.txt", "r") as file:
                    datas = [line.strip() for line in file.readlines()]
                    if username in datas:
                        print(f"\n{username} is already taken, please try a new one.\nDesired username: ", end="")
                    else:
                        break
            except:
                break
        else:
            if len(username)>10: print("\n"+"We only accept a maximum of 10 characters for usernames".center(70,"-")+"\n\nPlease try modifying it: ", end="")
            elif username.isascii(): print("\nPlease enter a username: ", end="")
            else: print("\n"+"Your username seems to have non-ASCII character/s".center(70,"-")+"\n\nPlease try modifying it: ", end="")
    print("Enter your desired password: ", end="")
    while True:
        password = input()
        if bool(password) and not password.isspace() and password.isascii() and len(password) <=50:
            print("Enter your shipping address: ", end="")
            while True:
                address = input()
                if bool(address) and not address.isspace() and len(address)<=150 and address.isascii():
                    with open("21-0411.txt", "a") as file:
                        file.write(f"{username}\n" + encrypt("user"+username) +"\n"+ encrypt("pass"+password+username)+"\n"+f"{address}\n"+f"{username}'s profile ending\n")
                    return username
                else:
                    if not address.isascii(): print("\n"+"Your address seems to have non-ASCII character/s".center(70,"-")+"\n\nPlease try modifying it: ", end="")
                    elif len(address) <= 150: print("\nPlease enter a shipping address: ", end="") 
                    else: print("\nYour shipping address is too long.\nTry making is shorter: ", end="") 
        else:
            if len(password)>50: print("\n"+"We only accept a maximum of 50 characters for passwords".center(70,"-")+"\n\nPlease try modifying it: ", end="")
            elif password.isascii(): print("\nPlease enter a password: ", end="")
            else: print("\n"+"Your password seems to have non-ASCII character/s".center(70,"-")+"\n\nPlease try modifying it: ", end="")
def displayOpeningMenu():
    global active_account_OR_selection
    try:
        with open("21-0411.txt", "r") as file:
            data = file.readlines()
            file_not_empty = len(data) > 0
    except:
        file_not_empty = False
    if file_not_empty:
        print("\n\n"+"Greetings, Lashopper!".center(70, "-")+"\n\n[1] Log in\n[2] Create an account\n[3] Exit\n\nAlready have an account? Select [1] and log in then!\nSelection: ",end="")
    else:
        print("\n\n"+"Greetings, Lashopper!".center(70, "-")+"\n\n[1] Log in\n[2] Create an account\n[3] Exit\n\nSelection: ",end="")
    while True:
        user_logIn_selection = input()
        if user_logIn_selection == "1":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            account_exists = validateLoginInfo(username, password)
            if account_exists:
                print("\n"+f"Welcome back, {username}!".center(70,"-"), end="")
                active_account_OR_selection = username
                return dispalyMainMenu()
            else:
                print("\n"+"There seems to be no such account.".center(70,"-")+"\n\n[1] Log in\n[2] Create an account\n[3] Exit\n\nTry creating one instead.\nSelection: ", end="")
        elif user_logIn_selection == "2":
            active_account = accountCreator()
            print("\n"+f"Welcome to the shop, {active_account}!".center(70, "-"), end="")
            active_account_OR_selection =  active_account
            return dispalyMainMenu()
        elif user_logIn_selection == "3":
            print(f"\nThank you and please come again :)")
            return 
        else:
            print("\n"+"Invalid selection, please try again.".center(70,"-")+"\n\n[1] Log in\n[2] Create an account\n[3] Exit\n\nSelection: ",end="")
def dispalyMainMenu(): 
    while True:
        menu_selection = input("\n"+"Main Menu".center(70,"-") + "\n[1] Products\n[2] Purchase History\n[3] Cart\n[4] Account\n[5] Log Out\n\nSelection: ")
        if menu_selection == "1": return displayProducts()
        elif menu_selection=="2": return viewHistory(active_account_OR_selection)
        elif menu_selection=="3": return displayCart(active_account_OR_selection)
        elif menu_selection=="4": return viewAccount(active_account_OR_selection)
        elif menu_selection=="5": 
            print("\n"+f"Thanks for shopping, {active_account_OR_selection}. Please come again :)".center(70, "-"), end="")
            return displayOpeningMenu()
        else:
            print("\n"+"Invalid selection, please try agin.".center(70,"-"), end="")
def displayProducts():
    while True:
        address = viewAccount(active_account_OR_selection, get_address=True)
        after_purchase_statement = "\n"+"Kindly wait for a couple of days to be delivered".center(70,"-")+f"\n\nTo your Shipping Address: {address}"
        product_selection = input("\n"+"Products".center(70,"-")+"\n\n• [1] Facemask (₱25)\n• [2] Faceshield (₱5)\n• [3] Alcohol (₱50)"+"\n\n"+"  [1] Add To Cart".ljust(26)+" [2] Buy Now".ljust(23)+"[3] Back to Main Menu"+"\n\nSelection: ")
        if product_selection in ["1", "2"]:
            print("\nEnter product number: ", end="")
            product_selection_itirator = True
            while product_selection_itirator:
                selected_product = input()
                if selected_product in ["1","2","3"]:
                    print("Enter quantity: ", end="")
                    while True:
                        try:
                            quantity = int(input())
                            if  0 < quantity <= 100:
                                if product_selection=="1":
                                    if selected_product == "1":
                                        if quantity > 1:
                                            addToCart(active_account_OR_selection, f"{quantity} PCS of Facemasks {quantity*25}")
                                            print("\n"+f"{quantity} PCS of Facemasks has been successfully added to Cart".center(70,"-"),end="")
                                        else:
                                            addToCart(active_account_OR_selection, f"{quantity} PC of Facemask 25")
                                            print("\n"+f"{quantity} PC of Facemask has been successfully added to Cart".center(70,"-"),end="")
                                        product_selection_itirator = False
                                        break    
                                    elif selected_product == "2":
                                        if quantity > 1:
                                            addToCart(active_account_OR_selection, f"{quantity} PCS of Faceshields {quantity*5}")
                                            print("\n"+f"{quantity} PCS of Faceshields has been successfully added to Cart".center(70,"-"),end="")
                                        else:
                                            addToCart(active_account_OR_selection, f"{quantity} PC of Faceshield 5")
                                            print("\n"+f"{quantity} PC of Faceshield has been successfully added to Cart".center(70,"-"),end="")
                                        product_selection_itirator = False
                                        break
                                    else:
                                        if quantity > 1:
                                            addToCart(active_account_OR_selection, f"{quantity} PCS of Alcohols {quantity*50}")
                                            print("\n"+f"{quantity} PCS of Alcohols has been successfully added to Cart".center(70,"-"),end="")
                                        else:
                                            addToCart(active_account_OR_selection, f"{quantity} PC of Alcohol 50")
                                            print("\n"+f"{quantity} PC of Alcohol has been successfully added to Cart".center(70,"-"),end="")
                                        product_selection_itirator = False
                                        break
                                else:
                                    if selected_product == "1":
                                        if quantity > 1:
                                            saveToHistory(active_account_OR_selection, f"Purchased {quantity} PCS of Facemasks")
                                            print("\n"+f"Thanks for purchasing {quantity} PCS of Facemasks, {active_account_OR_selection}!".center(70, "-")+ after_purchase_statement+f"\nTo pay: ₱{quantity*25+60} ( + Shipping Fee )") 
                                        else:
                                            saveToHistory(active_account_OR_selection, f"Purchased {quantity} PC of Facemask")
                                            print("\n"+f"Thanks for purchasing {quantity} PC of Facemask, {active_account_OR_selection}!".center(70, "-")+ after_purchase_statement+"\nTo pay: ₱85 ( + Shipping Fee )")
                                        product_selection_itirator = False
                                        break
                                    elif selected_product == "2":
                                        if quantity > 1:
                                            saveToHistory(active_account_OR_selection, f"Purchased {quantity} PCS of Faceshields")
                                            print("\n"+f"Thanks for purchasing {quantity} PCS of Faceshields, {active_account_OR_selection}!".center(70, "-")+ after_purchase_statement+f"\nTo pay: ₱{quantity*5+60} ( + Shipping Fee )")
                                        else:
                                            saveToHistory(active_account_OR_selection, f"Purchased {quantity} PC of Faceshield")
                                            print("\n"+f"Thanks for purchasing {quantity} PC of Faceshield, {active_account_OR_selection}!".center(70, "-")+ after_purchase_statement+"\nTo pay: ₱65 ( + Shipping Fee )")
                                        product_selection_itirator = False
                                        break
                                    else:
                                        if quantity > 1:
                                            saveToHistory(active_account_OR_selection, f"Purchased {quantity} PCS of Alcohols")
                                            print("\n"+f"Thanks for purchasing {quantity} PCS of Alcohols, {active_account_OR_selection}!".center(70, "-")+ after_purchase_statement+f"\nTo pay: ₱{quantity*50+60} ( + Shipping Fee )")
                                        else: 
                                            saveToHistory(active_account_OR_selection, f"Purchased {quantity} PC of Alcohol")
                                            print("\n"+f"Thanks for purchasing {quantity} PC of Alcohol, {active_account_OR_selection}!".center(70, "-")+ after_purchase_statement+"\nTo pay: ₱110 ( + Shipping Fee )")
                                        product_selection_itirator = False
                                        break
                            else:
                                print("\nSorry. We only sell for a maximum quantity of 100 PCS.\nPlease modify your purchase quantity: ", end="") if quantity >100 \
                                else print("\nPlease enter a sensible quantity: ", end="")
                        except:
                            print("\nPlease enter a valid quantity: ", end="")
                else:
                    if selected_product =="4":
                        break
                    else:
                        print("\n"+"Please select a product".center(70,"-")+"\n\n• [1] Facemask (₱25)\n• [2] Faceshield (₱5)\n• [3] Alcohol (₱50)\n• [4] Back to Product Menu\n\nSelection: ", end="") if not bool(selected_product) or selected_product.isspace() \
                        else print("\n"+"Please select an existing product number".center(70,"-")+"\n\n• [1] Facemask (₱25)\n• [2] Faceshield (₱5)\n• [3] Alcohol (₱50)\n• [4] Back to Product Menu\n\nSelection: ", end="")
        else:
            if product_selection == "3":
                return dispalyMainMenu()  
            else:
                print("\n"+"Invalid selection, please try agin.".center(70,"-"), end="")
def saveToHistory(username, activity_or_product):
    try:
        with open("21-0411.txt", "r") as file:
            data =file.readlines()
            if f"{username}'s Purchase History\n" in data:
                data.insert((data.index(f"{username}'s Purchase History\n"))+1, f"{activity_or_product}\n")
            else:
                data.insert((data.index(f"{username}\n")+3), f"{username}'s Purchase History\n{activity_or_product}\n{username}'s End of History\n")
        with open("21-0411.txt", "w") as file:
            file.writelines("".join(data))
        return False
    except:
        return True
def viewHistory(active_account):
    try:
        while True:
            with open ("21-0411.txt", "r") as file:
                data = file.readlines()
            if not f"{active_account}\n" in data: 
                print(error_occured_statement)
                return displayOpeningMenu()
            if f"{active_account}'s Purchase History\n" not in data:
                print("\n"+"Purchase History is empty.".center(70, "-"), end="")
                return dispalyMainMenu()
            else:
                purchase_history = data[data.index(f"{active_account}'s Purchase History\n")+1 : data.index(f"{active_account}'s End of History\n")] 
                filtered_purchase_history = [datum.strip() for datum in purchase_history]
                num_of_activity = len(filtered_purchase_history)
                cloned_num_of_activity = len(filtered_purchase_history)
                spacer = len(str(cloned_num_of_activity))+5
                max_activity_len = max([len(activity) for activity in filtered_purchase_history])
                print("\n"+"Purchase History".center(70,"-")+"\n")
                print(("_".ljust(spacer, "_")+ "_"+"_".center(max_activity_len+6, "_")+"_").center(70))
                print(("|".ljust(spacer)+ "|"+" ".center(max_activity_len+6)+"|").center(70))
                print(("| No.".ljust(spacer)+ "|" + "Activity".center(max_activity_len+6)+"|").center(70))
                print(("|"+"|".rjust(spacer,"-") + "-".center(max_activity_len+6, "-")+"|").center(70))
                for datum in filtered_purchase_history:
                    print(("| "+str(cloned_num_of_activity).center(spacer-2) +"|   "+ datum.ljust(max_activity_len+3)+"|").center(70))
                    cloned_num_of_activity-=1
                print(("|".ljust(spacer,"_")+ "|"+"_".center(max_activity_len+6,"_")+"|").center(70))
                history_selection = input("\n"+"[1] Delete all\n[2] Delete specific activity\n[3] Back to Main Menu\n\nSelection: ")
                if history_selection =="1":
                    print("\n"+"History is now cleared".center(70,"-"), end="")
                    deleteActivitiesOrAccount(active_account_OR_selection, delete_all=True)
                    return dispalyMainMenu()
                elif history_selection == "2":
                    while True:
                        activity_num = input("\nEnter the activity number to be deleted: ")
                        try:
                            if 0 < int(activity_num) <= num_of_activity:
                                deleteActivitiesOrAccount(active_account_OR_selection, activity_num)
                                print("\n" + f"Activity number {activity_num} has been successfully deleted".center(70,"-"), end="")
                                break 
                            else:
                                print("\n"+"There's no such activity number.".center(70,"-")+"\n"+"Please try again.".center(70,"-"))
                        except:
                            print("\n"+"Please enter a valid activity number.".center(70,"-"))
                elif history_selection == "3":
                    return "3"
                else:
                    print("\n"+"Invalid selection, please try again.".center(70,"-"), end="")
    except:
        print(error_occured_statement)
        return displayOpeningMenu()
def deleteActivitiesOrAccount(active_account,activity_or_product_num=None, delete_all = False, for_cart =False):
        try:
            with open ("21-0411.txt", "r") as file:
                data = file.readlines()
            if activity_or_product_num==None and not delete_all and not for_cart:
                del data[data.index(f"{active_account}\n") : data.index(f"{active_account}'s profile ending\n")+1]
            elif delete_all:
                if for_cart: del data[data.index(f"{active_account}'s Cart\n") : data.index(f"{active_account}'s Cart Ending\n")+1]
                else: del data[data.index(f"{active_account}'s Purchase History\n") : data.index(f"{active_account}'s End of History\n")+1]
            else:
                if for_cart: num_of_activity_or_product = len(data[data.index(f"{active_account}'s Cart\n")+1:data.index(f"{active_account}'s Cart Ending\n")])
                else: num_of_activity_or_product = len(data[data.index(f"{active_account}'s Purchase History\n")+1:data.index(f"{active_account}'s End of History\n")])
                if num_of_activity_or_product==1:
                    if for_cart: del data[data.index(f"{active_account}'s Cart\n") : data.index(f"{active_account}'s Cart Ending\n")+1]
                    else: del data[data.index(f"{active_account}'s Purchase History\n") : data.index(f"{active_account}'s End of History\n")+1]
                else:
                    if for_cart: del data[data.index(f"{active_account}'s Cart Ending\n")-activity_or_product_num]
                    else: del data[data.index(f"{active_account}'s End of History\n")-activity_or_product_num]
            with open ("21-0411.txt", "w") as file1:
                file1.writelines(data)
            return False
        except:
            print (error_occured_statement)
            return displayOpeningMenu()
def viewAccount(active_account, get_address=False):
    def changePassword(active_account):
        while True:
            print("\n"+"Account Password Change".center(70, "-")+"\n\n[1] Cancel\n")
            password = input("Enter you old password: ")
            if validateLoginInfo(active_account, password):
                while True:
                    new_password = input("\n"+"Account Password Change".center(70, "-")+"\n\nEnter your new password: ")
                    if bool(new_password) and not new_password.isspace() and new_password.isascii() and len(new_password) <=50:
                        try:
                            with open("21-0411.txt", "r") as file:
                                data = file.readlines()
                            data[data.index(f"{active_account}\n")+2] = encrypt("pass"+new_password+active_account)+"\n"
                            with open("21-0411.txt", "w") as file1:
                                file1.writelines(data)
                            print("\n"+"Your password has been successfully changed".center(70,"-"), end="")
                            return False
                        except:
                            return True
                    else:
                        if len(new_password)>50: print("\n"+"We only accept a maximum of 50 characters for passwords".center(70,"-")+"\n"+"Please try modifying it".center(70,"-"), end="")
                        elif new_password.isascii(): print("\n"+"Please enter something.".center(70,"-"), end="")
                        else: print("\n"+"Your password seems to have non-ASCII character/s".center(70,"-")+"\n"+"Please try modifying it".center(70,"-"), end="")
            elif password =="1":
                return False
            else:
                print("\n"+"Incorrect password, please try again".center(70,"-"), end="")
    try:
        account_itirator = True
        while account_itirator:
            with open("21-0411.txt", "r") as file:
                data = file.readlines()
            account = data[data.index(f"{active_account}\n")+1 : data.index(f"{active_account}\n")+3]
            username= decrypt(account[0][4:].strip()) 
            password = f"{account[1].strip()[4:-len(username)]} (Encrypted Format)"
            address = data[data.index(f"{active_account}'s profile ending\n")-1].strip()
            if get_address:
                return address
            print("\n"+"Your Account".center(70, "-"))
            print("\nUsername:", username +"\n"+"Password:", password+"\n"+"Shipping Address:", address)
            view_account_selection = input("\n[1] Change Password\n[2] Delete Account\n[3] Change Shipping Address\n[4] Back to Main Menu\n\nSelection: " )
            if view_account_selection=="1":
                error_occoured = changePassword(active_account)
                if error_occoured:
                    return True
                else:
                    continue
            elif view_account_selection=="2":
                while True:
                    confirmation = input("\n"+"Confirmation".center(70,"-")+"\n\nThis actoin will permanently delete all of your data.\nAre you sure want to proceed? [yes|no]\n\nAnswer: ")
                    if confirmation.lower() == "no":
                        break
                    elif confirmation.lower() == "yes":
                        return "2"
                    else:
                        print("\n"+"Please answer either yes or no".center(70,"-"), end="")
            elif view_account_selection=="3":
                return "3"
            elif view_account_selection=="4":
                return "4"
            else:
                print("\n"+"Invalid selection, please try again.".center(70,"-"), end="")
    except:
        print(error_occured_statement)
        return displayOpeningMenu()
def changeAddress(active_account):
        while True:
            print("\n"+"Account Shipping Address Change".center(70,"-"))
            new_address = input("\nEnter your new shipping address: ")
            if bool(new_address) and not new_address.isspace() and new_address.isascii() and len(new_address) <=150:
                try:
                    with open("21-0411.txt", "r") as file:
                        data = file.readlines()
                        data[data.index(f"{active_account}'s profile ending\n")-1] = new_address+"\n"
                    with open("21-0411.txt", "w") as file1:
                        file1.writelines(data)
                    return False
                except:
                    return True
            else:
                if not new_address.isascii(): print("\n"+"Your address seems to have non-ASCII character/s".center(70,"-")+"\n"+"Please try modifying it".center(70,"-"), end="")
                elif len(new_address) <= 150: print("\n"+"Please enter a shipping address".center(70,"-"), end="") 
                else: print("\n"+"Your shipping address is too long".center(70,"-")+"\n"+"Try making is shorter".center(70,"-"), end="")
def addToCart(active_account, product):
    try:
        with open("21-0411.txt", "r") as file:
            data = file.readlines()
        if f"{active_account}'s Cart\n" in data:
            data.insert(data.index(f"{active_account}'s Cart\n")+1, f"{product}\n")
        else:
            data.insert(data.index(f"{active_account}\n")+3, f"{active_account}'s Cart\n{product}\n{active_account}'s Cart Ending\n")
        with open("21-0411.txt", "w") as file:
            file.writelines(data)
    except:
        print (error_occured_statement)
        return displayOpeningMenu()
def displayCart(active_account):
    try:
        while True:
            with open("21-0411.txt", "r") as file:
                data = file.readlines()
            if not f"{active_account}\n" in data: return True
            if not f"{active_account}'s Cart\n" in data:
                print("\n"+"Your Cart is empty".center(70,"-"), end="")
                return "5"
            else:
                cart = data[data.index(f"{active_account}'s Cart\n")+1 : data.index(f"{active_account}'s Cart Ending\n")]
                filtered_cart = []
                for product in cart:
                    filtered_cart.append(" ".join(product.split()[:-1])+" ₱"+product.split()[-1])
                product_num = len(filtered_cart)
                cloned_product_num = len(filtered_cart)
                spacer = len(str(cloned_product_num))+5
                max_product_len = max([len(" ".join(prod.split()[:-1])) for prod in filtered_cart])
                max_cost_len = max(max([len(prod1.split()[-1]) for prod1 in filtered_cart]), 6)
                print("\n"+"Your Cart".center(70,"-")+"\n")
                print(("_"+"_".rjust(spacer,"_") + "_".center(max_product_len+5, "_")+"__"+"_".center(max_cost_len, "_")+"___").center(70))
                print(("|"+"|".rjust(spacer) + " ".center(max_product_len+5)+"| "+" ".center(max_cost_len)+"  |").center(70))
                print(("| No.".ljust(spacer)+ "|" + "Product".center(max_product_len+5)+"|"+"Cost".center(max_cost_len+3)+"|").center(70))
                print(("|"+"|".rjust(spacer,"-") + "-".center(max_product_len+5, "-")+"|-"+"-".center(max_cost_len, "-")+"--|").center(70))
                subtotal = 0
                for product1 in filtered_cart:
                    print(("|  "+str(cloned_product_num).ljust(spacer-3) +"|  "+ " ".join(product1.split()[:-1]).ljust(max_product_len+3)+"|  "+f"{product1.split()[-1]}".ljust(max_cost_len)+" |").center(70))
                    subtotal+=int(product1.split()[-1][1:])
                    cloned_product_num-=1
                print(("|"+"|".rjust(spacer,"_") + "_".center(max_product_len+5, "_")+"|_"+"_".center(max_cost_len, "_")+"__|").center(70))
                print("\n" + (f"Subtotal = ₱{subtotal}".ljust(max_product_len+7+spacer+max_cost_len)).center(70)) 
                cart_selection_itirator = True
                while cart_selection_itirator:
                    cart_selection = input("\n"+"[1] Check out all\n[2] Check out specific product\n[3] Edit product quantity\n[4] Remove\n[5] Back to Main Menu\n\nSelection: ")
                    if cart_selection =="1":
                        error_occured = saveToHistory(active_account, "".join(["Purchased "+" ".join(item.split()[:-1])+"\n" for item in cart])[:-1])
                        if error_occured: return True
                        else: return "1", subtotal
                    elif cart_selection == "2":
                        while True:
                            product_num_2checkOut = input("\nEnter the product number to be checked out: ")
                            try:
                                if 0 < int(product_num_2checkOut) <= product_num:
                                    error_occured = saveToHistory(active_account, "Purchased "+" ".join(cart[-int(product_num_2checkOut)].split()[:-1]))
                                    if error_occured: return True
                                    else:
                                        error_occured_or_address = viewAccount(active_account_OR_selection, get_address=True)
                                        if error_occured_or_address == True:
                                            return True
                                        print("\n"+f"Thanks for checking out {' '.join(cart[-int(product_num_2checkOut)][:-1].split()[:-1])}, {active_account_OR_selection}!".center(70,"-"), end="")
                                        print("\n"+"Kindly wait for a couple of days to be delivered".center(70,"-")+f"\n\nTo your Shipping Address: {error_occured_or_address}")
                                        print(f"Total amount to pay: ₱{int(cart[-int(product_num_2checkOut)][:-1].split()[-1])+60} ( + Shipping Fee )")
                                        return "2", int(product_num_2checkOut)
                                else:
                                    print("\n"+"There's no such product number.".center(70,"-")+"\n"+"Please try again.".center(70,"-"))
                            except:
                                print("\n"+"Please enter a valid product number.".center(70,"-"))
                    elif cart_selection == "3":
                        while True:
                            product_num_2edit = input("\nEnter the product number to be edited: ")
                            try:
                                if 1 <= int(product_num_2edit) <= product_num:
                                    while True:
                                        try:
                                            new_quantity = int(input("\nEnter new product quantity: "))
                                            if 1 <= new_quantity <= 100:
                                                return int(product_num_2edit), int(new_quantity)
                                            else:
                                                print("\n"+"Sorry. We only sell for a maximum quantity of 100 PCS.".center(70,"-")+"\n"+"Please modify your purchase quantity".center(70,"-"), end="") if new_quantity >100 \
                                                else print("\n"+"Please enter a sensible quantity".center(70,"-"), end="")
                                        except:
                                            print("\n"+"Please enter a valid quantity".center(70,"-"))
                                else:
                                    print("\n"+"There's no such product number.".center(70,"-")+"\n"+"Please try again.".center(70,"-"))
                            except:
                                print("\n"+"Please enter a valid product number.".center(70,"-"))
                    elif cart_selection=="4":
                        itirator_4cartRemoving = True
                        while itirator_4cartRemoving:
                            selected_option_4removing = input("\n"+"Remove from Cart".center(70,"-")+"\n\n[1] Remove all\n[2] Remove specific product\n[3] Cancel\n\nSelection: ")
                            if selected_option_4removing=="1":
                                error_occured = deleteActivitiesOrAccount(active_account, delete_all=True, for_cart=True)
                                if error_occured: return True
                                else: 
                                    print("\n"+"Your Cart has been successfully cleared".center(70,"-"), end="")
                                    return "5"
                            elif selected_option_4removing=="2":
                                while True:
                                    try:
                                        item_to_be_removed = int(input("Enter product number to be removed: "))
                                        if 0 < item_to_be_removed <= product_num:
                                            error_occured = deleteActivitiesOrAccount(active_account, item_to_be_removed, for_cart=True)
                                            if error_occured: return True
                                            else:
                                                if product_num==1:
                                                    print("\n"+f"{' '.join(cart[-item_to_be_removed][:-1].split()[:-1])} has been successfully removed from Cart".center(70,"-"),end="")
                                                    print("\n"+"Your Cart is now empty".center(70,"-"), end="")
                                                    return "5"
                                                else:
                                                    print("\n"+f"{' '.join(cart[-item_to_be_removed][:-1].split()[:-1])} has been successfully removed from Cart".center(70,"-"),end="")
                                                    itirator_4cartRemoving,cart_selection_itirator = False, False
                                                    break
                                        else:
                                            print("\n"+"There's no such product number.".center(70,"-")+"\n"+"Please try again.".center(70,"-"))
                                    except:
                                        print("\n"+"Please enter a valid product number".center(70,"-"))
                            elif selected_option_4removing=="3":
                                itirator_4cartRemoving,cart_selection_itirator = False, False
                            else:
                                print("\n"+"Invalid selection, please try again.".center(70,"-"), end="")
                    elif cart_selection=="5":
                        return "5"
                    else:
                        print("\n"+"Invalid selection, please try again.".center(70,"-"), end="")
                        cart_selection_itirator = False
    except:
        return True
def editCart(active_account, product_num, new_quantity):
    try:
        with open("21-0411.txt", "r") as file:
            data = file.readlines()
        if new_quantity >1:    
            updated_product = data[data.index(f"{active_account}'s Cart Ending\n")-product_num].split()
            updated_product[0],updated_product[1] = str(new_quantity), "PCS", 
            if not  updated_product[3].endswith("s"):updated_product[3]+="s"
            if updated_product[3] == "Facemask" or updated_product[3] == "Facemasks": updated_product[4] = str(25*new_quantity)+"\n" 
            elif updated_product[3] == "Faceshield" or updated_product[3] == "Faceshields": updated_product[4] = str(5*new_quantity)+"\n"
            else: updated_product[4] = str(50*new_quantity)+"\n"
            data[data.index(f"{active_account}'s Cart Ending\n")-product_num] = " ".join(updated_product)
        else:
            updated_product = data[data.index(f"{active_account}'s Cart Ending\n")-product_num].split()
            updated_product[0],updated_product[1] = str(new_quantity), "PC"
            if updated_product[3].endswith("s"): updated_product[3] = updated_product[3][:-1]
            if updated_product[3] == "Facemask" or updated_product[3] == "Facemasks": updated_product[4] = "25\n"
            elif updated_product[3] == "Faceshield" or updated_product[3] == "Faceshields": updated_product[4] = "5\n"
            else: updated_product[4] = "50\n"
            data[data.index(f"{active_account}'s Cart Ending\n")-product_num] = " ".join(updated_product)
        with open("21-0411.txt", "w") as file:
            file.writelines(data)
        return False
    except:
        return True

#-------------------------------------------------Start of the Beginning------------------------------------------
if __name__ == "__main__":
    active_account_OR_selection = ""
    error_occured_statement = "\n"+"Data storage has been manipulated.".center(70,"-")+"\n"+\
            f"{active_account_OR_selection}'s account is deleted for the system to work properly.".center(70,"-")+"\n"+"Usage of the deleted username is now available.".center(70,"-")
    displayOpeningMenu()
    

