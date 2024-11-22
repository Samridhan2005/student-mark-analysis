import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv(r'E:\python_miniproject\student_marks.csv')


# Calculate the average marks for each student across all subjects
df['Average'] = df[['Math', 'Science', 'English', 'History', 'Geography', 'Com.Science']].mean(axis=1)

# Display the results (name and average marks)
print(df[['Name', 'Average']])

# Bar chart for average marks per student
plt.figure(figsize=(8, 5))
plt.bar(df['Name'], df['Average'], color='skyblue')
plt.title('Average Marks of Each Student')
plt.xlabel('Student')
plt.ylabel('Average Marks')
plt.xticks(rotation=40)
plt.show()
