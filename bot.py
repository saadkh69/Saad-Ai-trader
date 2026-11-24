# Saad AI Trader
# Paper Trading - تجريبي فقط

balance = 100.0
coins = 0.0

prices = [100, 102, 105, 103, 99, 97, 101, 106]

for price in prices:
    print("السعر:", price)

    if price < 100 and balance >= 20:
        coins += 20 / price
        balance -= 20
        print("شراء تجريبي")

    elif price > 104 and coins > 0:
        balance += coins * price
        coins = 0
        print("بيع تجريبي")

    total = balance + coins * price
    print("قيمة المحفظة:", round(total, 2))
    print("----------------")

print("انتهى الاختبار")
