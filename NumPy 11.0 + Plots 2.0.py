import matplotlib.pyplot as plots
import numpy as np

Listx = np.arange(-5, 5, 0.1)
print(Listx)

Listy = Listx
Listz = Listx*Listx
Listw = Listz*Listx
plots.plot(Listx, Listy)
plots.show()
plots.plot(Listx, Listz)
plots.show()
plots.plot(Listx, Listw)
plots.show()