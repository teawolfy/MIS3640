import bookanalysis

def poe1():
    hist = process_file('poe1.txt', skip_header=True)
    scarywords = list(process_file('horrorkeywords.txt', skip_header=False).keys())
    t = compare(hist,scarywords)
    print('The most common scary words are:' )
    print_most_common(t ,num = 200)
    #score(hist)
    #print('The scary score for Poe is: ')

def poe3():
    hist = process_file('poe3.txt', skip_header=True)
    scarywords = list(process_file('horrorkeywords.txt', skip_header=False).keys())
    t = compare(hist,scarywords)
    print('The most common scary words are:' )
    print_most_common(t ,num = 200)

def poe5():
    hist = process_file('poe2.txt', skip_header=True)
    scarywords = list(process_file('horrorkeywords.txt', skip_header=False).keys())
    t = compare(hist,scarywords)
    print('The most common scary words are:' )
    print_most_common(t ,num = 200)

def poe():
    poe1()
    poe3()
    poe5()

poe()