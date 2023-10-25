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

#Arguments and parameter
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