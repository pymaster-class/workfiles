# 
'''


if (condition -  it returns true):
    action

'''

'''
# ph - 1-6.9 - Acidic
ph - 7 - Neutral
ph - 7.1 - 14.0 -Basic

'''
ph = float(input('Enter ph: '))

if (ph > 0 and ph <=6.9):
    print('ph is acidic')
elif (ph==7):
    print('The pH is neutral')
elif (ph >= 7.1 and ph <=14.0):

    print('pH is basic')
else:
    print('I dunno')