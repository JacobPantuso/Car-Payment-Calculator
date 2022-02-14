# This python program will take the purchase price of a vehicle, the purchase type (cash, finance, lease), and the rate (if applicable). 
# The program will calculate the monthly/biweekly payments and suggested income.

# This defined function below "paymentCalculator" will calculate the payments based on the user input while using those values to calculate the suggested income
def paymentCalculator(u,v,w,x,y,z): # payType = u, payRate = v, price = w, interval = x, length = y, downpayment = z
    a = w
    w = w-z
    monthlyIncome = income/12
    biweeklyIncome = monthlyIncome/2
    if u == "cash": # If the user is paying in cash, this conditional statement will be executed 
        payments = w
        print("")
        print("Since you are paying cash. The upfront cost of the veiche will be $" + str(payments))
    elif u == "finance" or u == "lease": # If the user is financing or leasing, this conditional statement will be executed 
        v = v/100 
        rate = (v/12) # Getting the interest rate per month
        if x == "biweekly": # Biweekly payments calculator conditional block
            if rate > 0:
                payments = (rate * w)/(1-(1+rate)**(y*-1)) # Calculating the monthly payments of the car using the given values
            elif rate == 0:
                payments = w/y # Calculating the monthly payments of the car using the given value            
            payments = payments/2 # Biweekly payment calculator
            payments = round(payments,2) # Rounding to two decimal places
            maxBiAfford = biweeklyIncome*0.15
            maxBiAfford = round(maxBiAfford, 2) # Rounding to two decimal places
            reccBiAfford = biweeklyIncome*0.12
            reccBiAfford = round(reccBiAfford, 2) # Rounding to two decimal places
            v=v*100
            v = round(v,2) # Rounding to two decimal places
            print("")
            print("If the vehicle you purchcase is $" + str(a) + " and you put $" + str(z) + " down on a " + str(y) + " month term at " + str(v) + "%. The biweekly payments will be $" + str(payments)) 
        else: # Monthly payments calculator conditional block
            if rate > 0:
                payments = (rate * w)/(1-(1+rate)**(y*-1)) # Calculating the monthly payments of the car using the given values
            elif rate == 0:
                payments = w/y # Calculating the monthly payments of the car using the given value
            payments = round(payments,2) # Rounding to two decimal places
            maxAfford = monthlyIncome*0.15
            maxAfford = round(maxAfford, 2) # Rounding to two decimal places
            reccAfford = monthlyIncome*0.12
            reccAfford = round(reccAfford, 2) # Rounding to two decimal places
            v=v*100
            v = round(v,2)
            print("")
            print("If the vehicle you purchcase is $" + str(a) + " and you put $" + str(z) + " down on a " + str(y) + " month term at " + str(v) + "%. The monthly payments will be $" + str(payments)) 
    print("")
    leftover = monthlyIncome-payments # Calculating how much leftover income will be left after monthly payments
    leftover = round(leftover,2) # Rounding to two decimal places
    leftoverbi= biweeklyIncome-payments
    leftoverbi = round(leftoverbi,2) # Rounding to two decimal places
    if u == "cash":
        print("Since you selected cash, you will need the total amount to cover the vehicles cost.")
    if x == "monthly" and payments > maxAfford:
        print("With the values provided, this vehicles payments will take more than 15% from your gross monthly income. The max you can afford with your income is $"+ str(maxAfford)+ " per month.")
    elif x == "monthly" and payments < reccAfford:
        print("With the values provided, this vehicle is in the suggested payment range. With your monthly income, you can afford this vehicles monthly payments. Your remaining gross monthly income will be $"+str(leftover))
    if x == "biweekly" and payments > maxBiAfford:
        print("With the values provided, this vehicles payments will take more than 15% from your gross biweekly income. The max you can afford with your income is $"+ str(maxBiAfford)+ " biweekly.")
    elif x=="biweekly" and payments < reccBiAfford:
        print("With the values provided, this vehicle is in the suggested payment range. With your biweekly income, you can afford this vehicles biweekly payments. Your remaining gross biweekly income will be $"+str(leftoverbi))

if __name__ == "__main__":
    quit = True # Setting boolean expression for exit condition
    while quit != False: 
        n=0
        while n == 0: # While loop to ensure that the user enters a valid purchase price
            print("")
            price = float(input("Please enter the purchase price of the vehicle (including taxes + fees):\n")) # Getting the price of the vehicle
            if price < 0:
                print("Please enter a valid purchase price!")
            elif price > 0:
                z=0
                while z == 0:
                    print("")
                    downpayment = float(input("Please enter the downpayment, if none enter 0:\n")) # Getting a downpayment value
                    if downpayment < 0:
                        print("Please enter a valid downpayment!")
                    elif downpayment > price:
                        print("Please enter a valid downpayment!")
                    else:
                        n+=1
                        z+=1
        n=0
        while n == 0: # While loop to ensure that the user enters a valid payment type
            print("")
            payType = input("How would you like to pay for the vehicle (Finance, Lease, or Cash)?\n") # Getting how the user would like to pay for the vehicle
            payType=payType.lower()
            if payType != "finance" and payType != "lease" and payType != "cash":
                print("Please enter a valid payment type!")
            elif payType == "finance" or payType == "lease":
                z=0
                while z==0:
                    print("")
                    interval = input("Are the payments monthly or biweekly?\n") # Getting if the user will be paying monthly or biweekly for the vehicle
                    interval = interval.lower()
                    if interval != "monthly" and interval != "biweekly":
                        print("Please enter a valid payment interval!")
                    else:
                        n+=1
                        z+=1
            else:
                n+=1
        n=0
        if payType == "finance" or payType == "lease":
            while n == 0: # While loop to ensure that the user enters a valid rate type if applicable
                print("")
                payRate = float(input("What is the interest rate? (Enter without percent symbol!):\n")) # Getting the interest rate for the payments
                if payRate < 0:
                    print("Please enter a valid payment rate!")   
                elif payRate >= 0:
                    z=0
                    while z==0:
                        print("")
                        length = int(input("How long are the payments for? (In Months)\n")) # Getting how long the payments are for
                        if length < 0:
                            print("Please enter a valid term length!")
                        else:
                            n+=1
                            z+=1
        n=0
        while n == 0:
            print("")
            income= float(input("For affordability reasons, what is your gross annual income?\n")) # Getting the income to suggest if the user can afford the vehicle.
            if income < 0:
                print("Please enter a valid income!")
            else:
                n+=1
        if payType == "finance" or payType == "lease":
            paymentCalculator(payType,payRate,price,interval,length,downpayment)
        else:
            paymentCalculator(payType,0,price,0,0,downpayment)
        print("")
        inp = input("Would you like to recalculate? (yes or no)\n")
        if inp == "no":
            quit = False
            print("")
            print("Goodbye!")
        else:
            continue