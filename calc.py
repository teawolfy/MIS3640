#VARIABLES
seconds = 42*60+60      #convert to seconds
miles = 10/1.61         #convert to miles
spm = seconds/miles     #calculates seconds per miles
apm = spm/60            #calculates pace in minutes

#QUESTIONS
print('Q1:',seconds)
print('Q2:',miles)
print('Q3: average pace=',apm,'mph=', 60/apm)

