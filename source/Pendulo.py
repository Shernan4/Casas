#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 17:16:21 2018

@author: sebas
"""
import numpy as np 
from scipy import integrate

def pendulo(t, y):
    """
    Funcion que regresa el lado derecho de un sistema de ecuaciones diferenciales
    
    Parameters
    ----------
    t : time
        Instante de tiempo
    y : array-like 
        Contiene la informacion del angulo (Theta) y la velocidad angular (omega)    
    
    """
    
    # Nombrando las variables
    theta, omega = y
    
    # Constantes
    b = 0.25
    c = 5.0
    
    d_theta = omega
    d_omega = -b * omega - (c * np.sin(theta))
    
    return [d_theta, d_omega]