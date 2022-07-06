hrs = input("Enter Hours:")
rate = input("Enter rate: ")

hrs = float(hrs)
rate = float(rate) # convert str to float

if hrs > 40:
    pay = 40*rate + (hrs-40)*(rate*1.5)
#    print("{:.2f}".format(pay))
    print(pay)
else:
    print(hrs*rate)

# above code doens't work
# below code worked???

hrs = input("Enter Hours:")
rate = input("Enter rate: ")

hrs = float(hrs)
rate = float(rate) # convert str to float

if hrs > 40:
    pay = 40*rate + (hrs-40)*(rate*1.5)
else:
    pay = hrs*rate
print(pay)