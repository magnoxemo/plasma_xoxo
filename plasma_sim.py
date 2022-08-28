import numpy as np 
import matplotlib.pyplot as plt 
import math 
import vector 
from matplotlib import animation

class elctron():

    #fundamental constants 

    """position """
    x=[]
    y=[]
    z=[]


    def __init__(self,T):

        charge=1.6*10**-19
        mass=9.11*10**-31
        k=1.9*10**-23
        m=self.mass
        temp=T
        K=self.k
        v0=math.sqrt(K*temp/m)

        pass

    def electric_force(self):

        electric_force=np.array(3)
        columb_constant=9*10**9
        r=[]
        def distance(r=[]):
            r=r
            return math.sqrt(r[0]**2+r[1]**2+r[2]**2)
        
        force=columb_constant*(1.6*10**-19)**2/math.pow(distance(r),2) 
            
        #as the force is a vector and it will have three components in x,y and  direction 

        pass 

    def magnetic_forcce(self):

        magnetic_force=np.array(3)

        pass 

    def position_updater(self):

        position=np.array(3)

        pass 

    def velocity_updater(self):

        velocity=np.array(3)
        

        pass 

    def acceleration_updater(self):
        acceleration=np.array(3)
        
        pass 

    def temp_updater(self,T):
        temp=T

        pass 

class proton():

    #fundamental constants 

    charge=1.6*10**-19
    mass=1.6*10**-28
    k=1.9*10**-23

    """position """
    x=[]
    y=[]
    z=[]


    def __init__(self,T):
        
        m=self.mass
        temp=T
        K=self.k
        v0=math.sqrt(K*temp/m)

        pass
    
    def electric_force(self):

        electric_force=np.array(3)
        columb_constant=9*10**9
        r=[]
        def distance(r=[]):
            r=r
            return math.sqrt(r[0]**2+r[1]**2+r[2]**2)
        
        force=columb_constant*(1.6*10**-19)**2/math.pow(distance(r),2) 
            
        #as the force is a vector and it will have three components in x,y and  direction 

        pass 

    def magnetic_forcce(self):

        magnetic_force=np.array(3)

        pass 

    def position_updater(self):

        position=np.array(3)

        pass 

    def velocity_updater(self):

        velocity=np.array(3)
        

        pass 

    def acceleration_updater():
        acceleration=np.array(3)
        
        pass 

    def temp_updater(self,T):
        temp=T

        pass 

def simulation_driver(number_of_particles_electron,number_of_particles_proton,temp,):
    pass 

def animation_show():
    pass 
