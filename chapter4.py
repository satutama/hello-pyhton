#Functions

def thing():
    print('Hello')
    print('Fun')

thing()
print('Done')

# built-in function
hello = 'Hello world'
big = max(hello)
tiny = min(hello)
print(big)
print(tiny)

# Arguments and parameter
def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')

greet('es')
greet('fr')
greet('test')

# Return values
def addTwo(a,b):
    return a+b

print(addTwo(1,5))

# Excercise
def computePay(hours, rate):
    if hours > 40:
        reg = rate * hours
        otp = (hours - 40.0) * (rate * 0.5)
        pay = reg + otp
    else:
        pay = hours * rate
    
    return pay

sh= input('Enter Hours: ')
sr= input('Enter Rate: ')
fh= float(sh)
fr= float(sr)

xp = computePay(fh,fr)

print('Pay:', xp)
