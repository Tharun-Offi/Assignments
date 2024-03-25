import getpass
from datetime import datetime, date, timedelta

username_db, user_db, activity_db, plan_db, goal_db = [], [], [], [], []
activities = ['Walking', 'Jogging', 'Running', 'Swimming', 'Cycling']
users, user_scores = {}, {}


class User:

    def __init__(self):
        pass

    def CreateUser(self):
        print()
        while True:
            username = input("Enter Your Username : ")
            if not self.CheckUsername(username):
                break
            else:
                print()
                print("Username already Taken...")

        while True:
            password = input("Enter Your Password : ")
            if password != "":
                cpassword = input("Confirm Your Password : ")
                if password == cpassword:
                    break
                else:
                    print("Both the Password column should be same...")
            else:
                print("Password Should not be Empty...")
        
        dob = input("Enter your Date of Birth (DD-MM-YYYY) : ")
        dob_date = datetime.strptime(dob, "%d-%m-%Y")
        current_date = datetime.now()
        age = current_date.year - dob_date.year - ((current_date.month, current_date.day) < (dob_date.month, dob_date.day))
        height = input("Enter your Height (in CM) : ") + ' cm'
        weight = input("Enter your Weight (in KG) : ") + ' kg'
        user_db.append([username, password, age, height, weight])
        username_db.append(username)
        activity_db.append([username, []])
        plan_db.append([username, []])
        goal_db.append([username, []])
        friends = Friends()
        friends.create_user(username)

    
    def SetProfile(self, username):
        for i in user_db:
            if i[0] == username:
                return i
    
    def ShowProfile(self, arr):
        profile_title = ['Username : ', 'Password : ', 'Age : ', 'Height : ', 'Weight : ']
        print()
        for i in range(len(profile_title)):
            if profile_title[i] != 'Password : ':
                print(f"{profile_title[i]}{arr[i]}")

    def ShowUsers(self, username):
        count = 1
        print("No. - Username")
        for i in range(len(username_db)):
            if username_db[i] != username:
                print(f"{count}   - {username_db[i]}")
                count+=1
    
    def CheckUsername(self, username):
        for i in user_db:
            if i[0] == username:
                return True
        return False

class Workout:
    def __init__(self):
        pass

    def CreateWorkout(self, workout_id, username, activity_index):
        activity_type = activities[workout_id]
        if self.CheckWorkout(activity_type, username):
            while True:
                number_of_days = input("Enter the Number of days work in this activity : ")
                if number_of_days.isdigit():
                    break

                else:
                    print("Invalid number of Days...")

            while True:
                goal = input("Enter the distance to be covered (in M) : ")
                if goal.isdigit():
                    break

                else:
                    print("Invalid Distance...")
            start_date = datetime.today()
            end_date = start_date + timedelta(days=int(number_of_days))
            activity_db[activity_index][1].append([activity_type, number_of_days, goal, start_date.strftime("%d-%m-%Y"), end_date.strftime("%d-%m-%Y")])
        
        else:
            print("This Activity is Already Active...")

    def CheckWorkout(self, activity_type, username):
        activity = Activity()
        activity_array = activity_db[activity.SetActivityProfile(username)][1]
        for i in range(len(activity_array)):
            if activity_type == activity_array[i][0]:
                return False
        return True
    
    def SelectWorkout(self, activity_type, username):
        activity = Activity()
        activity_array = activity_db[activity.SetActivityProfile(username)][1]
        for i in range(len(activity_array)):
            if activity_type == activity_array[i][0]:
                return i

class Activity:
    def __init__(self):
        pass

    def AddActivity(self, username):
        while True:
            print()
            print("1 - Walking")
            print("2 - Jogging")
            print("3 - Running")
            print("4 - Cycling")
            print("5 - Swimming")
            print()
            choice = input("Enter Your Activity Selection : ")
            if 1 <= int(choice) <= 5:
                break
            else:
                print("Invalid Activity Selection...")
        index = int(choice)
        activity_index = self.SetActivityProfile(username)
        workout = Workout()
        workout.CreateWorkout(index-1, username, activity_index)

    def ShowActivityProfile(self,username):
        activity_title = ['Activity : ', 'Duration (in Days): ', 'Daily Distance : ', 'Started on ', "Will Ends on "]
        index = self.SetActivityProfile(username)
        if len(activity_db[index][1]) > 0:
            for i in range(1, len(activity_db[index])):
                for j in activity_db[index][i]:
                    for k in range(len(activity_title)):
                        print(f"{activity_title[k]}{j[k]}")
                    print()
        else:
            print("No Such Activities are Currently Active...")
    
    def UpdateActivity(self, username):
        while True:
            print()
            print("1 - Walking")
            print("2 - Jogging")
            print("3 - Running")
            print("4 - Cycling")
            print("5 - Swimming")
            print()
            choice = input("Enter Your Activity Selection : ")
            if 1 <= int(choice) <= 5:
                break
            else:
                print("Invalid Activity Selection...")
        
        index = int(choice) - 1
        workout = Workout()
        activity_type = activities[index]
        if not workout.CheckWorkout(activity_type, username):
            activity_index = workout.SelectWorkout(activity_type, username)
            print()
            print("1 - Duration")
            print("2 - Distance")
            print()
            selection = input("Enter your Option to Update : ")
            if selection == '1' :
                while True:
                    number_of_days = input("Enter the Number of days from Today : ")
                    if number_of_days.isdigit():
                        break

                    else:
                        print("Invalid number of Days...")
                start_date = datetime.today()
                end_date = start_date + timedelta(days=int(number_of_days))
                activity_db[self.SetActivityProfile(username)][1][activity_index][1] = number_of_days
                activity_db[self.SetActivityProfile(username)][1][activity_index][3] = start_date.strftime("%d-%m-%Y")
                activity_db[self.SetActivityProfile(username)][1][activity_index][4] = end_date.strftime("%d-%m-%Y")


            elif selection == '2':
                while True:
                    goal = input("Enter the new distance to be covered (in M) : ")
                    if goal.isdigit():
                        break

                    else:
                        print("Invalid Distance...")
                
                activity_db[self.SetActivityProfile(username)][1][activity_index][2] = goal
            
            else:
                print("Invalid Option...")
                pass

        else:
            print("The selected Activity is not Currently Active...")

    def RemoveActivity(self, username):
        while True:
            print()
            print("1 - Walking")
            print("2 - Jogging")
            print("3 - Running")
            print("4 - Cycling")
            print("5 - Swimming")
            print()
            choice = input("Enter Your Activity Selection : ")
            if 1 <= int(choice) <= 5:
                break
            else:
                print("Invalid Activity Selection...")
        
        index = int(choice) - 1
        workout = Workout()
        activity_type = activities[index]
        if not workout.CheckWorkout(activity_type, username):
            activity_index = workout.SelectWorkout(activity_type, username)
            activity_db[self.SetActivityProfile(username)][1].pop(activity_index)

        else:
            print("No Such Activity Found...")


    def SetActivityProfile(self, username):
         for i in range(len(activity_db)):
            if activity_db[i][0] == username:
                return i

class Goal:
    def __init__(self):
        pass

    def AchievedGoal(self, username):
        activity = Activity()
        workout = Workout()
        leader = Leaderboard()
        index = activity.SetActivityProfile(username)
        activity_profile = activity_db[index]
        for i in range(len(activity_profile[1])):
            if activity_profile[1][i][4] == (date.today()).strftime("%d-%m-%Y") : 
                activity_profile[1][i].append(round((int(activity_profile[1][i][2])/1400)*5*(int(activity_profile[1][i][1])+1),2))
                goal_db[index][1].append(activity_profile[1][i])
                leader.add_user_score(username, round(activity_profile[1][i][5],2))
                activity_db[activity.SetActivityProfile(username)][1].pop(i)

        self.ShowAchievedGoal(username, index)
    
    def ShowAchievedGoal(self, username, index):
        goals_title = ['Activity', 'Duration in Days', 'Daily Distance in M', 'Started', 'Ended', 'Burned Calories']
        goals = goal_db[index][1]
        for i in range(len(goals)):
            print(f"\nCompleted Activity : {i+1}\n")
            for j in range(len(goals_title)):
                print(f"{goals_title[j]} : {goals[i][j]}")
        print()

class Friends:
    def __init__(self):
        pass

    def create_user(self, username):
        if username not in users:
            users[username] = {"friend_requests_sent": {}, "friend_requests_received": {}, "friends_list": []}
            print(f"User '{username}' created successfully.")
        else:
            print(f"User '{username}' already exists.")

    def send_friend_request(self, sender, receiver):
        if receiver not in users:
            print(f"User '{receiver}' does not exist.")
            return
        if receiver not in users[sender]["friend_requests_sent"] and receiver not in users[sender]["friends_list"]:
            users[sender]["friend_requests_sent"][receiver] = "pending"
            users[receiver]["friend_requests_received"][sender] = "pending"
            print(f"Friend request sent to '{receiver}' by '{sender}'.")
        elif receiver in users[sender]["friends_list"]:
            print(f"'{receiver}' is already your friend.")
        else:
            print(f"A friend request to '{receiver}' is already pending.")

    def accept_friend_request(self, receiver, sender):
        if sender not in users:
            print(f"User '{sender}' does not exist.")
            return
        if sender in users[receiver]["friend_requests_received"]:
            users[receiver]["friends_list"].append(sender)
            users[sender]["friends_list"].append(receiver)
            del users[receiver]["friend_requests_received"][sender]
            del users[sender]["friend_requests_sent"][receiver]
            print(f"Friend request accepted from '{sender}'.")
        else:
            print(f"No pending friend request from '{sender}'.")

    def display_friend_requests(self, username):
        if username in users:
            print()
            print("1 - Send Requests")
            print("2 - Received Requests")
            print()
            choice = input("Enter Your Selection : ")
            if choice == '1':
                if users[username]["friend_requests_sent"]:
                    print(f"Friend requests sent by user '{username}':")
                    for receiver, status in users[username]["friend_requests_sent"].items():
                        print(f"To '{receiver}': {status}")
                else:
                    print(f"No pending friend requests sent by user '{username}'.")
            elif choice == '2':
                if users[username]["friend_requests_received"]:
                    print(f"Friend requests received by user '{username}':")
                    for sender, status in users[username]["friend_requests_received"].items():
                        print(f"From '{sender}': {status}")
                    while True:
                        print()
                        print("1 - Accept Request")
                        print("0 - Exit")
                        print()
                        request = input("Enter Your Selection : ")
                        if request == '1':
                            receiver = input("Enter The Requested Username To Accept it : ")
                            self.accept_friend_request(username, receiver)
                            actionsss = getpass.getpass("Press Enter to Continue...")

                        elif request == '0':
                            break

                        else:
                            print("Invalid Selection...")
                else:
                    print(f"No pending friend requests received by user '{username}'.")
        else:
            print(f"User '{username}' does not exist.")

    def display_friends_list(self, username):
        if username in users:
            if users[username]["friends_list"]:
                print(f"Friends list for user '{username}':\n")
                for friend in users[username]["friends_list"]:
                    print(friend)
            else:
                print(f"No friends yet for user '{username}'.")
        else:
            print(f"User '{username}' does not exist.")

class Leaderboard:
    def __init__(self):
        pass

    def add_user_score(self, username, calories_burned):
        if username in user_scores:
            user_scores[username] += calories_burned
        else:
            user_scores[username] = calories_burned

    def display_leaderboard(self):
        sorted_scores = sorted(user_scores.items(), key=lambda x: x[1], reverse=True)
        if sorted_scores:
            print("Leaderboard:")
            rank = 1
            for username, score in sorted_scores:
                print(f"{rank}. {username}: {score} calories burned")
                rank += 1
        else:
            print("No users on the leaderboard yet.")
