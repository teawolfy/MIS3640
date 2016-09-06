print("EXERCISES CLASS ONE")
#VARIABLES
seconds = 42*60+60      #convert to seconds
miles = 10/1.61         #convert to miles
spm = seconds/miles     #calculates seconds per miles
apm = spm/60            #calculates pace in minutes

#QUESTIONS
print('Q1:',seconds)
print('Q2:',miles)
print('Q3: average pace=',apm,'mph=', 60/apm)

print('EXERCISES CLASS TWO')
#VARIABLES
pi = 3.14159                        #value of pi
r = 5                               #value of radius
price = 24.95                       #price of book
discount = .4*price                 #wholesale discount
quantity = 60                       #number of books
shipping = 3+((quantity-1)*.75)     #shipping cost

#QUESTIONS
print('Q1: volume=', (4/3)*pi*r**3)
print('Q2: wholesale cost=', (price-discount)*quantity+shipping)

