from os import sep
import random



def maxey_bot():
    print("Hello, my name is Maxey and I am your awesome Random Workout Generator Bot. I will help to train you to your full potential! .... or to help you get a good workout in before you hit the buffet tonight. So let's do this!")
    return workout_length()


def workout_length():
    time_result = input("How long would you like to workout today? \n[A] Do I have to? (10 Minutes) \n[B]I have some time. (20 minutes) \n[C] Let's Work! (30 minutes) \n[D] Hit it! (45 minutes) \n[E] I can do this all day! (60 Minutes) \n>")
    if time_result == "A" or time_result == "a":
        return workout_10()
    elif time_result == "B" or time_result == "b":
        return workout_20()
    elif time_result == "C" or time_result == "c":
        return workout_30()
    elif time_result == "D" or time_result == "d":
        return workout_45()
    elif time_result == "E" or time_result == "e":
        return workout_60()
    else:  
        return choose_one()   


def choose_one():
    print("Sorry, I didn't get that. Please choose one of the choices. Let's try again.")
    return maxey_bot()
    
        
def workout_10():
    print("Ofcourse you do! You can fit in a simple workout in just 10 minutes. We'll be done even before you finish that boring 11 minute Youtube video.")
    
    core = random.sample(core_workouts, k=2)
    arm = random.sample(arm_workouts, k=2)
    back = random.sample(back_workouts, k=3)
    cooldowns = random.sample(cool_downs, k=3)
    
    Total_workout = []
    
    core_result = core
    arm_result = arm
    back_result = back
    cooldown_result = cooldowns
    Separator = " , "
    
    print("Here's round one. We're focusing on your rock solid core. Do 2 rounds each with 15 seconds rest in between. " + '<-- {0:^50} -->'.format(Separator.join(core_result)))
    input("Woo! Got that core working now. Hit enter to continue to Round 2. \n[Enter] \n>")
    Total_workout += core_result
    
    print("Round 2 for you. Let's get those guns working. 2 rounds each. 20 second rest in between. " + '<-- {0:^50} -->'.format(Separator.join(arm_result)))
    input("Awesome! Smoked those arms! Hit enter to continue to Round 3. \n[Enter] \n>")
    Total_workout += arm_result
    
    print("I've got your back for Round 3. Just one round of these and we're good to go. " + '<-- {0:^50} -->'.format(Separator.join(back_result)))
    input("Looking confident with that strong back! Hit enter to move on to the cool down. \n[Enter] \n>")
    Total_workout += back_result
    
    print("Take a few deep breaths and do these cool down exercises to help your rocking body recover. " + '<-- {0:^50} -->'.format(Separator.join(cooldown_result)))
    input("Feeling relaxed after that good workout? Nice. Hit Enter to end the workout. \n[Enter] \n>")
    Total_workout += cooldown_result
    
    print("Great job team. You just torched that workout in the same time it takes you to scroll your news feed. Look at the all the work you just did: " + '<-- {0:^50} -->'.format(Separator.join(Total_workout)), "Awesome work today! I'm Maxey and I'll be here the next time you want to get a great workout in. See ya!")
    
    
    
#Work out lists
warm_ups =[ "Knee Hugs: 10 reps",
    "Shoulder Circles: 10 reps",
    "Walk Outs to High Planks: 5 Reps",
    "Hurdle Steps: 10 Reps",
    "Fixed Feet Lateral Lunges: 10 Reps",
    "Quad Stretches: 10 reps",
    "Fire Hydrants: 10 reps",
    "Bird Dogs: 10 Reps",
    "Tin Soldiers: 10 Reps"
]

cool_downs = [ "Child's Pose: 10 breaths", 
    "Downward Facing Dog: 10 breaths",
    "Upward Facing Dog: 10 breaths",
    "Cat-Cows: 10 breaths",
    "World's Greatest Stretch: 5 reps each side",
    "Figure 4 Stretch: 5 breaths each leg",
    "Pigeon Pose: 10 breaths each side" 
]



core_workouts = [ "Sit-ups: 20 reps", 
    "High Plank Shouler Taps: 20 reps", 
    "Reverse Crunch: 10 reps",
    "Russian Twists: 20 reps",
    "Toe taps in low boat: 20 reps",
    "High Plank Knee drives: 20 reps",
    "Bear Crawls: 20 reps",
    "Torture Twists: 10 reps",
    "Flutter Kicks: 20 reps",
    "Bird Dogs: 20 reps"
]

chest_workouts = [ "Push-Ups: 10 reps",
    "Dumbell Bench press: 10 reps",
    "Kneeling Push-ups: 20 reps",
    "DB Floor Chest press: 20 reps", 
    "Incline Push-ups: 20 reps",
]

leg_workouts = [ "Forward Lunges: 10 reps",
    "Backward Lunges: 10 reps",
    "Bodyweight Squats: 20 reps",
    "DB Deadlifts: 20 reps",
    "Single Leg Deadlift: 10 reps",
    "Lateral Lunges: 20 reps",
    "DB Lateral Lunges: 10 reps",
    "Calf Raises: 20 reps",
    "Walking Lunges: 20 reps",
    "Hip Lift March: 20 reps"
]

arm_workouts = [ "Bicep curls: 10 reps", 
    "Hammer curls: 10 reps",
    "Bicep Curls to Overhead Press: 10 reps",
    "High Planks with Rows: 10 reps",
    "DB Cleans: 20 reps",
    "DB Push-up press: 10 reps"
]

back_workouts = [ "DB Bent-Over Rows: 10 reps",
    "DB Bent-Over Flys: 10 reps",
    "DB Shoulder Shrugs: 20 reps",
    "Supermans: 10 reps",
    "Pull-ups: 10 reps",
    "Renegade Row: 10 reps",
    "Romanian Deadlift: 10 reps",
    "Single Arm DB Row: 20 reps",
    "Deadlift: 20 reps",
    "Seated Cable Rows: 20 reps"
]

glute_workouts = [ "Glute Bridges: 20 reps",
    "Dumbell Hip Lifts: 10 reps",
    "Kettlebell Swings: 20 reps",
    "Goblet Squats: 20 reps",
    "Bodyweight Squats: 30 reps",
    "Clamshells with Bands: 20 reps"
]


maxey_bot()    
