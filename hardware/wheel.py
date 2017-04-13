#_positions = ['driver_front', 'driver_rear', 'passenger_front', 'passenger_rear']
_materials = ['aluminum', 'titanium']

wheel = {
          'position': ''
          ,'size': ''
          ,'lug_pattern': ''
          ,'material': ''
}

class WheelSet(object):
    '''return wheelset of count wheels'''
    
    _wheels = []
    
    def __init__(self, count):
        pass

class Wheel(object):
    def __init__(self
                 ,material='aluminum'
                 ,axel=''
                 ,lug_pattern=5
                 ,spoke_pattern='star'
                 ):
        if material in _materials:
            self._material = material
        else:
            raise AttributeError("invalid material specified")
        
#         if position in _positions:
#             self._position = position
#         else:
#             raise AttributeError("invalid position specified")
        
        self._lug_pattern = lug_pattern
        self._spoke_pattern = spoke_pattern
