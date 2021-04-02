def concat(*args, sep="/"):
    return sep.join(args)

concat("earth", "mars", "venus")
#'earth/mars/venus'
concat("earth", "mars", "venus", sep=".")
#'earth.mars.venus'

-----------
list(range(3, 6)) # нормальный вызов с отдельными аргументами
#[3, 4, 5]
args = [3, 6]
list(range(*args)) # вызов с аргументами, распакованными из списка
#[3, 4, 5]

------------
def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")
    
d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)

#This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !
--------------

L = ['a', 'b', 'c']
print(id(L))

L.append('d')
print(id(L))

----------------