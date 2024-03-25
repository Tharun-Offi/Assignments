import getpass
from modal import User, Activity, Goal, Friends, Leaderboard

if __name__ == '__main__':
    user = User()
    activity = Activity()
    goal = Goal()
    friends = Friends()
    leader = Leaderboard()

    while True:
        print()
        print("----------------------------------------Fitness App--------------------------------------")
        print()
        print("1 - Create Account")
        print("2 - Login")
        print("0 - Exit")
        print()
        option = input("Enter your Selection : ")
        if option == '1':
            user.CreateUser()

        elif option == '2':
            username = input("Enter Your Username : ")

            if user.CheckUsername(username):
                user_profile = user.SetProfile(username)
                activity_profile = activity.SetActivityProfile(username)
                flag = True

                while True:
                    password = getpass.getpass("Enter your Pasword (0 to Exit) : ")

                    if user_profile[1] == password or password == '0':
                        if password == '0':
                            flag = False
                        break

                    else:
                        print()
                        print("Incorrext Password...")

                while flag:
                    print()
                    print(f"----------------------------------------Welcome back Mr.{username}----------------------------------------")
                    print()
                    print("1 - Show Profile")
                    print("2 - Manage Activity")
                    print("3 - Goal Achived")
                    print("4 - Manage Friends")
                    print("5 - Leaderboard")
                    print("0 - Logout")
                    print()
                    choice = input("Enter your Selection : ")

                    if choice == '1':
                        user.ShowProfile(user_profile)
                        actionsss = getpass.getpass("Press Enter to Continue...")

                    elif choice == '2':
                        while True:
                            print(f"----------------------------------------Mr.{username}'s Activity Room----------------------------------------")
                            print()
                            print("1 - Show Current Activities")
                            print("2 - Add New Activity")
                            print("3 - Update Current Activity")
                            print("4 - Remove Activity")
                            print("0 - Return to Main Menu")
                            print()
                            activity_choice = input("Enter Your Selection : ")
                            if activity_choice == '1':
                                activity.ShowActivityProfile(username)
                                actionsss = getpass.getpass("Press Enter to Continue...")
                            elif activity_choice == '2':
                                activity.AddActivity(username)
                                actionsss = getpass.getpass("Press Enter to Continue...")
                            elif activity_choice == '3':
                                activity.UpdateActivity(username)
                            elif activity_choice == '4':
                                activity.RemoveActivity(username)
                            elif activity_choice == '0':
                                break
                            else:
                                print("Invalid Selection...")
                    
                    elif choice == '3':
                        goal.AchievedGoal(username)
                        actionsss = getpass.getpass("Press Enter to Continue...")
                    
                    elif choice == '4':
                        while True:
                            print()
                            print("1 - Add Friends")
                            print("2 - Show Friends")
                            print("3 - Friend Request")
                            print("0 - Exit")
                            print()
                            friends_option = input("Enter Your Selection : ")
                            if friends_option == '1':
                                user.ShowUsers(username)
                                reciever = input("Enter The Username To Send Request : ")
                                friends.send_friend_request(username, reciever)
                                actionsss = getpass.getpass("Press Enter to Continue...")

                            elif friends_option == '2':
                                friends.display_friends_list(username)
                                actionsss = getpass.getpass("Press Enter to Continue...")

                            elif friends_option == '3':
                                friends.display_friend_requests(username)

                            elif friends_option == '0':
                                break

                            else:
                                print("Invalid Input...")
                    
                    elif choice == '5':
                        print()
                        leader.display_leaderboard()
                        actionsss = getpass.getpass("Press Enter to Continue...")

                    elif choice =='0':
                        break

                    else:
                        print("Invalid Selection")

            else:
                print("No User Found")

        elif option == '0':
            print()
            print("Thank You")
            break

        else:
            print()
            print("Invalid Option")