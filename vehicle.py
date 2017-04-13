#!python3
''' automobile class for operating and tracking stats on autos '''

from .hardware import 

class Vehicle(object):
    
    def __init__(self, make, model, axel_count=2, wheel_count=4):
        #trim
        self._axels = []
        
        pass
        
    options = {}
    
    def move(self, direction=None, speed=0):
        '''move vehicle in specified direction at specified speed (mph)'''
        pass
    
    def notify_user(self, msg='', priority=0):
        '''send message to driver of vehicle'''
        pass
    
    
class Moto(Vehicle):
    wheels = {
              'front': ''
              ,'rear': ''
              }
    

class Car(Vehicle):
    def __init__(self):
        pass
    

class Truck(Vehicle):
    def __init__(self):
        pass
    

class Semi(Vehicle):
    def __init__(self):
        pass