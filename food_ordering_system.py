#!/usr/bin/env python
# coding: utf-8

# In[51]:


import re


class FoodApp:

    # main code
    def __init__(self):
        self.foodapp_name = "KillHunger"
        self.admin_details = {}
        self.user_details = {}
        self.food = {}
        # adding +1 in exixting dict item number
        self.food_id = len(self.food) + 1
        self.foodkart = {}
        self.or_history = len(self.foodkart) + 1
        self.order = {}

    def admin_reg(self):
        ''' Admin Registration '''
        self.name = input("Entre Youre Full Name\n")
        while True:
            number = input("entre your phone number\n")
            if number.isnumeric() == True:
                if len(number) == 10:
                    self.number = number
                    break
                else:
                    print("number should contain only 10 numbers\n")
            else:
                print("Please Entre Numbers Only\n")
        while True:
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            email = input("Entre Your Email Id here\n")
            if (re.fullmatch(regex, email)):
                self.email = email
                break
            else:
                print("Invalid Email\n")
        while True:
            print("Password must Contain min 8 characters\n")
            password = input("Entre Your Password Here\n")
            if len(password) >= 8:
                self.password = password
                break
            else:
                print("Please Entre Minimum 8 Characters\n")

        self.admin_details = {"NAME": self.name, "EMAIL": self.email, "NUMBER": self.number,
                              "PASSWORD": self.password}  # add collected data in to dict to use it in future
        print("    !!!CONGRATULATIONS!!!       \nAccount Created Succsessfully/n")

    def admin_login(self, email, Password):
        '''registerd admin can login For That You need Rgisterd Email And Password'''
        if self.admin_details["EMAIL"] == email and self.admin_details["PASSWORD"] == Password:
            print("!!!!!Login successfully!!!!!")
            print(f'Welocme {self.admin_details["NAME"]}')
            return True
        else:
            print("Check email and password again")

    def add_food_item(self, name, quantity, price, discount, stock):
        '''add food items to the list which is availble in the Your restaurent'''
        self.item = {'NAME': name, 'QUANTITY': quantity, 'PRICE': price, 'DISCOUNT': discount,
                     'STOCK': stock}  # add data in dict
        self.foodid = len(self.food) + 1  # to genrate food item autometiclly
        self.food[self.foodid] = self.item
        print('\n!! Item Added Successfully !!\n')

    def edit_food_item(self, foodid):
        '''You Can edit available food items from list Here'''
        try:
            if len(self.food) > 0:  # to check if list is empty or not
                print(
                    "\n1.Edit Food Name\n2.Edit Quantity of food\n3.Edit Price\n4.Edit Discount\n5.Edit stock")
                while True:
                    Echoice = int(input("\nEntre Choice From Above List\n"))
                    if Echoice == 1:
                        new_name = input("Entre New Food Name\n")
                        # to edit dict values with new values
                        self.food[foodid]['NAME'] = new_name
                        print('\n!! Name updated Successfully !!')
                        break
                    elif Echoice == 2:
                        new_qun = input("Entre New Quantity\n")
                        self.food[foodid]['QUANTITY'] = new_qun
                        print('\n!! Quantity updated Successfully !!')
                        break
                    elif Echoice == 3:
                        while True:
                            new_PRICE = input("Entre New Price\n")
                            if new_PRICE.isnumeric() == True:
                                new_PRICE = int(new_PRICE)
                                self.food[foodid]['PRICE'] = new_PRICE
                                print('\n!! Price updated Successfully !!')
                                break
                            else:
                                print("Entre only numeric value")
                    elif Echoice == 4:
                        while True:
                            new_Discount = input("Entre New Discount\n")
                            if new_Discount.isnumeric() == True:
                                new_Discount = int(new_Discount)
                                self.food[foodid]['DISCOUNT'] = new_Discount
                                print('\n!! Discount updated Successfully !!')
                                break
                            else:
                                print("Entre only numeric value")
                    elif Echoice == 5:
                        while True:
                            new_stock = input("Entre New stock\n")
                            if new_stock.isnumeric() == True:
                                new_stock = float(new_stock)
                                self.food[foodid]['STOCK'] = new_stock
                                print('\n!! stock updated Successfully !!')
                                break
                            else:
                                print("Entre only numeric value")
                    else:
                        print("Invalid Input\n")
            else:
                print('\nNO FOOD ITEMS AVAILABLE NOW FOR EDIT\n')
        except Exception as e:
            print('!! ENTERED INVALID FOOD ITEM DETAILS !!\n')

    def view_food_item(self):
        '''List of Food Items Which is added by admin'''
        if len(self.food) != 0:
            for i in self.food:
                print(
                    f"ID: {i} | NAME: {self.food[i]['NAME']} | PRICE: {self.food[i]['PRICE']} | DISCOUNT: {self.food[i]['DISCOUNT']} | STOCK: {self.food[i]['STOCK']}")
        else:
            print('\nNO FOOD ITEMS AVAILABE NOW FOR VIEW')

    def delete_food_item(self, foodid):
        '''function for delete food items from list'''
        if len(self.food) != 0:
            if foodid in self.food.keys():
                del self.food[foodid]
                print('\n!!Deleted Successfully !!\n')
            else:
                print('Invalid Food ID\n')
        else:
            print('\nNo food Items Availble  Now For  Delete')

    # user function

    def user_reg(self):  # using "u" to indicate user
        '''USER REGISTRATION FUNCTION'''
        self.uname = input("Entre Your Full Name = \n")
        while True:
            uphone = input("Entre Your Phone Number\n")
            if uphone.isnumeric() == True:
                if len(uphone) == 10:
                    self.uphone = uphone
                    break
                else:
                    print("Invalid Phone Number\n")
            else:
                print("Invalid Phone Number\n")
        while True:
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            uemail = input("Entre Your Email  here= \n")
            if (re.fullmatch(regex, uemail)):
                self.uemail = uemail
                break
            else:
                print("Invalid Email")
        while True:
            print("Password must Contain min 8 characters")
            upassword = input("Entre Your Password Here\n")
            if len(upassword) >= 8:
                self.upassword = upassword
                break
            else:
                print("Please Entre Minimum 8 Characters\n")
        self.address = input("Entre Your Full Address Here\n")
        self.user_details = {"NAME": self.uname, "PHONE": self.uphone, "EMAIL": self.uemail, "PASSWORD": self.upassword,
                             "ADDRESS": self.address}
        print("    !!!CONGRATULATIONS!!!       \nAccount Created Succsessfully/n")

    def user_login(self, uemail, upassword):
        '''USER LOGIN FOR THAT YOU NEED REGISTERD EMAIL AND PASSWORD'''
        if len(self.user_details) > 0:
            if self.user_details["EMAIL"] == uemail and self.user_details["PASSWORD"] == upassword:
                print("!!!!!Login successfully!!!!!")
                print(f"Welcome {self.user_details['NAME']}")
                return True
            else:
                print("Check email and password again\n")
        else:
            print("This Email Is Not Registerd With Us Please Register First")

    def user_show_food_list(self):
        '''Function to show food list which is adeed by admin to the user'''
        if len(self.food) != 0:
            for i in self.food:
                print(
                    f"ID: {i} | NAME: {self.food[i]['NAME']} | PRICE: {self.food[i]['PRICE']} | QUANTITY: {self.food[i]['QUANTITY']}")
        else:
            print("Nothing To Show Here\n")

    def show_user_profile(self):
        '''function to show info about user that was given by user'''
        print(
            f" Name= {self.user_details['NAME']}\n Phone Number= {self.user_details['PHONE']}\n EMAIL= {self.user_details['EMAIL']}\n ADDRESS= {self.user_details['ADDRESS']}\n ")

    def update_User_Profile(self, upassword):
        '''function to update profile info'''
        if self.user_details["PASSWORD"] == upassword:
            while True:
                print(
                    " 1.Update Your Name\n 2.Update Your Phone Number\n 3.Upadte Your Email\n 4.Update Your Address\n 5.Update Your Password\n 6.Back")
                upchoice = input('Entre Your Choice\n')
                if upchoice == '1':
                    print(
                        f"Your Currunt Profile Name is{self.user_details['NAME']}")
                    newname = input("Entre new Name \n")
                    self.user_details['NAME'] = newname
                    print(" Name Updated")
                elif upchoice == '2':
                    print(
                        f"Your Currunt Phone Number is{self.user_details['PHONE']}")
                    while True:
                        newnum = input("Entre new Number \n")
                        if newnum.isnumeric() == True:
                            if len(newnum) == 10:
                                self.user_details['PHONE'] = newnum
                                print("Phone Number Updated")
                                break
                            else:
                                print("Invalid Phone Number")
                        else:
                            print("Invalid Phone Number")
                elif upchoice == '3':
                    print(f"Your Currunt Email is{self.user_details['EMAIL']}")
                    while True:
                        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
                        newemail = input("Entre Your Email  here= \n")
                        if (re.fullmatch(regex, newemail)):
                            self.user_details['EMAIL'] = newemail
                            print("Email Updated")
                            break
                        else:
                            print("Invalid Email")
                elif upchoice == '4':
                    print(
                        f"Your Currunt Address is{self.user_details['ADDRESS']}")
                    newadd = input("Entre new Email \n")
                    self.user_details['ADDRESS'] = newadd
                    print("Address Upadted")
                elif upchoice == '5':
                    print("Password must Contain min 8 characters")
                    while True:
                        newpass = input("Entre new Password \n")
                        if len(newpass) >= 8:
                            self.user_details['PASSWORD'] = newpass
                            print("Password Updated")
                            break
                        else:
                            print("Please Entre Minimum 8 Characters")
                elif upchoice == '6':
                    break
                else:
                    print("PLEASE GIVE VALID INPUT")
        else:
            print("Wrong Password Entre Valid Password To continue")

    def add_food_kart(self, food_id):
        '''function to add food item in cart'''
        food_id = int(food_id)
        if food_id in self.food.keys():
            if self.food[food_id]['STOCK'] > 0:
                if food_id in self.foodkart.keys():
                    self.foodkart[food_id]["QTY"] = self.foodkart[food_id]["QTY"] + 1
                    self.foodkart[food_id]['TOTAL'] = self.foodkart[food_id]['TOTAL'] + \
                        self.food[food_id]['PRICE']
                    self.foodkart[food_id] = {"NAME": self.food[food_id]['NAME'], "PRICE": self.food[food_id]['PRICE'],
                                              "QTY": self.foodkart[food_id]["QTY"],
                                              "TOTAL": self.foodkart[food_id]['TOTAL']}
                    self.food[food_id]['STOCK'] = self.food[food_id]['STOCK'] - 1
                else:
                    self.foodkart[food_id] = {"NAME": self.food[food_id]['NAME'], "PRICE": self.food[food_id]['PRICE'],
                                              "QTY": 1, "TOTAL": self.food[food_id]['PRICE']}
                    self.food[food_id]['STOCK'] = self.food[food_id]['STOCK'] - 1
            else:
                print(
                    F" {self.food[food_id]['NAME']} Not Available At This Moment")
        else:
            print(f'Opps!!! You Entered {food_id} is Wrong ID')

    def show_kart(self):
        '''function to show cart items to user'''
        if len(self.foodkart) > 0:
            for i in self.foodkart:
                print(
                    f" ID={i} | NAME: {self.foodkart[i]['NAME']} | PRICE: {self.foodkart[i]['PRICE']} | QUANTITY : {self.foodkart[i]['QTY']} | TOTAL : {self.foodkart[i]['TOTAL']}")
        else:
            print("Kart is Empty now add something")

    def orde_history(self):
        '''all orders history will be save here'''
        for i in self.foodkart.keys():
            self.order[self.or_history] = {"NAME": self.foodkart[i]['NAME'], "PRICE": self.foodkart[i]['PRICE'],
                                           "QTY": 1, "TOTAL": self.foodkart[i]['PRICE']}
            self.or_history = self.or_history + 1

    def show_order_history(self):
        '''all orders history user can check here'''
        if len(self.order) > 0:
            for i in self.order:
                print(
                    f" Id: {i} | NAME: {self.order[i]['NAME']} | PRICE: {self.order[i]['PRICE']} | QTY: {self.order[i]['QTY']} | TOTAL: {self.order[i]['TOTAL']}")
        else:
            print("Nothing TO Show Order Something First")

    def delete_kart_item(self, foodid):
        '''function for delete food items from list'''
        if len(self.foodkart) != 0:
            if foodid in self.foodkart.keys():
                self.food[foodid]['STOCK'] = self.food[foodid]['STOCK'] + \
                    self.foodkart[foodid]['QTY']
                del self.foodkart[foodid]
                print('\n!!Deleted Successfully !!\n')
            else:
                print('Invalid Food ID\n')
        else:
            print('\nNo food Items Availble  Now For  Delete')


def Driver_code():
    '''driver code to run main functiom'''
    obj = FoodApp()
    print(obj.admin_login.__doc__)
    while True:
        print(
            f'Welcome to {obj.foodapp_name} We are here to Take Care Of Your Hunger\n')
        print("Please Entre Your Selction from Below Options\n")
        print('1. ADMIN')
        print('2. USER')
        print('3. CLOSE\n')
        Dinput = input('Enter Your Selection : \n')
        if Dinput == '1':
            while True:
                print('\n1. ADMIN REGISTER')
                print('2. ADMIN LOGIN')
                print('3. BACK')
                Dinput2 = input('Enter Your Selection : \n')
                if Dinput2 == '1':
                    print(obj.admin_reg.__doc__)
                    obj.admin_reg()
                elif Dinput2 == '2':
                    print(obj.admin_login.__doc__)
                    email = input('ENTRE YOUR REGISTRED EMAIL : \n')
                    password = input('REGISTRED ADMIN PASSWORD : \n')
                    if obj.admin_login(email, password):
                        while True:
                            print('1. Add new food item')
                            print('2. Edit food item')
                            print('3. View food item')
                            print('4. Delete food item')
                            print('5. Back')
                            X = input('Enter Your Selection : \n')
                            if X == '1':
                                print(obj.add_food_item.__doc__)
                                name = input('Enter the food name : \n')
                                quantity = input(
                                    'Enter Updated Quantity like For eg, 100ml, 250gm, 4pieces etc : \n')
                                while True:
                                    price = input('Enter Updated Price ₹ : \n')
                                    if price.isnumeric() == True:
                                        price = int(price)
                                        break
                                    else:
                                        print("Only numeric value will execpted")
                                while True:
                                    discount = input(
                                        'Enter Updated Discount in ₹ : ')
                                    if discount.isnumeric() == True or discount.isdecimal() == True:
                                        discount = float(discount)
                                        break
                                    else:
                                        print("Only numeric value will execpted")
                                while True:
                                    stock = input('Enter Updated Stock : ')
                                    if stock.isnumeric() == True:
                                        stock = int(stock)
                                        break
                                    else:
                                        print("Only numeric value will execpted")
                                obj.add_food_item(
                                    name, quantity, price, discount, stock)
                            elif X == '2':
                                print("List Of Added Food Items")
                                obj.view_food_item()
                                foodid = int(input('Enter food id : '))
                                obj.edit_food_item(foodid)
                            elif X == '3':
                                obj.view_food_item()
                            elif X == '4':
                                foodid = int(input('Enter food id : '))
                                obj.delete_food_item(foodid)
                                print("Updated Food Items")
                                obj.view_food_item()
                            elif X == '5':
                                break
                            else:
                                print('Invalid option\n')
                    else:
                        print('INVALID EMAIL OR PASSOWRD')
                elif Dinput2 == '3':
                    break
                else:
                    print('INVALID OPTION')
        elif Dinput == '2':
            while True:
                print('\n1. USER REGISTER')
                print('2. USER LOGIN')
                print('3. BACK')
                uinput = input('Enter Your Selection : ')
                if uinput == '1':
                    obj.user_reg()
                elif uinput == '2':
                    uemail = input("Enter Your Registerd Email Here = ")
                    upassword = input("Entre Your Password ")
                    if obj.user_login(uemail, upassword):
                        while True:
                            print('1. Place Order')
                            print('2. Show Order History')
                            print('3. Show Profile Details')
                            print('4. Edit Profile Details')
                            print('5. Back')
                            uinput2 = input("Entre Your Choice")
                            if uinput2 == '1':
                                while True:
                                    print('1. Show Food Items')
                                    print('2. Add Food Items In Your kart')
                                    print('3. Delete Food Items From Your Kart')
                                    print('4. Show Kart')
                                    print('5. Back')
                                    uinput3 = input("Entre Your Choice\n")
                                    if uinput3 == '1':
                                        obj.view_food_item()
                                    elif uinput3 == '2':
                                        if len(obj.food) > 0:
                                            food_id = input(
                                                "Entre food Id Seprated By comma ex: 1,2,3,4,4,4 \n")
                                            for i in food_id:
                                                if i.isnumeric() == True:
                                                    obj.add_food_kart(i)
                                                else:
                                                    pass
                                            while True:
                                                print(
                                                    "1. Show Kart\n2. Place Order\n3.Back ")
                                                oinput = input(
                                                    "Entre Your Choice \n")
                                                if oinput == "1":
                                                    obj.show_kart()
                                                if oinput == "2":
                                                    if len(obj.foodkart) > 0:
                                                        print(
                                                            "We are preparing Your Order. ")
                                                        print(
                                                            "After Ready Your Order We Will be delivered at Your Location ")
                                                        print(
                                                            f"Address= {obj.user_details['ADDRESS']}")
                                                        obj.orde_history()
                                                        obj.foodkart = {}
                                                        break
                                                    else:
                                                        print(
                                                            "nothing is added in cart to place your order")
                                                elif oinput == "3":
                                                    break
                                                else:
                                                    print(
                                                        "Please Give Correct Input")
                                        else:
                                            print(
                                                "No Items Are Available At This Moment/n Please Visit again.")
                                    elif uinput3 == '3':
                                        if len(obj.foodkart) > 0:
                                            foodid = int(
                                                input('Enter food id : '))
                                            obj.delete_kart_item(foodid)
                                            print("Updated Food Items")
                                            obj.show_kart()
                                        else:
                                            print("Nothing to Remove")
                                    elif uinput3 == '4':
                                        obj.show_kart()
                                        if len(obj.foodkart) > 0:
                                            while True:
                                                print(
                                                    "1. Place Order\n2.Back ")
                                                oinput = input(
                                                    "Entre Your Choice \n")
                                                if oinput == "1":
                                                    print(
                                                        "We are preparing Your Order. ")
                                                    print(
                                                        "After Ready Your Order We Will be delivered at Your Location ")
                                                    print(
                                                        f"Address= {obj.user_details['ADDRESS']}")
                                                    obj.orde_history()
                                                    obj.foodkart = {}
                                                    break
                                                elif oinput == "2":
                                                    break
                                                else:
                                                    print("Invalid Option")
                                        else:
                                            print(
                                                "Kart Is Empty Please Add Something...")
                                    elif uinput3 == "5":
                                        break
                            elif uinput2 == '2':
                                obj.show_order_history()
                            elif uinput2 == '3':
                                obj.show_user_profile()
                            elif uinput2 == '4':
                                upassword = input("Entre Your Password ")
                                obj.update_User_Profile(upassword)
                            elif uinput2 == "5":
                                break
                            else:
                                print("PLEASE GIVE VALID INPUT")
                    else:
                        print("Wrong Id OR Password")
                elif uinput == '3':
                    break
                else:
                    print("Entre Valid Input")
        elif Dinput == '3':
            break
        else:
            print('Please enter again')


if __name__ == "__main__":
    Driver_code()

print('THANK YOU VISIT AGAIN :')
