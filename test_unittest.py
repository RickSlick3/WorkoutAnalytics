import unittest
import os.path
import pandas as pd
from userProfile import UserProfile, read_user_profile
from analysis import Analysis

class test_UserProfile(unittest.TestCase):
    
    def setUp(self):
        print("\nRunning setUp method...")
        self.profile_1 = UserProfile("Mr Test", 7, 5, 35, 150)
        self.profile_1.addGoal("Running", "8k", "00:45:00", "2023-08-31")
        self.profile_1.addGoal("Biking", "5k", "00:28:30", "2023-08-31")
        self.profile_1.addGoal("Swimming", "1mi", "00:15:15", "2023-08-31")
           
                
    def tearDown(self):
        print("Running tearDown method...")
        del self.profile_1
    
    
    def test_UserProfile_setUp(self):
        print("Running test_UserProfile...")
        # Arrange/Act done in the test setUp
        # Assert
        self.assertEqual(self.profile_1.name, "Mr Test")
        self.assertEqual(self.profile_1.height_in, 7)
        self.assertEqual(self.profile_1.height_ft, 5)
        self.assertEqual(self.profile_1.age, 35)
        self.assertEqual(self.profile_1.weight, 150)
        self.assertEqual(len(self.profile_1.goals), 3)
       
        
    def test_editProfile(self):
        print("Running test_editProfile...")
        # Act 
        self.profile_1.editProfile("Ms Test", 6, 6, 28, 160)
        # Assert
        self.assertEqual(self.profile_1.name, "Ms Test")
        self.assertEqual(self.profile_1.height_in, 6)
        self.assertEqual(self.profile_1.height_ft, 6)
        self.assertEqual(self.profile_1.age, 28)
        self.assertEqual(self.profile_1.weight, 160)      
       
        
    def test_addGoal(self):
        print("Running test_addGoal...")
        # Arrange
        self.profile_1.goals = []
        # Assert 
        self.assertEqual(self.profile_1.goals, [])
        # Act
        self.profile_1.addGoal("Running", "8k", "00:45:00", "2023-08-31")
        self.profile_1.addGoal("Biking", "5k", "00:28:30", "2023-08-31")
        self.profile_1.addGoal("Swimming", "1mi", "00:15:15", "2023-08-31")
        # Assert
        self.assertEqual(len(self.profile_1.goals), 3)
        self.assertEqual(self.profile_1.goals[0].exercise_type, "HKWorkoutActivityTypeRunning")
        self.assertEqual(self.profile_1.goals[1].exercise_type, "HKWorkoutActivityTypeBiking")
        self.assertEqual(self.profile_1.goals[2].exercise_type, "HKWorkoutActivityTypeSwimming")
      
        
    def test_deleteGoal(self): # TODO
        print("Running test_deleteGoal...")
        # Functionality not added
        
        
    def test_csvImport(self):
        print("Running csvImport...")
        self.assertTrue(len(self.profile_1.userData.index) == 0)
        # Act
        self.profile_1.csvImport("test.csv")
        # Assert
        self.assertTrue(len(self.profile_1.userData.index) != 0)
      
        
    def test_dataFrameImport(self):
        print("Running test_dataFrameImport...")
        # # Assert
        # self.assertTrue(len(self.profile_1.userData.index) == 0)
        # # Act
        # self.profile_1.dataFrameImport("workouts.xml")
        # # Assert
        # self.assertTrue(len(self.profile_1.userData.index) != 0)
    
    
    def test_exportDf(self):
        print("Running test_exportDf...")
        # Arrange
        self.profile_1.csvImport("test.csv")
        # Act
        self.profile_1.exportDf()
        # Assert
        self.assertTrue(os.path.isfile("Mr Test.csv"))
        self.assertTrue(os.path.isfile("Mr Test.txt"))
       
        
    def test_read_user_profile(self):
        print("Running test_read_user_profile...")
        # Act
        user_profile_data, goals_list = read_user_profile("Mr Test.txt")
        # Assert
        self.assertEqual(user_profile_data['height_in'], 7)
        self.assertEqual(user_profile_data['height_ft'], 5)
        self.assertEqual(user_profile_data['age'], 35)
        self.assertEqual(user_profile_data['weight'], 150)
        self.assertTrue(len(goals_list) == 3)
      
        
    def test_existingUserImport(self):
        print("Running test_existingUserImport...")
        # Arrange 
        self.profile_1.editProfile("Ms Test", 6, 6, 28, 160)
        self.profile_1.goals = []
        # Assert
        self.assertEqual(self.profile_1.name, "Ms Test")
        self.assertEqual(self.profile_1.height_in, 6)
        self.assertEqual(self.profile_1.height_ft, 6)
        self.assertEqual(self.profile_1.age, 28)
        self.assertEqual(self.profile_1.weight, 160)
        self.assertEqual(self.profile_1.goals, [])
        self.assertTrue(len(self.profile_1.userData.index) == 0)
        # Act
        self.profile_1.existingUserImport("Mr Test")
        # Assert
        self.assertEqual(self.profile_1.name, "Mr Test")
        self.assertEqual(self.profile_1.height_in, 7)
        self.assertEqual(self.profile_1.height_ft, 5)
        self.assertEqual(self.profile_1.age, 35)
        self.assertEqual(self.profile_1.weight, 150)
        self.assertEqual(len(self.profile_1.goals), 3)
        self.assertTrue(len(self.profile_1.userData.index) != 0)
        
        
    def test_multipleUsersExports(self):
        print("Running test_multipleUsersExports...")
        # Arrange
        self.profile_1.csvImport("test.csv")
        self.profile_2 = UserProfile("Ms Test", 6, 6, 28, 160)
        self.profile_2.csvImport("test.csv")
        # Act
        self.profile_1.exportDf()
        self.profile_2.exportDf()
        # Assert
        self.assertTrue(os.path.isfile("Mr Test.csv"))
        self.assertTrue(os.path.isfile("Mr Test.txt"))
        self.assertTrue(os.path.isfile("Ms Test.csv"))
        self.assertTrue(os.path.isfile("Ms Test.txt"))
        
        
class test_Analyze(unittest.TestCase):
    
    def setUp(self):
        print("\nRunning setUp method...")      
        self.A = Analysis()
           
                
    def tearDown(self):
        print("Running tearDown method...")
        del self.A
        
        
    def test_assign_score(self):
        print("Running test_assign_score...")
        # Act/Assert
        self.assertEqual(self.A.assign_score(155, 170, 40), "3.5 4.4 4.4")
        
        
    def test_assign_ranking(self):
        print("Running test_assign_ranking...")    
        # Act/Assert
        self.assertEqual(self.A.assign_ranking(["3.5", "4.4", "4.4"]), {"Base": {3.5, "Minor benefit"}, "Threshold": {4.4, "Maintaining current fitness"}, "Vo2 max": {4.4, "Maintaining current fitness"}})
        
        
        
if __name__ == '__main__':
    unittest.main()