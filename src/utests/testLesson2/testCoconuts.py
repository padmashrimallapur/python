import unittest
from lesson2.coconut import Coconut
from lesson2.coconuts import Inventory


class Test(unittest.TestCase):


    def setUp(self):
        self.coc_in = Coconut(type="IN", weight=3)
        self.coc_ca = Coconut(type="CA", weight=3)
        self.coc_us = Coconut(type="US", weight=2.5)
        self.inventory = Inventory()

    def testCoconutsAPI(self):
        self.inventory.add_coconuts(self.coc_in)
        self.assertEqual(3, self.inventory.total_weight(), "Total weight of coconuts is not matching!")
        
        self.inventory.add_coconuts(self.coc_ca)
        self.inventory.add_coconuts(self.coc_us)
        self.assertEqual(8.5, self.inventory.total_weight(), "Total weight of coconuts is not matching!")
        
        self.assertRaises(AttributeError, self.inventory.add_coconuts, "Not a Coconut Object")
        
        self.assertRaises(AttributeError, Coconut, name="Not a Coconut Object")
        self.assertRaises(AttributeError, Coconut, weight="Not an integer")


if __name__ == "__main__":
    unittest.main()