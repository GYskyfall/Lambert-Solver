"""
Notation:
a = Semimajor axiy
e = Eccentricity
E = Eccentric Anomaly
i = Inclination
k = Integer Number of revolution
r = Position Vector Magnitude
Deltat = Time of flight
mu = Gravitational parameter
nu = true anomaly
"""

import numpy as np
import math

# feste Konstanten:
# mu =


def lambert(r0_v, rf_v, DT0, DM):
    # TODO Dnu methode implementieren
    nu0 = math.atan2(r0_v[1]/r0_v[2])
    nuf = math.atan2(rf_v[1]/rf_v[2])
    Dnu= nuf - nu0
    r0 = np.linalg.norm(r0_v)
    rf = np.linalg.norm(rf_v)
    cos_D_nu = np.vdot(r0, rf)/(r0*rf)
    A = DM * math.sqrt(r0*rf*(1+ cos_D_nu))
    if Dnu == 0 or A == 0:
        print("Trajectory cant be computed")

    c2, c3 = 0.5, 1/6
    psi = 0 # psi eigentlich Eccentricity
    psi_up = 4*math.pi ** 2
    psi_low = 4*math.pi

    DT = 0 # Muss DT gesetzt werden, da while schleife evaluieren muss?

    while abs(DT - DT0) > 10**(-6):
        y = r0 + rf + A (psi * c3 - 1)/math.sqrt(c2)
        if A > 0.0 and y < 0.0:
            # readjust psi s.t. y > 0
            while y < 0:
                psi = psi + 0.1
                y = r0 + rf + A (psi * c3 - 1)/math.sqrt(c2)

        xi = math.sqrt(y/c2)
        DT = (xi**3 * c3 + A*math.sqrt(y))/(math.sqrt(mu))

        if DT <= DT0:
            psi_low = psi
        else:
            psi_up = psi

        psi = (psi_up + psi_low)/2



