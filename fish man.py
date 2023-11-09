pond = float(input("vazne mahi ra be pond vared konid: "))

money = float(input("poly ke bayad be mahi gir pardakht konid ra vared konid: "))

kg = pond * 0.5

price = kg * 2

if money > price:
    print("jayezeh: fishing kit or more...")
else:
    print("jarimeh: ghayegh")

print("pole baghi mandeh: ", money - price)