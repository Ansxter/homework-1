import pandas as pd

df = pd.read_csv("SuperMarket Analysis.csv")


print("資料筆數:", len(df))
print(df.head())

branch_map = {"A": "Yangon", "B": "Mandalay", "C": "Naypyitaw"}

filtered = df[(df["Branch"] == branch_map["A"]) & (df["Customer type"] == "Member")]

print("篩選後筆數:", len(filtered))
print(filtered.head())

product_summary = filtered.groupby("Product line").agg(
    Total_Sales=("Sales", "sum"),
    Avg_Rating=("Rating", "mean")
).reset_index()


product_summary["Total_Sales"] = product_summary["Total_Sales"].round(2)
product_summary["Avg_Rating"] = product_summary["Avg_Rating"].round(2)

print("\n各產品線銷售與評分：\n", product_summary)


city_gender_summary = filtered.groupby(["City", "Gender"]).agg(
    Avg_Sales=("Sales", "mean"),
    Transaction_Count=("Invoice ID", "count")
).reset_index()

city_gender_summary["Avg_Sales"] = city_gender_summary["Avg_Sales"].round(2)

print("\n依 City 與 Gender 分組：\n", city_gender_summary)


if not product_summary.empty:
    top_product_line = product_summary.loc[product_summary["Total_Sales"].idxmax(), "Product line"]
    print("\n總銷售額最高的產品線:", top_product_line)
else:
    print("\n⚠️ 沒有符合條件的產品線資料")


product_summary.to_csv("0520_pandas_3OK.CSV", index=False)

