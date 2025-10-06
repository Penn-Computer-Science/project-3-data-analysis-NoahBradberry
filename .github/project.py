import pandas as pd
import random 
classes = ["Math", "Science", "History", "English"]
grades = ["Freshmen", "Sophomore", "Junior", "Senior"]
survey_classes = ["Math", "Math", "Math", "Science", "History", "English", "Math", "Math"]
survey_grades = ["Junior", "Sophomore", "Junior", "Junior", "Senior", "Junior", "Junior", "Sophomore"]
survey_studyhours = [3, 4, 2, 3, 2, 5, 1, 3]
survey_sleep = [7, 8, 7, 7, 8, 7, 7, 5]
survey_gpa = [3.6, 4.0, 4.1, 3.8, 2.47, 4.2, 3.8, 4.1389]

for i in range(22):
    survey_classes.append(random.choice(classes))
    survey_grades.append(random.choice(grades))
    survey_studyhours.append(random.randint(1, 5))
    survey_sleep.append(random.randint(5, 8))
    survey_gpa.append(round(random.uniform(2.5, 4.3),2))

data = pd.DataFrame(
    {
        "Favorite Class" : survey_classes,
        "Grade" : survey_grades,
        "Hours Studying" : survey_studyhours,
        "Hours Sleeping" : survey_sleep,
        "GPA" : survey_gpa
    }
)

print(data)
print(round(data.describe()))
