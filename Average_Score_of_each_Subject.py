/*You have been provided with exam scores for a group of students. Your task is to analyze these scores using Python and pandas.

Instructions:
Create a DataFrame: Using the data provided in the editor, create a DataFrame that includes student names and their scores in different subjects (Math, English, Science).
Display the DataFrame: Print the DataFrame to show the student names and their scores.
Calculate Average Scores: Compute and display the average score for each subject (Math, English, Science).

Output Format:
Student Exam Scores: Display the DataFrame showing all students and their scores followed by the print statement "Student Exam Scores:".
Average Scores: Display the average score for each subject (Math, English, Science) followed by the print statement "Average Score:".


  
import pandas as pd

def analyze_student_scores():
	data = {'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
			'Math': [85, 92, 78, 65, 89],
			'English': [90, 88, 75, 82, 95],
			'Science': [80, 85, 92, 70, 88]}
	print("Student Exam Scores:")
	ds=pd.DataFrame(data)
	print(ds)
	print("Average Score:")
	sc=ds.drop("Student",axis=1)
	sc=sc.mean()
	print(sc)
analyze_student_scores()
