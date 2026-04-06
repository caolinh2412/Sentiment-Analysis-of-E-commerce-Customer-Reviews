import pandas as pd

# Đọc file Excel
df = pd.read_excel("Product_review_unlabel.xlsx")

# Danh sách shop cần lọc
shop_list = [
    3791784325,
    6955942015,
    20569803451,
    13560559943,
    20434747104,
    20425793191
]

# Lọc dữ liệu
filtered_df = df[df['shopid'].isin(shop_list)]

# Lưu ra file Excel mới
filtered_df.to_excel("filtered_shops.xlsx", index=False)

print(filtered_df.head())