# astro-cosmo
Functions to evaluate cosmological quantities assuming a homogeneous, isotropic, and flat LCDM universe. 

Function "dc.py" calculates the comoving distance out to arbitrary redshift, z, having specified the Hubble
parameter, $h$, and the current normalized matter density, $\Omega_{0,m}$. The elliptic integral in terms of 
the scale parameter, $a$, is evaluated using the scipy.integrate.quad. The resulting distance is returned in 
units of Mpc. This function includes the current normalized radiation density, $\Omega_{0,r}$, and is therefore
accurate out to high redshifts ($z > 3500)$.
