#MODEL
one_plus_day_1_sales = 150
one_plus_day_2_sales = 250
one_plus_day_3_sales = 100

profits_to_amazon_from_oneplus = 200.27

discounts_from_sbi_to_oneplus = 3000.12

home_appl_day_1_sales = 120
home_appl_day_2_sales = 220
home_appl_day_3_sales = 180

profits_to_amazon_from_home_appl = 50

discounts_from_sbi_to_home_appl = 100

#CONTROLLER

total_oneplus_sales = one_plus_day_1_sales + one_plus_day_2_sales + one_plus_day_3_sales
total_home_appl_sales = home_appl_day_1_sales + home_appl_day_2_sales + home_appl_day_3_sales

net_oneplus_sales = total_oneplus_sales * profits_to_amazon_from_oneplus
net_home_appl_sales = total_home_appl_sales * profits_to_amazon_from_home_appl

print("Oneplus Sale Profits Made by Amazon", net_oneplus_sales)
print("Home Appliances Sale Profits Made by Amazon", net_home_appl_sales)

if net_oneplus_sales > net_home_appl_sales:
    print("Amazon Made more Profit on OnePlus Sales by :",net_oneplus_sales - net_home_appl_sales)
else:
    print("Amazon Made more Profit on Home Appliances Sales by :", net_home_appl_sales - net_oneplus_sales)