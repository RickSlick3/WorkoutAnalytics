import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk, Label, Frame, filedialog, PhotoImage, Canvas
from tkcalendar import Calendar, DateEntry
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from userProfile import UserProfile
from PIL import ImageTk, Image
import os 
from analysis import Analysis
# UI Screens (according to our doccumentation)
# Start Screen ( has login or new user) DONE
# Login page (has username fields and an OK button and cancle, as well as an x in the top left corner) DONE 
# New user page ( has username, name, age, weight, height as well as a cancel and ok button and an x in the corner) DONE
# Landing page, has progress as well as graph, has list of past workouts, import, export, add goal, and analyze DONE
# Add goal page (has list of goals, distanace, time, goal date, as well as cancel and add goal button) DONE
# Analysis page, has progress, list of workouts used in the analysis, suggestions to reach goal, as well as add workout, renalayze and cancel buttions) DONE

user = UserProfile("Grant", "1234", "2", "6", "60")

    
class StartScreen:
    def __init__(self):
        #setting title
        self.window = tk.Tk()
        self.window.title("Start Screen")
        #setting window size
        width=772
        height=487
        screenwidth = self.window.winfo_screenwidth()
        screenheight = self.window.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.window.geometry(alignstr)
        self.window.resizable(width=True, height=True)

        logInButton=tk.Button(self.window)
        logInButton["bg"] = "#5ffb0e"
        logInButton["cursor"] = "mouse"
        ft = tkFont.Font(family='Times',size=10)
        logInButton["font"] = ft
        logInButton["fg"] = "#000000"
        logInButton["justify"] = "center"
        logInButton["text"] = "Log in"
        logInButton.place(x=260,y=240,width=197,height=43)
        logInButton["command"] = self.logIn

        newUserButton=tk.Button(self.window)
        newUserButton["bg"] = "#5ffb0e"
        ft = tkFont.Font(family='Times',size=10)
        newUserButton["font"] = ft
        newUserButton["fg"] = "#000000"
        newUserButton["justify"] = "center"
        newUserButton["text"] = "New User"
        newUserButton.place(x=260,y=300,width=197,height=41)
        newUserButton["command"] = self.newUser

        Logo=tk.Label(self.window)
        Logo["bg"] = "#5ffb0e"
        Logo["cursor"] = "mouse"
        ft = tkFont.Font(family='Times',size=38)
        Logo["font"] = ft
        Logo["fg"] = "#333333"
        Logo["justify"] = "center"
        Logo["text"] = "Workout Analytics"
        Logo.place(x=180,y=20,width=394,height=56)

    def logIn(self):
        self.window.destroy()
        logIn = LogIN()
        logIn.run()

    def newUser(self):
        self.window.destroy()
        newUser = NewProfile()
        newUser.run()
    
    def run(self):
        # Run the Tkinter event loop
        self.window.mainloop()

class LogIN:
    def __init__(self):
        #setting title
        self.window = tk.Tk()
        self.window.title("Log In Screen")

        #setting window size
        width=767
        height=329
        screenwidth = self.window.winfo_screenwidth()
        screenheight = self.window.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.window.geometry(alignstr)
        self.window.resizable(width=False, height=False)

        Logo=tk.Label(self.window)
        Logo["bg"] = "#5ffb0e"
        Logo["cursor"] = "mouse"
        ft = tkFont.Font(family='Times',size=36)
        Logo["font"] = ft
        Logo["fg"] = "#000000"
        Logo["justify"] = "center"
        Logo["text"] = "Workout Analytics"
        Logo.place(x=210,y=20,width=380,height=49)

        self.username_value = tk.StringVar()
        self.UsernameEntry = tk.Entry(self.window, textvariable=self.username_value)
        self.UsernameEntry.place(x=360, y=160, width=70, height=25)
        

        UsernameLabel = tk.Label(self.window, text="Username:")
        UsernameLabel.place(x=290, y=160, width=70, height=25)
        
        
        CancelButton=tk.Button(self.window)
        CancelButton["bg"] = "#f0f0f0"
        CancelButton["cursor"] = "mouse"
        ft = tkFont.Font(family='Times',size=10)
        CancelButton["font"] = ft
        CancelButton["fg"] = "#000000"
        CancelButton["justify"] = "center"
        CancelButton["text"] = "Cancel"
        CancelButton.place(x=210,y=270,width=169,height=38)
        CancelButton["command"] = self.cancelButton
        
        OKButton=tk.Button(self.window)
        OKButton["bg"] = "#f0f0f0"
        OKButton["cursor"] = "mouse"
        ft = tkFont.Font(family='Times',size=10)
        OKButton["font"] = ft
        OKButton["fg"] = "#000000"
        OKButton["justify"] = "center"
        OKButton["text"] = "OK"
        OKButton.place(x=390,y=270,width=171,height=38)
        OKButton["command"] = self.loginButton

    def cancelButton(self):
        self.window.destroy()
        startScreen = StartScreen()
        startScreen.run()


    def loginButton(self):
        print("Login")
        # Check if login is valid and if they have a profile here
        username = self.username_value.get()
        if(os.path.exists(username +".csv")):
            user.existingUserImport(username)
        else:
            return
        self.window.destroy()
        mainPage = MainPage()
        mainPage.run()

    
    def run(self):
        # Run the Tkinter event loop
        self.window.mainloop()

class NewProfile:
    def __init__(self):
        self.window = tk.Tk()
        #setting title
        self.window.title("New Profile Screen")
        #setting window size
        width=767
        height=429
        screenwidth = self.window.winfo_screenwidth()
        screenheight = self.window.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.window.geometry(alignstr)
        self.window.resizable(width=False, height=False)

        Logo=tk.Label(self.window)
        Logo["bg"] = "#5ffb0e"
        Logo["cursor"] = "mouse"
        ft = tkFont.Font(family='Times',size=36)
        Logo["font"] = ft
        Logo["fg"] = "#000000"
        Logo["justify"] = "center"
        Logo["text"] = "Workout Analytics"
        Logo.place(x=210,y=20,width=380,height=49)

        
        self.username_value = tk.StringVar()
        self.UsernameEntry =tk.Entry(self.window, textvariable=self.username_value)
        self.UsernameEntry.place(x=240, y = 90, width = 70, height = 30 )
        UsernameLabel = tk.Label(self.window, text = "Username:", font = ("Times", 10))
        UsernameLabel.place(x=170, y = 90, width = 70, height = 30)

        CancelButton=tk.Button(self.window)
        CancelButton["bg"] = "#f0f0f0"
        CancelButton["cursor"] = "mouse"
        ft = tkFont.Font(family='Times',size=10)
        CancelButton["font"] = ft
        CancelButton["fg"] = "#000000"
        CancelButton["justify"] = "center"
        CancelButton["text"] = "Cancel"
        CancelButton.place(x=210,y=370,width=169,height=38)
        CancelButton["command"] = self.cancelButton

        OKButton=tk.Button(self.window)
        OKButton["bg"] = "#f0f0f0"
        OKButton["cursor"] = "mouse"
        ft = tkFont.Font(family='Times',size=10)
        OKButton["font"] = ft
        OKButton["fg"] = "#000000"
        OKButton["justify"] = "center"
        OKButton["text"] = "OK"
        OKButton.place(x=390,y=370,width=171,height=38)
        OKButton["command"] = self.loginButton

        
        self.Age_value = tk.StringVar()
        self.AgeEntry =tk.Entry(self.window, textvariable=self.Age_value)
        self.AgeEntry.place(x=240, y = 180, width = 70, height = 30 )
        AgeLabel = tk.Label(self.window, text = "Age:", font = ("Times", 10))
        AgeLabel.place(x=170, y = 180, width = 70, height = 30)
  
        self.HeightFt_value = tk.StringVar()
        self.HeightFtEntry = tk.Entry(self.window, textvariable=self.HeightFt_value)
        self.HeightFtEntry.place(x=240,y=210,width=70,height=30)
        HeightFtLabel = tk.Label(self.window, text = "Height Ft:", font = ("Times", 10))
        HeightFtLabel.place(x=170, y = 210, width = 70, height = 30)

        self.Heightin_value = tk.StringVar()
        self.HeightinEntry = tk.Entry(self.window, textvariable=self.Heightin_value)
        self.HeightinEntry.place(x=240,y=240,width=70,height=30)
        HeightinLabel = tk.Label(self.window, text = "Height In:", font = ("Times", 10))
        HeightinLabel.place(x=170, y = 240, width = 70, height = 30)

        self.Weight_value = tk.StringVar()
        self.WeightEntry = tk.Entry(self.window, textvariable=self.Weight_value)
        self.WeightEntry.place(x=240,y=270,width=70,height=30)
        WeightLabel = tk.Label(self.window, text = "Weight Lbs:", font = ("Times", 10))
        WeightLabel.place(x=170, y = 270, width = 70, height = 30)
    

    def cancelButton(self):
        self.window.destroy()
        startScreen = StartScreen()
        startScreen.run()


    def loginButton(self):
        print("Login")
        # Put the data into a user profile
        # Check if login is valid and if they have a profile here
        username = self.username_value.get()
        hft = self.HeightFt_value.get()
        hin = self.Heightin_value.get()
        weight = self.Weight_value.get()
        age = self.Age_value.get()

        if(username == '' or hft == '' or hin == '' or weight == '' or age == ''):
            return
        user.__init__(username, hin, hft, age, weight)
        self.window.destroy()
        mainPage = MainPage()
        mainPage.run()
    
    def run(self):
        self.window.mainloop()

class Analyze:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Workout Analytics")
        self.create_widgets()
        self.baseVal = None
        self.thresholdVal = None
        self.vo2Val = None
        
    def create_widgets(self):

        # Create the bar graph
        fig = plt.figure(figsize=(6, 4))
        ax = fig.add_subplot(111)
        data = [5, 5, 5]
        #data = [self.baseVal, self.thresholdVal, self.vo2Val]
        bars = ax.bar(['Base', 'Threshold', 'Vo2'], data)
        ax.set_title('Workout Metrics')
        ax.set_ylim(0, 10)  # Set the y-axis limit to fit the range of scores (0 to 10 in this case)
        colors = ['blue', 'green', 'red']
        bars = ax.bar(['Base', 'Threshold', 'Vo2'], data, color=colors)
          

        # Add labels above each bar showing the scores
        for bar, score in zip(bars, data):
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.2, str(score),
                    ha='center', va='bottom')

        canvas = FigureCanvasTkAgg(fig, master=self.window)
        canvas.get_tk_widget().pack(pady=20)



       # text_box1 = tk.Text(text_frame, yscrollcommand=text_scrollbar.set, height=10)
       #text_box1.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH, expand=True)
        workouts = (user.userData['workoutActivityType'])
        workoutDate =(user.userData['Date'])
        name = []
        i = 0
        for workout in workouts:
            if (workouts[i]=="Running" or workouts[i]=="Biking" or workouts[i]=="Swimming"):
                name.append(str(i)+" "+str(workouts[i]) +" "+str(workoutDate[i]))  
                i=i+1
            else:
                i=i+1
        var = tk.Variable(value = name)
        listbox = tk.Listbox(listvariable=var, height=6, selectmode=tk.SINGLE)
        listbox.pack(expand=True, fill=tk.BOTH, side=tk.LEFT, padx=5, pady=5)
        #val = listbox.selection_get()
        # link a scrollbar to a list
        scrollbar = ttk.Scrollbar(
            orient=tk.VERTICAL,
            command=listbox.yview
        )

        listbox['yscrollcommand'] = scrollbar.set
        

        scrollbar.pack(side=tk.LEFT, expand=True, fill=tk.Y)
                # Create the scrollable text boxes
        text_frame = tk.Frame(self.window)
        text_frame.pack(fill=tk.BOTH, expand=True, padx=50)

        text_scrollbar = ttk.Scrollbar(text_frame)
        text_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_box2 = tk.Text(text_frame, yscrollcommand=text_scrollbar.set, height=10)
        text_box2.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH, expand=True)

        text_scrollbar.config(command=tk.YView)

        # Create the buttons
        button_frame = tk.Frame(self.window)
        button_frame.pack(pady=20)
        # add_button = tk.Button(button_frame, text="Add Workout", command=self.add_workout)
        # add_button.pack(side=tk.LEFT, padx=10)
        reanalyze_button = tk.Button(button_frame, text="Reanalyze", command=lambda: 
                                     self.reanalyze(listbox.selection_get()))
        reanalyze_button.pack(side=tk.LEFT, padx=10)
        cancel_button = tk.Button(button_frame, text="Return", command=self.cancel)
        cancel_button.pack(side=tk.LEFT, padx=10)

    def add_workout(self):
        print("Add Workout button pressed")

    def reanalyze(self, var):
        # Check if an item is selected in the listbox
        if var is None:
            print("No workout selected for reanalysis.")
            return
        print("Reanalyze button pressed")
        var = str(var).split()
        index=var[0]
        info = str(user.userData.iloc[int(index)]).splitlines()
        print(info)
        hr_mean = str(info[8]).split()
        hrMax=str(info[9]).split()
        Duration = str(info[4]).split()
        print (hr_mean[1])
        analyze_instance = Analysis()
        values = analyze_instance.assign_score(float(hr_mean[1]), float(hrMax[1]), float(Duration[1]))
        val=values.split()
        print(str(analyze_instance.assign_ranking(val)))
        print (index)

        self.baseVal = val[0]
        self.thresholdVal = val[1]
        self.vo2Val = val[2]
        

    def cancel(self):
        self.window.destroy()
        analyze_app = MainPage()
        analyze_app.run()


    def run(self):      
        # Run the Tkinter event loop
        self.window.state('zoomed')
        self.window.mainloop()

class AddGoal:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Workout Analysis Tool")
        self.create_widgets()

    def create_widgets(self):
        # Create the title label
        title_label = tk.Label(self.window, text="Workout Analysis Tool", font=("Times", 16, "bold"))
        title_label.pack(pady=20)

        # Create the image
        # image = tk.PhotoImage(file="work.png").subsample(2)  # Replace "workout_image.png" with your image file path
        # image_label = tk.Label(self.window, image=image)
        # image_label.pack()

        # Create the dropdown box
        goal_label = tk.Label(self.window, text="Add Goal:")
        goal_label.pack(pady=10)

        goal_options = ["Running", "Biking", "Swimming"]
        goal_var = tk.StringVar()
        goal_dropdown = ttk.Combobox(self.window, textvariable=goal_var, values=goal_options)
        goal_dropdown.pack()

        # Create the distance fields
        dist_label = tk.Label(self.window, text="Choose Distance:")
        dist_label.pack(pady=10)

        goal_var.get() == "Running"
        dist_options = ["1mi", "5k", "8k", "10k", "Half-Marathon", "Marathon", "Ultra Marathon"]    

        distance_entry = tk.StringVar()
        dist_dropdown = ttk.Combobox(self.window, textvariable=distance_entry, values=dist_options)
        dist_dropdown.pack()
        

        time_label = tk.Label(self.window, text="Time (HH:MM:SS):")
        time_label.pack(pady=10)
        time_entry = tk.Entry(self.window)
        time_entry.pack()

        cal = DateEntry(self.window, width= 16, background= "#5ffb0e", foreground= "black",bd=2)
        cal.pack(pady=20)
        

        # Create the buttons
        button_frame = tk.Frame(self.window)
        button_frame.pack(pady=20)
        cancel_button = tk.Button(button_frame, text="Return", command=self.cancel)
        cancel_button.pack(side=tk.LEFT, padx=10)
        add_goal_button = tk.Button(button_frame, text="Add Goal",
                                    command=lambda: self.add_goal(goal_var.get(), distance_entry.get(),
                                                                  time_entry.get(), cal.get_date()))
        add_goal_button.pack(side=tk.LEFT, padx=10)

    def add_goal(self, goal, distance, time, goal_date):
        print("Goal: {}".format(goal))
        print("Distance: {}".format(distance))
        print("Time: {}".format(time))
        print("Goal Date: {}".format(goal_date))
        user.addGoal(goal, distance, time, goal_date)

    def cancel(self):
        self.window.destroy()
        analyze_app = MainPage()
        analyze_app.run()

    def run(self):
        # Run the Tkinter event loop
        self.window.state('zoomed')
        self.window.mainloop()


class MainPage:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Workout Analysis Tool")
        self.create_widgets()

    def create_widgets(self):
        # Create the title label
        title_label = tk.Label(self.window, text="Workout Analysis Tool", font=("Times", 16, "bold"))
        title_label.pack(pady=20)
        
        try:
            # Create the green highlight box
            green_box_label = tk.Label(self.window, text=f"Goal: {user.goals[0].distance} in {user.goals[0].time}", bg="green", fg="white", font=("Times", 12, "bold"))
            green_box_label.pack(pady=10, fill=tk.X)
        except:
            green_box_label = tk.Label(self.window, text="Goal:", bg="green", fg="white", font=("Times", 12, "bold"))
            green_box_label.pack(pady=10, fill=tk.X)

        try:
            image = Image.open("fnaf.png")
            new_width = 300
            new_height = 300
            image = image.resize((new_width, new_height))
            photo = ImageTk.PhotoImage(image)

            # Create a label to display the image
            image_label = tk.Label(self.window, image=photo)
            image_label.image = photo  # To prevent the image from being garbage collected
            image_label.pack(pady=20)
        except FileNotFoundError:
            print("Image not found. Make sure the file name and path are correct.")

         # Create the scrollable list titled "Past Workouts"
        past_workouts_label = tk.Label(self.window, text="Past Workouts", font=("Times", 12, "bold"))
        past_workouts_label.pack(pady=10)

        past_workouts_frame = tk.Frame(self.window)
        past_workouts_frame.pack(fill=tk.X, expand=True)

        past_workouts_scrollbar = ttk.Scrollbar(past_workouts_frame)
        past_workouts_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        past_workouts_list = tk.Listbox(past_workouts_frame, yscrollcommand=past_workouts_scrollbar.set)
        past_workouts_list.pack(fill=tk.X, expand=True)

        past_workouts_scrollbar.config(command=past_workouts_list.yview)

        # Add some example items to the scrollable list
        try:
            workouts = (user.userData['workoutActivityType'])
            workoutDate =(user.userData['Date'])
            i = 0
            j = 0
            for workout in workouts:
                # workoutTypes = ["Running", "Biking", "Swimming"]
                workoutTypes = ["TraditionalStrengthTraining", "FunctionalStrengthTraining"]
                if str(workouts[i]) not in workoutTypes:
                    past_workouts_list.insert(tk.END, "{0:6} {1:20} {2}".format(str(j), str(workouts[i]), str(workoutDate[i])))
                    j=j+1
                i=i+1
        except:
            past_workouts_list.insert(tk.END, "No workout data")

        # Create the buttons
        button_frame = tk.Frame(self.window)
        button_frame.pack(pady=20)

        import_button = tk.Button(button_frame, text="Import", command=self.import_data)
        import_button.pack(side=tk.LEFT, padx=10)

        export_button = tk.Button(button_frame, text="Export", command=self.export_data)
        export_button.pack(side=tk.LEFT, padx=10)

        add_goal_button = tk.Button(button_frame, text="Add Goal", command=self.add_goal)
        add_goal_button.pack(side=tk.LEFT, padx=10)

        analyze_button = tk.Button(button_frame, text="Analyze", command=self.analyze)
        analyze_button.pack(side=tk.LEFT, padx=10)
    
    def update_goal(self, distance, time):
        # Update the text in the green highlight box with the new goal text
        self.green_box_label.config(text=f"Goal: {distance} {time}")

    def run(self):
        self.window.state('zoomed')
        self.window.mainloop()

    
    def import_data(self):
        
        file_path = filedialog.askopenfilename(filetypes=[("XML files", "*.xml"), ("CSV files", "*.csv")])
        if file_path:
            print("Selected file:", file_path)
            
        if(file_path[-4:] == ".xml"):
            user.dataFrameImport(file_path)
        else:
            user.csvImport(file_path)
        self.window.destroy()
        app = MainPage()
        app.run()


    def export_data(self):
        user.exportDf()
        print("Export Data Here")

    def add_goal(self):
        self.window.destroy()
        addGoalApp = AddGoal()
        addGoalApp.run()

    def analyze(self):
        self.window.destroy()
        analyze_app = Analyze()
        analyze_app.run()

    def run(self):
        # Run the Tkinter event loop
        self.window.state('zoomed')
        self.window.mainloop()


startApp = StartScreen()
startApp.run()