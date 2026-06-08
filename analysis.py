import numpy as np

def jobs_per_category(data):
    print(data["category"].value_counts())

def jobs_per_location(data):
    print(data["location"].value_counts())

def average_salary(data):
    print(data.groupby("category")["salary"].mean().round(2))

def salary_statistics(data):

    salary = data["salary"]

    print("Mean Salary:", np.mean(salary).round(2))
    print("Median Salary:", np.median(salary))
    print("Standard Deviation:", np.std(salary).round(2))

