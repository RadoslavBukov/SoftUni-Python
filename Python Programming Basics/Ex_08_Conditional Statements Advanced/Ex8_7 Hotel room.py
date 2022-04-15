"""
Input               Output
May                 Apartment: 877.50 lv.
15	                Studio: 525.00 lv.

June                Apartment: 961.80 lv.
14	                Studio: 1052.80 lv.

August              Apartment: 1386.00 lv.
20	                Studio: 1520.00 lv.
"""
month = str(input())
nights_number = int(input())

if month == "May" or month == "October":
    apartment_price = 65
    studio_price = 50
    if 7 < nights_number <= 14:
        studio_price -= studio_price * 0.05
    elif nights_number > 14:
        studio_price -= studio_price * 0.3
        apartment_price -= apartment_price * 0.1
elif month == "June" or month == "September":
    apartment_price = 68.7
    studio_price = 75.2
    if nights_number > 14:
        studio_price -= studio_price * 0.2
        apartment_price -= apartment_price * 0.1
elif month == "July" or month == "August":
    apartment_price = 77
    studio_price = 76
    if nights_number > 14:
        apartment_price -= apartment_price * 0.1

studio_price = studio_price * nights_number
apartment_price = apartment_price * nights_number

print(f"Apartment: {apartment_price:.2f} lv.")
print(f"Studio: {studio_price:.2f} lv.")