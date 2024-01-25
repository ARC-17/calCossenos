from pylab import *

ent = arange(.5, 30.7, .1)

sai = cos(ent)

plot(ent, sai)

xlabel('entrada')

ylabel('cosseno')

title('Cossenos')

grid(True)

show()