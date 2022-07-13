amount = float(input("Enter Amount Value:"))
"""
if amount >= 149:
    print("Eligible to Apply Promo Code")
    print("Apply ZOMATO to get 40% Off upto \u20b9100")
else:
    print('Not Eligible to Apply Promo Code')
"""

# Nested if/else | if/else within if/else
"""if amount >= 149:
    print("Eligible to Apply Promo Code")
    print("Apply ZOMATO to get 40% Off upto \u20b9100")

    promoCode = input("Enter the Promo Code:")
    if promoCode == "CRAVINGS":
        discount = 0.40* amount
        amountToPay = 0
        if discount >= 100:
            discount = 100
#           amountToPay = amount - 100
#        else:
        amountToPay = amount - discount
        print("Discount of \u20b9", discount, "applied. Please Pay:\u20b9", amountToPay)
    else:
        print("Sorry!! Promo Code Not Applicable")
else:
    print('Not Eligible to Apply Promo Code')
"""
# CRAVINGS:  40% Off upto Rs.100 | amount >=149
# JUMBO:     50% Off upto Rs.200 | amount >=500
# BINGO:     Flat 20% Off        | amount >=100

# Ladder if/else
if amount >= 100:
    promoCode = input("Enter the Promo Code:")
    if promoCode == "CRAVINGS":
        discount = 0.40* amount
        if discount >= 100:
            discount = 100
        amountToPay = amount - discount
        print("CRAVINGS Applied")
        print("Discount of \u20b9", discount, "applied. Please Pay:\u20b9", amountToPay)
    elif promoCode == "JUMBO":
        discount = 0.50* amount
        if discount >= 200:
            discount = 200
        amountToPay = amount - discount
        print("JUMBO Applied")
        print("Discount of \u20b9", discount, "applied. Please Pay:\u20b9", amountToPay)
    elif promoCode == "BINGO":
        discount = 0.20 * amount
        amountToPay = amount - discount
        print("BINGO Appied")
        print("Discount of \u20b9", discount, "applied. Please Pay:\u20b9", amountToPay)
    else:
        print("Sorry!! Promo Code ", promoCode,"Not Applicable")
        print("Please pay \u20b9", amount)
else:
    print('No Promo Code Applicable')
    print("Please pay \u20b9", amount)

# In the same program suggest the right promo code to the user if user is getting
# less discount as compared to the promo code which he has entered