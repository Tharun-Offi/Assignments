from datetime import date, timedelta
import getpass

class User:
    
    def CreateUser(self):
        while True:
            username = input("Enter Your Username : ")
            flag = True
            for i in user_db:
                if username == i[0]:
                    flag = False
                    break
            if not flag:
                print()
                print("Username Already Taken...")
                print("Try another Username...")
                print()
            else:
                break
        while True:
            password = getpass.getpass("Enter Your Password : ")
            confirm_password = getpass.getpass("Confirm Your Password : ")
            if password != '' and password == confirm_password:
                break
            else:
                print()
                print("Both the passwords Should be same and Password should not be empty...")
                print()
        while True:
            phone_number = input("Enter Your 10 digit Mobile Number : ")
            if len(phone_number) == 10 and phone_number.isdigit():
                break
            else:
                print()
                print("Invalid Mobile Number")
                print("Please Enter a Valid Mobile number...")
                print()
        while True:
            email = input("Enter Your E-Mail Id : ")
            if email.endswith(".com") and '@' in email and email.index('@') +1 != email.index('.'):
                break
            else:
                print()
                print("Invalid E-Mail ID")
                print("Please Enter a Valid E-Mail ID...")
                print()
        print("Enter Your Address...")
        door = input("Door Number : ")
        street = input("Street Name : ")
        area = input("Area : ")
        city = input("City : ")
        pincode = input("Postal code : ")
        user_db.append([username, password, phone_number, email, [door, street, area, city, pincode]])
        sub = Subscription()
        bil = Billing()
        feed = FeedBack()
        sub.CreateSubscription(username)
        bil.CreateBilling(username)
        feed.CreateFeedback(username)

    def UpdateUser(self, userinfo):
        index = user_db.index(userinfo)
        print("1 - Phone Number")
        print("2 - Email")
        print("3 - Address")
        print("4 - Back to Main Menu")
        print()
        ch = input()
        if ch == '1':
            print()
            while True:
                phone = input(f"Enter your Exixting mobile number ending with {userinfo[2][-3:]} : ")
                if phone == userinfo[2]:
                    temp = input("Enter your new Phone Number : ")
                    while True:
                        if len(temp) >= 10:
                            userinfo[2] = temp
                            break
                        else:
                            print("Enter a valid Mobile Number")
                    break
                else:
                    print("Invalid Number")
            print("Successfully Updated")
            print()
        elif ch == '2':
            print()
            while True:
                mail = input("Enter your new email to Update : ")
                if mail.endswith("@gmail.com") or mail.endswith("@yahoo.com") or mail.endswith("@outlook.com") or mail.endswith(".com"):
                    userinfo[3] = mail
                    break
                else:
                    print("Invalid Mail ID")
            print("Successfully Updated")
            print()
        elif ch == '3':
            print()
            door = input("Door Number : ")
            street = input("Street Name : ")
            area = input("Area : ")
            city = input("City : ")
            pincode = input("Postal code : ")
            userinfo[4] = [door, street, area, city, pincode]
            print("Successfully Updated")
            print()
        elif ch == '4':
            print("No Updation was Made")

        else:
            print("Invalid Input")
        user_db[index] = userinfo

    def CheckUser(self, username):
        for i in user_db:
            if i[0] == username:
                return True
                break
        else:
            return False

    def UserInfo(self, username):
        for i in user_db:
            if i[0] == username:
                return i
            
    def ShowInfo(self, userinfo):
        user_title = ['Username', 'Password', 'Phone Number', "Email", "Address"]
        for i in range(len(userinfo)-1):
            print(f"{user_title[i]} : {userinfo[i]}")
        print("Address : ",end="")
        for i in userinfo[-1]:
            print(i,end=" ")

class Subscription:

    def CreateSubscription(self, username):
        subscription_db.append([username])

    def SubscriptionPicker(self, username):
        for i in subscription_db:
            if i[0] == username:
                return subscription_db.index(i)

    def AddSubscription(self, username):
        flag = True
        plan = Service_plan()
        bill = Billing()
        while True:
            for i in range(len(service_db)):
                plan.ShowPlans(i)
            print()
            plan_id = input("Enter Your Plan ID : ")
            print()
            if plan_id.isdigit() and 1 <= int(plan_id) <= 5:
                plan_db = service_db[int(plan_id) - 1]
                break
            else:
                print("Invalid Plan ID")
                print()
        amount = plan_db[-1]
        subscription_id = len(subscription_db[self.SubscriptionPicker(username)])
        start = date.today()
        end = start + timedelta(days=30)
        subscription_db[self.SubscriptionPicker(username)].append([plan_id, subscription_id, 'Active', start.strftime("%d-%m-%Y"), end.strftime("%d-%m-%Y")])
        bill.AddBilling(username, end, subscription_id, amount = amount, last_bill_date = start)

    def ModifySubscription(self, subscription_id, username):
        serv = Service_plan()
        bill = Billing()
        index = self.SubscriptionPicker(username)
        selected = subscription_db[index]
        amount = service_db[index - 1][-1]
        while True:
            for i in range(len(service_db)):
                serv.ShowPlans(i)
            print()
            plan_id = input("Enter Your Plan ID : ")
            print()
            if plan_id.isdigit() and 1 <= int(plan_id) <= 5:
                plan_db = service_db[int(plan_id) - 1]
                break
            else:
                print("Invalid Plan ID")
                print()
        start = date.today()
        end = start + timedelta(days=30)
        subscription_db[index][int(subscription_id)] = ([plan_id, subscription_id, 'Active', start.strftime("%d-%m-%Y"), end.strftime("%d-%m-%Y")])
        bill.ModifyBill(username, subscription_id, end, amount, start)


    def CancelSubscription(self, cancellation, username):
        bill = Billing()
        feed = FeedBack()
        index = self.SubscriptionPicker(username)
        selected = subscription_db[index]
        selected.pop(int(cancellation))
        subscription_db[index] = selected

        index = bill.BillingPicker(username)
        selected = billing_db[index]
        selected.pop(int(cancellation))
        billing_db[index] = selected

    def CheckActiveSubscription(self, username):
        if len(subscription_db[self.SubscriptionPicker(username)]) > 1:
            return True
        else:
            return False

    def SubscriptionInfo(self, plan_id, subscription_details):
        serv = Service_plan()
        subscription_title = ['Plan ID', 'Subscription ID', 'Status', 'Start Date', 'End Date']
        serv.ShowPlans(plan_id)
        for i in range(2, len(subscription_title)):
            print(f"{subscription_title[i]} : {subscription_details[i]}")
        print()


class Service_plan:

    def __init__(self):
        pass

    def ShowPlans(self, plan_index):
        plan_title = ['Plan ID : ', 'Data Limit : ', 'Data Speed : ', 'Price : ']
        for j in range(len(plan_title)):
            if j == 3:
                print(f"{plan_title[j]}{service_db[plan_index][j]} per Month")
            else:
                print(f"{plan_title[j]}{service_db[plan_index][j]}")
        print()
    
    def Plans():
        return service_db

class Billing:
    
    def CreateBilling(self, username):
        billing_db.append([username])

    def BillingPicker(self, username):
        for i in billing_db:
            if i[0] == username:
                return billing_db.index(i)
    
    def AddBilling(self, username, end_date, subscription_id, amount, last_bill_date):
        billing_id = len(billing_db[self.BillingPicker(username)])
        while True:
            print("Select the Mode of Payment...")
            print("1 - Credit Card")
            print("2 - Debit Card")
            print("3 - UPI")
            print("4 - Net Banking")
            select = input("Enter The Value : ")
            if select == "1":
                mode = "Credit Card"
                break
            elif select == "2":
                mode = "Debit Card"
                break
            elif select == "3":
                mode = "UPI"
                break
            elif select == "4":
                mode = "Net Banking"
                break
            else:
                print("Transaction Failed...")
                print("Please Try Again...")
        billing_db[self.BillingPicker(username)].append([billing_id, subscription_id, end_date.strftime("%d-%m-%Y"), amount, mode, last_bill_date.strftime("%d-%m-%Y")])

    def ModifyBill(self, username, subscription_id, end_date, amount, start_date):
        index = self.BillingPicker(username)
        selected = billing_db[index]
        while True:
            print("Select the Mode of Payment...")
            print("1 - Credit Card")
            print("2 - Debit Card")
            print("3 - UPI")
            print("4 - Net Banking")
            select = input("Enter The Value : ")
            if select == "1":
                mode = "Credit Card"
                break
            elif select == "2":
                mode = "Debit Card"
                break
            elif select == "3":
                mode = "UPI"
                break
            elif select == "4":
                mode = "Net Banking"
                break
            else:
                print("Transaction Failed...")
                print("Please Try Again...")
        billing_db[index][int(subscription_id)] = ([index, subscription_id, end_date.strftime("%d-%m-%Y"), amount, mode, start_date.strftime("%d-%m-%Y")])
    
    def ShowBilling(self, billing_details):
        bill_title = ['Bill No', 'Subscription ID', 'Next Due Date', 'Amount', 'Last Mode of Payment', 'Last Payment Date']
        for i in range(2, len(bill_title)):
            print(f"{bill_title[i]} : {billing_details[i]}")
        print()

class FeedBack:

    def CreateFeedback(self, username):
        feedback_db.append([username])
    
    def FeedbackPicker(self, username):
        for i in feedback_db:
            if i[0] == username:
                return feedback_db.index(i)
    
    def AddFeedback(self, username):
        feedback_id = len(billing_db[self.FeedbackPicker(username)])
        description = input("Enter Your Feedback Details : ")
        while True:
            rating = input("Enter Your Rating upto 10 : ")
            if 1 <= int(rating) <= 10:
                break
            else:
                print("Invalid Rating Score...")
        feedback_db[self.FeedbackPicker(username)].append([feedback_id, description, rating])
    
    def ShowFeedback(self, Feedback_details):
        feedback_title = ['Feedback No', 'Description', 'Rating']
        for i in range(len(feedback_title)):
            print(f"{feedback_title[i]} : {Feedback_details[i]}")
        print()

user_db = []
subscription_db = []
service_db = [['1', '10GB per Day', '100Mbps', 350], ['2', '15GB per Day', '100Mbps', 400], ['3', '30GB per Day', '100Mbps', 500], ['4', '50GB per Day', '200Mbps', 650], ['5', 'Unlimited', '300Mbps', 800]]
billing_db = []
feedback_db = []
