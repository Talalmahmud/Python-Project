student_data = {"student": ["Talal", "Movin", "Nayem"],
                "score":[50, 60, 64]}

student_dataframe = pandas.DataFrame(student_data)

for (index, row) in student_dataframe.iterrows():
    print(row.score)
