import unittest
from vehicle_slot import *

class TestString(unittest.TestCase):
    def test_vehicle_type(self):
        v=Vehicle(1,'car')
        level_1=Level({'car':2,'bike':2,'cycle':1},2,level=[])
        level_2=Level({'car':2,'bike':3},2,level=[])
        parking=Parking()
        x=parking.check_vehicle_entry('car',allowed_vehicle={'car':2,'bike':2})
        self.assertTrue(x,True)

    def test_vehicle_type1(self):
        v=Vehicle(1,'car')
        level_1=Level({'car':2,'bike':2,'cycle':1},2,level=[])
        level_2=Level({'car':2,'bike':3},2,level=[])
        parking=Parking()
        x=parking.check_vehicle_entry('train',allowed_vehicle={'car':2,'bike':2})
        self.assertFalse(x,False)

    def test_vehicle_type2(self):
        v=Vehicle(1,'car')
        level_1=Level({'car':2,'bike':2,'cycle':1},2,level=[])
        level_2=Level({'car':2,'bike':3},2,level=[])
        parking=Parking()
        x=parking.check_vehicle_entry('cycle',allowed_vehicle={'car':2,'bike':2})
        self.assertFalse(x,False)

        
        
    def test_vehicle(self):
        v=Vehicle(1,'car')
        level_1=Level({'car':2,'bike':2,'cycle':1},2,level=[])
        level_2=Level({'car':2,'bike':3},2,level=[])
        parking=Parking()
        x=parking.check_vehicle_entry('train',allowed_vehicle={'car':2,'bike':2})
        self.assertFalse(x,False)

    def test_enrty(self):
        v=Vehicle(1,'car')
        level_1=Level({'car':2,'bike':2,'cycle':1},2,level=[])
        level_2=Level({'car':2,'bike':3},2,level=[])
        check=level_1.allocate_space()
        self.assertEqual(check,2)


    def test_vehicle_entry1(self):
        v=Vehicle(1,'car')
        level_1=Level({'car':2,'bike':2,'cycle':1},2,level=[])
        level_2=Level({'car':2,'bike':3},3,level=[])
        check=level_2.allocate_space()
        self.assertNotEqual(check,None)

    def test_available_space(self):
        v=Vehicle(1,'car')
        level_1=Level({'car':2,'bike':2,'cycle':1},2,level=[])
        level_2=Level({'car':2,'bike':3},3,level=[])
        check=level_1.get_release_space(1)
        self.assertEqual(check,2)

    def test_available_space1(self):
        v=Vehicle(1,'car')
        level_1=Level({'car':2,'bike':2,'cycle':1},2,level=[])
        level_2=Level({'car':2,'bike':3},3,level=[])
        check=level_2.get_release_space(-1)
        self.assertEqual(check,0)

    def test_vehicle_slot(self):
        v=Vehicle(1,'car')
        level_1=Level({'car':2,'bike':2,'cycle':1},2,level=[])
        level_2=Level({'car':2,'bike':3},3,level=[])
        check=level_1.park_vehicle('train','v1')
        self.assertEqual(check,None)

        
        
if __name__=='__main__':
    unittest.main()
        
        
        
    
