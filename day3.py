run = 5.2
gym = "yes"

if run >= 5:
    print("run target achieved ")
else:
    print("run target missed")

if gym == "yes":
    print("gym completed")
else:
    print("gym skipped")   

# Discipline log should not be indented

discipline_log = [
    {"day":1, "run": 5.2, "gym": "yes", "python_study": 2},
    {"day":2, "run": 5, "gym": "yes", "python_study": 2},
    {"day":3, "run": 5.03, "gym": "yes", "python_study": 2}    
    ]
for entry in discipline_log:

    print(
         f"day {entry['day']}: Run{entry['run']}km, Gym: {entry['gym']}, Python: {entry['python_study']}hrs"
         )