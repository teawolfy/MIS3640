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
#Question One
pi = 3.14159                        #value of pi
r = 5                               #value of radius
#Question Two
price = 24.95                       #price of book
discount = .4*price                 #wholesale discount
quantity = 60                       #number of books
shipping = 3+((quantity-1)*.75)     #shipping cost
#Question 3
easy tempo= 2*8.25                  #time at easy tempo
hard tempo= 3*7.2                   #time at hard tempo
total time= easy tempo + hard tempo #total time spent running
end time = total time - 8           #the amount of minutes past 7:00am
#Question 4
percent = ((89-82)/82)*100          #calculates total percentage


#QUESTIONS
print('Q1: volume=', (4/3)*pi*r**3)
print('Q2: wholesale cost=', (price-discount)*quantity+shipping)
print('Q3: 7:%d' % (end time))
print('Q4: %.1f%%' % percent)




