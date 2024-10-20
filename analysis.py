import pandas as pd
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET
import datetime as dt
plt.style.use("fivethirtyeight")

from goal import Goal
from userProfile import UserProfile 

class Analysis():


    def assign_score(user, HRAvg, HRMax, TotalDuration):
        HRAvg = float(HRAvg)#user.userData["hr_mean"]
        HRMax = float(HRMax)#user.userData["hr_peak"]
        TotalDuration = float(TotalDuration)#user.userData["duration"]
        #Assigning Vo2 scores for each variable
        HRAvg_Vo2 = (
            10 if HRAvg >= 180 else
            9 if HRAvg >= 175 else
            8 if HRAvg >= 170 else
            7 if HRAvg >= 165 else
            6 if HRAvg >= 160 else
            5 if HRAvg >= 155 else
            4 if HRAvg >= 150 else
            3 if HRAvg >= 145 else
            2 if HRAvg >= 130 else
            1 if HRAvg >= 120 else
            0
        )
        HRMax_Vo2 = (
            10 if HRMax >= 200 else
            9 if HRMax >= 195 else
            8 if HRMax >= 190 else
            7 if HRMax >= 185 else
            6 if HRMax >= 183 else
            5 if HRMax >= 180 else
            4 if HRMax >= 170 else
            3 if HRMax >= 163 else
            2 if HRMax >= 160 else
            1 if HRMax >= 155 else
            0
        )

        # Calculate the average Vo2 score
        Vo2Avg = (HRAvg_Vo2*2 + (HRMax_Vo2 * 3)) / 5
        print("Vo2Av = "+str(Vo2Avg))
        # Assigning Threshold scores for each variable
        HRAvg_Threshold = (
            10 if HRAvg >= 170 else
            9 if HRAvg >= 167 else
            8 if HRAvg >= 165 else
            7 if HRAvg >= 163 else
            6 if HRAvg >= 160 else
            5 if HRAvg >= 157 else
            4 if HRAvg >= 155 else
            3 if HRAvg >= 150 else
            2 if HRAvg >= 145 else
            1 if HRAvg >= 140 else
            0
        )
        HRMax_Threshold = (
            10 if HRMax >= 190 else
            9 if HRMax >= 185 else
            8 if HRMax >= 183 else
            7 if HRMax >= 180 else
            6 if HRMax >= 175 else
            5 if HRMax >= 173 else
            4 if HRMax >= 170 else
            3 if HRMax >= 163 else
            2 if HRMax >= 160 else
            1 if HRMax >= 155 else
            0
        )
        TotalDuration_Threshold = (
            10 if TotalDuration >= 60 else
            9 if TotalDuration >= 55 else
            8 if TotalDuration >= 50 else
            7 if TotalDuration >= 45 else
            6 if TotalDuration >= 40 else
            5 if TotalDuration >= 37 else
            4 if TotalDuration >= 35 else
            3 if TotalDuration >= 30 else
            2 if TotalDuration >= 25 else
            1 if TotalDuration >= 20 else
            0
        )
        # Calculate the average Threshold score
        ThresholdAvg = (HRAvg_Threshold*2 + HRMax_Threshold*2 + TotalDuration_Threshold)/ 5

        # Assigning Base scores for each variable
        HRAvg_Base = (
            10 if HRAvg <= 125 else
            9 if HRAvg <= 135 else
            8 if HRAvg <= 140 else
            7 if HRAvg <= 145 else
            6 if HRAvg <= 150 else
            5 if HRAvg <= 155 else
            4 if HRAvg <= 160 else
            3 if HRAvg <= 165 else
            2 if HRAvg <= 170 else
            1 if HRAvg <= 175 else
            0
        )
        HRMax_Base = (
            10 if HRMax <= 145 else
            9 if HRMax <= 150 else
            8 if HRMax <= 155 else
            7 if HRMax <= 157 else
            6 if HRMax <= 160 else
            5 if HRMax <= 163 else
            4 if HRMax <= 165 else
            3 if HRMax <= 167 else
            2 if HRMax <= 170 else
            1 if HRMax <= 175 else
            0
        )
        TotalDuration_Base = (
            10 if TotalDuration >= 200 else
            9 if TotalDuration >= 150 else
            8 if TotalDuration >= 100 else
            7 if TotalDuration >= 80 else
            6 if TotalDuration >= 60 else
            5 if TotalDuration >= 50 else
            4 if TotalDuration >= 40 else
            3 if TotalDuration >= 35 else
            2 if TotalDuration >= 30 else
            1 if TotalDuration >= 20 else
            0
        )
        # Calculate the average Base score
        BaseAvg = (HRAvg_Base + HRMax_Base*2 + TotalDuration_Base*3) / 6
        return str(BaseAvg)+" "+str(ThresholdAvg)+" "+str(Vo2Avg)
        #return BaseAvg, ThresholdAvg, Vo2Avg
        

    def assign_ranking(user, Val):
        base_value = float(Val[0])
        threshold_value = float(Val[1])
        vo2_value = float(Val[2])
        def get_phrase(value):
            if value <= 2:
                return "No benefit"
            elif value <= 4:
                    return "Minor benefit"
            elif value <= 6:
                return "Maintaining current fitness"
            elif value <= 8:
                return "Impacting fitness"
            else:
                return "Highly impacting fitness"
    #Defines the 3 cateogries we are going to track and measure
        base_phrase = get_phrase(base_value)
        threshold_phrase = get_phrase(threshold_value)
        vo2_phrase = get_phrase(vo2_value)

        return {
            "Base": {base_value, base_phrase},
            "Threshold": {threshold_value,threshold_phrase},
            "Vo2 max": {vo2_value,vo2_phrase}
    }


    def SuggestWorkout():
        print("Workout")