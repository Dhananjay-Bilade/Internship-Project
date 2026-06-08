import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from matplotlib.ticker import FuncFormatter


def jobs_by_category_chart(data):

    sns.set_theme(style="whitegrid")
    category_counts = data["category"].value_counts().reset_index()
    category_counts.columns = ["category","count"]

    plt.figure(figsize=(9,5))

    ax = sns.barplot(
        x="category",
        y="count",
        hue="category",
        data=category_counts,
        palette="magma",
        edgecolor="black",
        legend=False
    )

    plt.title("Number of Jobs per Category",fontsize=16,weight='bold')
    plt.xlabel("Job Category",fontsize=12)
    plt.ylabel("Number of Jobs",fontsize=12)

    plt.xticks(rotation=30)

    for p in ax.patches:
        height = p.get_height()
        ax.text(
            p.get_x() + p.get_width()/2,
            height,
            int(height),
            ha="center",
            va="bottom",
            fontsize=10,
            weight="bold"
        )

    plt.grid(axis="y", linestyle="--", alpha=0.6)

    plt.tight_layout()
    plt.show()


def jobs_by_location_chart(data):

    sns.set_theme(style="whitegrid")
    location_counts = data["location"].value_counts().reset_index()
    location_counts.columns = ["location","count"]

    plt.figure(figsize=(9,5))

    ax = sns.barplot(
        x="location",
        y="count",
        hue="location",
        data=location_counts,
        palette="viridis",
        edgecolor="black",
        legend=False
    )

    plt.title("Number of Jobs per Location",fontsize=16,weight='bold')
    plt.xlabel("Location",fontsize=12)
    plt.ylabel("Number of Jobs",fontsize=12)

    plt.xticks(rotation=30)

    for p in ax.patches:
        height = p.get_height()
        ax.text(
            p.get_x() + p.get_width()/2,
            height,
            int(height),
            ha="center",
            va="bottom",
            fontsize=10,
            weight='bold'
        )

    plt.grid(axis="y", linestyle="--", alpha=0.7)

    plt.tight_layout()
    plt.show()



def salary_distribution(data):

    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(8,5))

    sns.histplot(
        data["salary"],
        bins=10,
        kde=False,
        color="skyblue",
        edgecolor="black",
        linewidth=1.2,
        alpha=0.7
    )

    kde = sns.kdeplot(
        data["salary"],
        color="red",
        linewidth=2,
    )

    y_vals = kde.get_lines()[0].get_ydata()

    #scaling
    bin_width = (data["salary"].max() - data["salary"].min()) / 10
    scale = len(data["salary"]) * bin_width
    kde.get_lines()[0].set_ydata(y_vals * scale)

    plt.title("Salary Distribution",fontsize=16,weight='bold')
    plt.xlabel("Salary",fontsize=12)
    plt.ylabel("Number of Jobs",fontsize=12)

    # removing scientific notation of salary
    plt.ticklabel_format(style='plain',axis='x')

    # Formating salary with commas
    formatter = FuncFormatter(lambda x, pos: f'{int(x):,}')

    plt.gca().xaxis.set_major_formatter(formatter)

    plt.grid(axis="y", linestyle="--", alpha=0.6)
    plt.gca().patch.set_alpha(0.95)
    plt.tight_layout()
    plt.show()



def category_pie_chart(data):

    sns.set_theme(style="whitegrid")
    category_counts = data["category"].value_counts()

    #color palette
    colors = sns.color_palette("pastel")

    plt.figure(figsize=(7,7))

    wedges, texts, autotexts = plt.pie(
        category_counts.values,
        labels=category_counts.index,
        autopct='%1.1f%%',
        colors=colors,
        startangle=140,
        wedgeprops={'edgecolor':'black','linewidth': 1}
    )

    for w in wedges:
        w.set_edgecolor('black')
        w.set_linewidth(1.5)

    for autotext in autotexts:
        autotext.set_color('black')
        autotext.set_fontsize(11)
        autotext.set_weight('bold')

    for text in texts:
        text.set_fontsize(11)
        text.set_weight('bold')
    
    plt.title("Job Category Distribution",fontsize=16,weight='bold')
    plt.axis('equal')
    plt.tight_layout()
    plt.show()



def experience_vs_salary(data):

    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(9, 5))
    data["experience_years"] = data["experience_years"].astype(int)

    sns.regplot(
        x="experience_years",
        y="salary",
        data=data,
        line_kws={
            "linewidth": 3,
            "linestyle": "-",
            "color": "crimson" },
        ci=None
    )

    # Unique X values
    x_vals = sorted(data["experience_years"].unique())

    # Linear regression 
    z = np.polyfit(data["experience_years"], data["salary"], 1)
    p = np.poly1d(z)

    # Y values on regression line
    y_vals = p(x_vals)

    # Plot only intersection points
    plt.scatter(x_vals, y_vals, color='red', zorder=5)

    # Add labels on intersection points
    for x, y in zip(x_vals, y_vals):
        plt.text(
            x, y,
            f'{int(y):,}', fontsize=9, ha='center', va='bottom', color='black', weight='bold'
        )

    plt.title("Experience vs Salary", fontsize=16, weight='bold')
    plt.xlabel("Years of Experience", fontsize=12)
    plt.ylabel("Salary (₹)", fontsize=12)

    plt.ticklabel_format(style='plain', axis='y')
    formatter = FuncFormatter(lambda x, pos: f'{int(x):,}')
    plt.gca().yaxis.set_major_formatter(formatter)

    plt.xticks(sorted(data["experience_years"].unique()))

    plt.grid(True, linestyle="--", alpha=0.6)

    plt.gca().patch.set_alpha(0.9)

    plt.tight_layout()
    plt.show()


def jobs_posted_per_month(data):

    sns.set_theme(style="whitegrid")
    data["month"] = pd.to_datetime(data["posted_date"]).dt.month

    month_counts = data["month"].value_counts().sort_index()
    all_months = pd.Series(0,index=range(1,13))
    month_counts = all_months.add(month_counts, fill_value=0)

    month_map = {
        1:"Jan", 2:"Feb",3:"Mar",4:"Apr",5:"May",6:"Jun",
        7:"Jul",8:"Aug",9:"Sep",10:"Oct",11:"Nov",12:"Dec"
    }

    df = pd.DataFrame({
        "Month_num" : month_counts.index,
        "Month" : [month_map[m] for m in month_counts.index],
        "Jobs" : month_counts.values
    })

    plt.figure(figsize=(10,5))

    sns.lineplot(
        x="Month", y="Jobs",
        data=df, marker="o", sort=False,
        linewidth=3, markersize=8, color="#2E86C1"
    )

    max_idx = df["Jobs"].idxmax()
    plt.scatter(
        max_idx,
        df["Jobs"][max_idx],
        color="red", s=120, zorder=5, label="Peak"
    )

    plt.title("Jobs Posted per Month",fontsize=16, weight='bold')
    plt.xlabel("Month",fontsize=12)
    plt.ylabel("Number of Jobs",fontsize=12)
    sns.set_theme(style="whitegrid")

    for i, val in enumerate(df["Jobs"]):
        plt.text(i,val,int(val),ha='center',va='bottom',fontsize=9)

    plt.grid(True, linestyle="--", alpha=0.5)
    plt.legend()
    plt.tight_layout()
    plt.show()
