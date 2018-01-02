import numpy as np # for arrays, linspace, cos, sin, etc.
import scipy.integrate as sp # for integrals
import matplotlib.pyplot as plt # for plotting

# note: "nu" is a greek letter. It's pronounced like "noo".

def C(z):
    return np.cos((np.pi*z**2)*0.5) #integrals given in question
def S(z):
    return np.sin((np.pi*z**2)*0.5)
def II0(nu):
    return 0.5*((Cnu - 0.5)**2 + (Snu - 0.5)**2) # I/I_0. Cnu and Snu handled later

nu = np.linspace(0, 10, 1000)# creates an array like (0, 0.01, 0.02, ..., 10)
Cnu = np.zeros(1000) # creates an array of a thousand 0s
Snu = np.zeros(1000) # creates an array of a thousand 0s

for i in range(len(Cnu)):
    Cnu[i] = sp.quad(C, 0, nu[i])[0]
for i in range(len(Snu)):
    Snu[i] = sp.quad(S, 0, nu[i])[0]

## Above: takes each element of the array Cnu and replaces it with the
## result of the Fresnel integral evaluated between 0 and n[i]. So the
## first element is the integral between 0 and 0, the next is between
## 0 and 0.01, then between 0 and 0.02, and so on until it reaches
## between 0 and 10. Does the same for Snu.

plt.figure(1)  # code from here onwards is only for plotting.
plt.suptitle("Fresnel Integral C(nu) against nu (proportional to distance travelled)")
plt.plot(nu, Cnu)
plt.xlabel("nu")
plt.ylabel("Fresnel integral, C(nu)")
plt.xlim(0, 10)
plt.ylim(0, 1)

plt.figure(2)
plt.suptitle("Fresnel Integral S(nu) against  nu(proportional to distance travelled)")
plt.plot(nu, Snu)
plt.xlabel("nu")
plt.ylabel("Fresnel integral, (nu)")
plt.xlim(0, 10)
plt.ylim(0, 1)

plt.figure(3)
plt.suptitle("I/I_0 against nu")
plt.plot(nu, II0(nu))
plt.xlabel("nu")
plt.ylabel("I/I_0")
plt.xlim(0, 10)
plt.ylim(0, 0.3)

plt.show()
