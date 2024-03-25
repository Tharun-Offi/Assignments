from datetime import date
from modal import User, Subscription, Billing, FeedBack
from modal import user_db, subscription_db, service_db, billing_db, feedback_db

if __name__ == "__main__":
    bill = Billing()
    feed = FeedBack()
    print()
    print("--------------------------------------Welcome to Broadband Service App--------------------------------------")
    while True:
        print()
        print("1 - Create New User")
        print("2 - Login")
        print("3 - Exit")
        print()
        first_choice = input("Enter Your Option : ")
        if first_choice == '1':
            user = User()
            user.CreateUser()
        elif first_choice == '2':
            username = input("Username : ")
            if user.CheckUser(username):
                user_info = user.UserInfo(username)
                while True:
                    password = input("Password : ")
                    if user_info[1] == password:
                        while True:
                            print()
                            print("1 - Show Profile")
                            print("2 - Update Profile")
                            print("3 - Subscription")
                            print("4 - Feedback")
                            print("5 - Return to Login Page")
                            print("")
                            print()
                            option = input("Enter your Selection : ")
                            print()
                            if option == '1':
                                print()
                                user.ShowInfo(user_info)
                                print()
                            elif option == '2':
                                print()
                                user.UpdateUser(user_info)
                                user_info = user.UserInfo(username)
                            elif option == '3':
                                subscription = Subscription()
                                while True:
                                    print()
                                    print("1 - User Subscription Details")
                                    print("2 - Plans to Subscribe")
                                    if subscription.CheckActiveSubscription(username):
                                        print("3 - Upgrade / Downgrade Subscription")
                                        print("4 - Cancel Subscription")
                                    print("5 - Return to Main Menu")
                                    print()
                                    subscription_option = input("Enter Your Option : ")
                                    print()
                                    if subscription_option == '1':
                                        if len(subscription_db[subscription.SubscriptionPicker(username)]) == 1:
                                            print("Plans Not Yet Subscribed")
                                        else:
                                            subscription_info = subscription_db[subscription.SubscriptionPicker(username)]
                                            billing_details = billing_db[bill.BillingPicker(username=username)]
                                            print()
                                            print(f"Username : {username}")
                                            print()
                                            for i in range(1, len(subscription_info)):
                                                subscription.SubscriptionInfo(int(subscription_info[i][0])-1, subscription_info[i])
                                                bill.ShowBilling(billing_details[i])
                                    elif subscription_option == '2':
                                        subscription.AddSubscription(username)
                                    elif subscription_option == '3' and subscription.CheckActiveSubscription(username):
                                        subscription_info = subscription_db[subscription.SubscriptionPicker(username)]
                                        while True:
                                            for i in range(1, len(subscription_info)):
                                                print(f"Plan Number = {i}")
                                                subscription.SubscriptionInfo(int(subscription_info[i][0])-1, subscription_info[i])
                                            modification = input("Select Your Subscribed Plan Number to Upgrade or Downgrade : ")
                                            if int(modification) <= len(subscription_info):
                                                break
                                            else:
                                                print("Invalid Plan Number...")
                                                print("Please Enter Valid One...")
                                        subscription.ModifySubscription(modification, username)
                                    elif subscription_option == '4' and subscription.CheckActiveSubscription(username):
                                        subscription_info = subscription_db[subscription.SubscriptionPicker(username)]
                                        while True:
                                            for i in range(1, len(subscription_info)):
                                                print(f"Plan Number = {i}")
                                                subscription.SubscriptionInfo(int(subscription_info[i][0])-1, subscription_info[i])
                                            cancellation = input("Select Your Subscribed Plan Number to Cancel : ")
                                            if int(cancellation) <= len(subscription_info):
                                                break
                                            else:
                                                print("Invalid Plan Number...")
                                                print("Please Enter Valid One...")
                                        subscription.CancelSubscription(cancellation, username)
                                    elif subscription_option == '5':
                                        break
                                    else:
                                        print("Invalid Input")
                            elif option == '4':
                                while True:
                                    print()
                                    print("1 - Add a New Feedback")
                                    print("2 - Show My Feedback")
                                    print("3 - Back to Main Menu")
                                    print()
                                    feedback_option = input("Enter Your Option : ")
                                    if feedback_option == '1':
                                        feed.AddFeedback(username)
                                    elif feedback_option == '2':
                                        feedback_info = feedback_db[feed.FeedbackPicker(username)]
                                        print(f"Username : {username}")
                                        print()
                                        for i in range(1, len(feedback_info)):
                                                feed.ShowFeedback(feedback_info[i])
                                    elif feedback_option == '3':
                                        break
                                    else:
                                        print("Invalid Option...")
                            elif option == '5':
                                break
                            else:
                                print("Invalid Option")
                        break
                    else:
                        print("Invalid Password")
            else:
                print("User not Found...")
        elif first_choice == '3':
            print()
            print("Thank You...")
            print()
            break
        else:
            print()
            print("Invalid Input")
