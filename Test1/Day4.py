import pandas as pd
import matplotlib.pyplot as plot
df=pd.read_csv("Test1/employees.csv")
# result=df.groupby("department")
# x=result["salary"].mean()
# plot.bar(x.index,x.values)
# plot.title("Average salary per department")
# plot.xlabel("Department")
# plot.ylabel("Average Salary")
# plot.show()
# plot.hist(df["salary"], bins=5, color="skyblue", edgecolor="black")

# plot.title("Distribution of Employee Salaries")
# plot.xlabel("Salary")
# plot.ylabel("Number of Employees")

# plot.show()


# Get unique departments
departments = df["department"].unique()

# Plot each department separately
# for dept in departments:
#     data = df[df["department"] == dept]

#     plot.scatter(
#         data["id"],
#         data["salary"],
#         label=dept
#     )

# plot.title("Employee ID vs Salary by Department")
# plot.xlabel("Employee ID")
# plot.ylabel("Salary")
# plot.show()

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [12, 15, 14, 18, 22, 25]

plot.plot(
    months,
    sales,
    color="blue",
    marker="o",
    linestyle="-",
    linewidth=2,
    markersize=8,
    label="Monthly Sales"
)

plot.title("Monthly Sales")
plot.xlabel("Month")
plot.ylabel("Sales")

plot.legend()
plot.grid(True)

plot.show()
