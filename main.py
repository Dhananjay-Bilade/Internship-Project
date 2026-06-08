from preprocessing import load_data, clean_data
from analysis import jobs_per_category, jobs_per_location, average_salary, salary_statistics
from visualization import (
    jobs_by_category_chart,
    jobs_by_location_chart,
    salary_distribution,
    category_pie_chart,
    experience_vs_salary,
    jobs_posted_per_month
)

data = load_data()
data = clean_data(data)

while True:

    print("\n===== JOB ANALYTICS TOOL =====")

    print("1 View Dataset")
    print("2 Jobs per Category")
    print("3 Jobs per Location")
    print("4 Average Salary per Category")
    print("5 Salary Statistics")

    print("\n--- Charts ---")
    print("6 Jobs per Category Chart")
    print("7 Jobs per Location Chart")
    print("8 Salary Distribution")
    print("9 Job Category Pie Chart")
    print("10 Experience vs Salary")
    print("11 Jobs Posted per Month")

    print("\n12 Exit")

    choice = input("\nEnter choice: ")

    if choice == "1":
        print(data)

    elif choice == "2":
        jobs_per_category(data)

    elif choice == "3":
        jobs_per_location(data)

    elif choice == "4":
        average_salary(data)

    elif choice == "5":
        salary_statistics(data)

    elif choice == "6":
        jobs_by_category_chart(data)

    elif choice == "7":
        jobs_by_location_chart(data)

    elif choice == "8":
        salary_distribution(data)

    elif choice == "9":
        category_pie_chart(data)

    elif choice == "10":
        experience_vs_salary(data)

    elif choice == "11":
        jobs_posted_per_month(data)

    elif choice == "12":
        print("Exiting Job Analytics Tool...")
        break

    else:
        print("Invalid choice, please try again.")