trans = {'0':'ling','1':'yi', '2':'er', '3':'san', '4':'si', '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10':'shi', '100':'bai'}

def speak_Chinese(number):
    '''
    number: a integer, 0<=number<99
    Returns: a string that is the number in Chinese
    '''
    if number < 11:
        x = str(number)
        a = trans[x]
        return a

    if number > 10 and number < 20:
        a = number - 10
        x = str(a)
        b = trans[x]
        return 'shi' + ' ' + b 

    if number == [20, 30, 40, 50, 60, 70, 80, 90]:
        number_string = str(number)
        for ch in number_string:
            first = number_string[0]
            a = trans[first]
            return a + ' ' + 'bai'
    
    if number > 20 and number < 100:
        number_string = str(number)
        for ch in number_string:
            first = number_string[0]
            a = trans[first]
            last = number_string[-1:]
            b = trans[last]
            if ch == 0:
                return a + ' ' + 'shi'
            else:
                return a +  ' ' + 'shi' + ' ' + b

    if number == [100, 200, 300, 400, 500, 600, 700, 800, 900]:
        number_string = str(number)
        for ch in number_string:
            first = number_string[0]
            a = trans[first]
            return a + ' ' + 'bai'

    if number > 100 and number < 1000:
        number_string = str(number)
        for ch in number_string:
            first = number_string[0]
            a = trans[first]
            middle = number_string[1]
            b = trans[middle]
            last = number_string[-1:]
            c = trans[last]
            if ch == 0:
                return a + ' ' + 'bai' + ' ' + b + ' ' + 'shi'
            else:
                return a + ' ' + 'bai' + ' ' + b + ' ' + 'shi' + ' ' + c
    pass

# For testing

def main():
    print(speak_Chinese(36))
    print('In Chinese: 36 = san shi liu')
    print(speak_Chinese(20))
    print('In Chinese: 20 = er shi')
    print(speak_Chinese(16))
    print('In Chinese: 16 = shi liu')
    print(speak_Chinese(109))
    print('In Chinese: 109 = yi bai ling jiu')
    print(speak_Chinese(200))
    print('In Chinese: 200 = er bai')
    print(speak_Chinese(999))
    print('In Chinese: 999 = jiu bai jiu shi jiu')

if __name__ == '__main__':
    main()