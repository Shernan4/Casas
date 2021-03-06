#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 17:16:21 2018

@author: sebas
"""
import numpy as np 
from scipy import integrate
import matplotlib.pyplot as plt

def pendulo(t, y):
    """
    Funcion que regresa el lado derecho de un sistema de ecuaciones diferenciales
    
    Parameters
    ----------
    t : time
        Instante de tiempo
    y : array-like 
        Contiene la informacion del angulo (Theta) y la velocidad angular (omega)
        
    Returns
    -------
    Las dos derivadas de theta y omega
    
    """
    
    # Nombrando las variables
    theta, omega = y
    
    # Constantes
    b = 0.25
    c = 5.0
    
    d_theta = omega
    d_omega = -b * omega - (c * np.sin(theta))
    
    return [d_theta, d_omega]

y_initial = [0,np.pi]
tlist = np.linspace(0,10,100)

solution = integrate.solve_ivp(pendulo, (0, 10), y_initial, t_eval=tlist)

fig, axis = plt.subplots()
axis.plot(solution.t, solution.y.T)
plt.show()


