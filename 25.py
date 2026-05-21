import numpy as np

data = np.genfromtxt("Grocery_Inventory_and_Sales_Dataset.csv",delimiter=",",dtype=str,skip_header=1)

product_names = data[:, 1]  # 商品名稱
stock_qty = data[:, 5].astype(int)  # 庫存數量
unit_price = np.char.replace(data[:, 8], "$", "").astype(float)  # 單價
sales_volume = data[:, 13].astype(int)  # 銷售量


inventory_value = stock_qty * unit_price

best_seller_index = np.argmax(sales_volume)
best_seller = product_names[best_seller_index]

total_revenue = np.sum(sales_volume * unit_price)
discounted_revenue = total_revenue * 0.9

for i in range(len(product_names)):
    print(f"{product_names[i]} 的庫存價值: {inventory_value[i]:.2f}")

print("\n最暢銷商品:", best_seller)
print("總收入:", total_revenue)
print("9折後收入:", discounted_revenue)

