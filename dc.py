#!/usr/bin/env python

import numpy as np
from scipy.integrate import quad

def intgnd(a, h, Om0, Ol0, Or0):
    #Define the integrand by Equation B5 in J.J. Condon &
    #A.M. Matthews (PASP, 2018).
    H0 = 100. * h
    c = 299792.458 #km/s
    return (c/H0) \
        / np.sqrt(Om0 * a + Or0 + Ol0 * a**4.)

def dc(z, h, Om0):
    #Function used to calculate the comoving distance at
    #redshift z for a Hubble parameter, h, and current normalized
    #matter density, Om0. Calculations assume a flat universe, i.e.
    #Ok0 = 1.0. Comoving distance returned in units of Mpc.
    #Integration is done using scipy.integrate.quad.
    Or0 = h**(-2.)*4.2e-5
    Ol0 = 1. - Om0 - Or0

    #Calculate scale factor, a.
    a = 1./(1.+z)

    #Do the integral.
    dc = quad(intgnd, a, 1., args=(h, Om0, Ol0, Or0))[0]
    return dc

