largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    number = []

    if num == "done":
        break
        
    try:
        num = int(num)
        # number.append(num)
        
        if (smallest == None) or (smallest > num):
            smallest = num
        elif largest == None or largest < num:
            largest = num
        
    except:
        print("Invalid input")
        continue
    
#    print(num)

print("Maximum is", largest)
print("Minimum is", smallest)
