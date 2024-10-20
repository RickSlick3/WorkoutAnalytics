import xml.etree.ElementTree as ET
from datetime import datetime

from goal import Goal
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import re


def read_user_profile(file_path):
    # Dictionary to store the user profile data
    user_profile_data = {}
    # List to store multiple goals
    goals_list = []

    # Regular expression patterns for extracting data
    profile_pattern = r"UserProfile:\s+height_in='(\d+)' height_ft='(\d+)' age='(\d+)' weight='(\d+)'"
    goal_pattern = r"Goal:\s+type='(.+)' distance='(.+)' time='(.+)' goal_date='(.+)'"

    try:
        # Read the file
        with open(file_path, 'r') as file:
            data = file.read()

            # Extract user profile data
            profile_match = re.search(profile_pattern, data)
            if profile_match:
                height_in, height_ft, age, weight = map(int, profile_match.groups())
                user_profile_data['height_in'] = height_in
                user_profile_data['height_ft'] = height_ft
                user_profile_data['age'] = age
                user_profile_data['weight'] = weight

            # Extract multiple goals
            goal_matches = re.findall(goal_pattern, data)
            for goal_match in goal_matches:
                type_, distance, time, goal_date = goal_match
                goal_data = {
                    'type': type_,
                    'distance': distance,
                    'time': time,
                    'goal_date': goal_date
                }
                goals_list.append(goal_data)

    except FileNotFoundError:
        print("File not found!")
        return None

    return user_profile_data, goals_list

class UserProfile:
    def __init__(self, name, heightIn, heightFt, age, weight): 
        self.name = name
        self.height_in = heightIn
        self.height_ft = heightFt
        self.age = age
        self.weight = weight
        self.workouts = []
        self.userData = pd.DataFrame()
        self.goals = []
        
    def editProfile(self, newName, newHeightIn, newHeightFt, newAge, newWeight):
        self.name = newName
        self.height_in = newHeightIn
        self.height_ft = newHeightFt
        self.age = newAge
        self.weight = newWeight

    def deleteGoal(self, goal):
        if goal in self.goals:
            self.goals.remove(goal)
        else:
            print("Goal not found.")

    def addGoal(self, goal_type, distance, timeGoal, completionDate):
        if goal_type == "Running":
            goal_type = "HKWorkoutActivityTypeRunning"
        elif goal_type == "Biking":
            goal_type = "HKWorkoutActivityTypeBiking"
        elif goal_type == "Swimming":
            goal_type = "HKWorkoutActivityTypeSwimming"
        else:
            print("Invalid goal_type.")
        newGoal = Goal(goal_type, distance, timeGoal, completionDate)
        self.goals.append(newGoal)
        


    def csvImport(self, fileName):
        self.userData = pd.read_csv(fileName)

    def existingUserImport(self, userName):
        print("Working")
        existingUser, goals = read_user_profile(userName+'.txt')
        self.userData = pd.read_csv(userName+'.csv')

        self.height_in =existingUser["height_in"]
        self.height_ft =existingUser["height_ft"]
        self.age =existingUser["age"]
        self.weight =existingUser["weight"]
        self.name = userName
        
        if goals:
            print("\nGoals:")
            for index, goal in enumerate(goals, start=1):
                newGoal = Goal(goal['type'], goal['distance'], goal['time'], goal['goal_date'])
                self.goals.append(newGoal)

        if existingUser:
            print("User Profile Data:")
            for key, value in existingUser.items():
                print(f"{key}: {value}")

        if goals:
            print("\nGoals:")
            for index, goal in enumerate(goals, start=1):
                print(f"Goal {index}:")
                for key, value in goal.items():
                    print(f"{key}: {value}")
                print()  # Blank line between goals
        
    def dataFrameImport(self, filename):
        plt.style.use("fivethirtyeight")

        # create element tree object
        tree = ET.parse(filename) 
        # for every health record, extract the attributes
        root = tree.getroot()
        record_list = [x.attrib for x in root.iter('Record')]

        record_data = pd.DataFrame(record_list)

        # proper type to dates
        for col in ['creationDate', 'startDate', 'endDate']:
            record_data[col] = pd.to_datetime(record_data[col])

        # value is numeric, NaN if fails
        record_data['value'] = pd.to_numeric(record_data['value'], errors='coerce')

        # some records do not measure anything, just count occurences
        # filling with 1.0 (= one time) makes it easier to aggregate
        record_data['value'] = record_data['value'].fillna(1.0)

        # shorter observation names
        record_data['type'] = record_data['type'].str.replace('HKQuantityTypeIdentifier', '')
        record_data['type'] = record_data['type'].str.replace('HKCategoryTypeIdentifier', '')
        # dictionary of DataFrames for filtered 'record_data'
        record_data_df_dict = {}
        # filter 'type' of 'record_data'
        record_types = [
        'BodyMass',
        'ActiveEnergyBurned',
        'BasalEnergyBurned',
        'DistanceWalkingRunning',
        'StepCount',
        'AppleStandTime',
        'WalkingSpeed',
        'RunningSpeed',
        'HeartRateVariabilitySDNN',
        'RestingHeartRate',
        'WalkingHeartRateAverage',
        'VO2Max',
        'HeartRateRecoveryOneMinute'
        ]
        # create new DataFrame for every interested data
        for record_type in record_types:
            record_data_df_dict[record_type] = record_data.loc[(record_data['type'].str.contains(record_type))].rename(columns={"value":record_type}).sort_values(by='startDate')

        final_workout_dict = []
        workout_list = list(root.iter('Workout'))
        for i in range(len(workout_list)):
            workout_dict = workout_list[i].attrib
            WorkoutStatisticsList = list(workout_list[i].iter("WorkoutStatistics"))
            for i, WorkoutStatistics in enumerate(WorkoutStatisticsList):
                if "ActiveEnergyBurned" in WorkoutStatistics.attrib['type']:
                    workout_dict['activeEnergyBurned'] = WorkoutStatistics.attrib['sum']
                if "BasalEnergyBurned" in WorkoutStatistics.attrib['type']:
                    workout_dict['basalEnergyBurned'] = WorkoutStatistics.attrib['sum']
            final_workout_dict.append(workout_dict)
        final_workout_df = pd.DataFrame(final_workout_dict) #create final_workout_df dataframe

        workout_list = [x.attrib for x in root.iter('Workout')]

        # create DataFrame
        workout_data = pd.DataFrame(workout_list)
        workout_data['workoutActivityType'] = workout_data['workoutActivityType'].str.replace('HKWorkoutActivityType', '')
        
        # workoutTypes = ["Running", "Biking", "Swimming"]
        # workout_data = workout_data[str(workout_data['workoutActivityType']) in workoutTypes]
        
        workout_data = workout_data.rename({"workoutActivityType": "Type"}, axis=1)

        # proper type to dates
        for col in ['creationDate', 'startDate', 'endDate']:
            workout_data[col] = pd.to_datetime(workout_data[col])
        # convert string to numeric   
        workout_data['duration'] = pd.to_numeric(workout_data['duration'])

        def get_heartrate_for_workout(heartrate, workout):
            def get_heartrate_for_date(hr, start, end):
                hr = hr[hr["startDate"] >= start]
                hr = hr[hr["endDate"] <= end]
                return hr
            return get_heartrate_for_date(heartrate, workout["startDate"].item(), workout["endDate"].item())

        heartrate_data = record_data[record_data["type"] == "HeartRate"]

        # Extract heartrate statistics for certain workout
        last_workout = workout_data.iloc[[-1]]
        heartrate_workout = get_heartrate_for_workout(heartrate_data, last_workout)
        minh = heartrate_workout["value"].min()
        maxh = heartrate_workout["value"].max()
        meanh = heartrate_workout["value"].mean()

        def get_hr_for_workout_row(workout, heartrate):
            def get_hr_for_date(hr, start, end):
                hr = hr[hr["startDate"] >= start]
                hr = hr[hr["endDate"] <= end]
                return hr
            return get_hr_for_date(heartrate, workout["startDate"], workout["endDate"])

        workout_data["heartrate"] = workout_data.apply(lambda row: get_hr_for_workout_row(row, heartrate_data), axis=1)
        workout_data["hr_mean"] = workout_data.apply(lambda row: row['heartrate']["value"].mean(), axis=1)
        workout_data["hr_peak"] = workout_data.apply(lambda row: row['heartrate']["value"].max(), axis=1)

        #drop 'creationDate' and 'endDate' column
        final_workout_df_cleaned = final_workout_df.drop(['sourceName','sourceVersion', 'device', 'creationDate','endDate'], axis=1)
        # transform creationDate into date format 
        final_workout_df_cleaned['Date'] = pd.to_datetime(final_workout_df['startDate']).dt.strftime('%Y-%m-%d')
        final_workout_df_cleaned['Day'] = pd.to_datetime(final_workout_df['startDate']).dt.strftime('%A')
        # rename Activity Type
        final_workout_df_cleaned['workoutActivityType'] = final_workout_df['workoutActivityType'].str.replace('HKWorkoutActivityType','')
        # reorder column
        final_workout_df_cleaned = final_workout_df_cleaned[['Day', 'Date', 'workoutActivityType', 'duration', 'durationUnit', 'activeEnergyBurned', 'basalEnergyBurned']]
        # transform data type of 'duration' from object into float
        final_workout_df_cleaned['duration'] = final_workout_df['duration'].astype(float)
        # transform data type of 'activeEnergyBurned' and 'basalEnergyBurned' from object into float
        final_workout_df_cleaned['activeEnergyBurned'] = final_workout_df['activeEnergyBurned'].astype(float)
        final_workout_df_cleaned['basalEnergyBurned'] = final_workout_df['basalEnergyBurned'].astype(float)
        final_workout_df_cleaned["hr_mean"] = workout_data["hr_mean"].astype(float)
        final_workout_df_cleaned["hr_peak"] = workout_data["hr_peak"].astype(float)

        self.userData = final_workout_df_cleaned

    def exportDf(self):
        with open(f"{self.name}.txt", "w") as file:
            # Write the UserProfile data
            file.write(f"UserProfile: height_in='{self.height_in}' height_ft='{self.height_ft}' age='{self.age}' weight='{self.weight}'\n")

            # Write the Goals data
            for goal in self.goals:
                file.write(f"Goal: type='{goal.exercise_type}' distance='{goal.distance}' time='{goal.time}' goal_date='{goal.date}'\n")
        
        self.userData.to_csv(f"{self.name}.csv")
