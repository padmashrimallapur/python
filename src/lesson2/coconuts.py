from lesson2.coconut import Coconut


class Inventory(object):
    '''
    class docs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.coconuts = []
        
    def add_coconuts(self, coconut):
        '''
        Add coconuts API
        '''
        if not isinstance(coconut, Coconut):
            raise AttributeError("Object %s is not a type of Coconut" % coconut)
        self.coconuts.append(coconut)
        
    def total_weight(self):
        '''
        Get Total weight of all coconuts in inventory
        '''
        weight = 0
        for coconut in self.coconuts:
            weight += getattr(coconut, "weight")
            
        return weight