

class Coconut(object):
    '''
    classdocs
    '''

    def __init__(self, **kwargs):
        '''
        Constructor
        '''
        for key, value in kwargs.items():
            if hasattr(self, key):
                raise AttributeError("Attribute already exists")
            setattr(self, key, value)
            
        _ = getattr(self, "type")
        weight = getattr(self, "weight")
        if type(weight) is str:
            raise AttributeError("weight Attribute not found in this Coconut object")
        