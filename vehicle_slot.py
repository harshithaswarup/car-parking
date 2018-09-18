import datetime
class Vehicle(object):
    def __init__(self,vehicle_number,vehicle_type1):
        self.vehicle_number=vehicle_number
        self.vehicle_type1=vehicle_type1
        
class Parking(object):
    
    def get_vehicle_type(self,get_type):
        vehicle_type=get_type
        return vehicle_type

    def check_vehicle_entry(self,vehicle_type,allowed_vehicle={'car':2,'bike':2}):
        for keys in allowed_vehicle:
            if(vehicle_type==keys):
                return True
            else:
                return False
        
    def get_vehicle_ID(self,get_ID):
        vehicle_ID=get_ID
        return vehicle_ID


    def get_entry_time(self):
        entry_time=datetime.datetime.now()
        return entry_time


class Process:
    parking_slot=[]
    def __init__(self,allowed_vehicle,level=[]):
        self.level=level
        self.allowed_vehicle=allowed_vehicle

    def park_vehicle(self,vehicle_type,vehicle_ID):
        parking=Parking()
        parking.get_vehicle_type(vehicle_type)
        parking.check_vehicle_entry(vehicle_type,allowed_vehicle={'car':2,'bike':2})
        parking.get_vehicle_ID(vehicle_ID)
        parking.get_entry_time
        for keys in self.allowed_vehicle:
            if(vehicle_type==keys):
                self.level.append(vehicle_ID)
                self.parking_slot.append(vehicle_type)


    def get_vehicle_count(self):
        vehicle_count=sum(map(lambda x:1,self.level))
        return vehicle_count


    def get_vehicle(self,vehicle_ID):
        self.level.remove(str(vehicle_ID))

class Level(Process):
    def __init__(self,allowed_vehicle,level_capacity,level=[]):
        Process.__init__(self,allowed_vehicle,level=[])
        self.level_capacity=level_capacity


    def allocate_space(self):
        available_space=(self.level_capacity)-(len(self.level))
        return available_space

    def get_release_space(self,available_space):
        available_space+=1
        return available_space


if __name__=='__main__':
    
    process=True

    v=Vehicle(1,'car')
    level_1=Level({'car':2,'bike':2,'cycle':1},4,level=[])
    level_2=Level({'car':2,'bike':2},4,level=[])

    while process:
        print('press 1 to Park')
        print('press 2 to get ur car')

        choice=int(input("Enter your choice:"))
    
        if(choice==1):
            parking = Parking()
            vehicle_type=raw_input("Enter the type of vehicle")
            parking.get_vehicle_type(vehicle_type)
            parking.check_vehicle_entry(vehicle_type,allowed_vehicle={'car':2,'bike':2})
            if vehicle_type in level_1.allowed_vehicle:
                print "Allowed to park"
            else:
                print "Not Allowed"
            vehicle_ID=raw_input("Enter the vehicle ID:")
            parking.get_vehicle_ID(vehicle_ID)
            entry_time=parking.get_entry_time()
            print entry_time
            vehicle_count=level_1.get_vehicle_count()
            print vehicle_count
            vehicle_count=level_2.get_vehicle_count()
            print vehicle_count
            if(len(level_1.level)!= level_1.level_capacity):
            #if(vehicle_count!= level_1.level_capacity):
                level_1.park_vehicle(vehicle_type,vehicle_ID)
                print "Filled slots at L1:",level_1.level
                print "----"
            elif(len(level_2.level)!=level_2.level_capacity):
            #elif(vehicle_count!= level_2.level_capacity):
                level_2.park_vehicle(vehicle_type,vehicle_ID)
                print "Filled slots at L2:",level_2.level
                print "-----"
            available_space=level_1.allocate_space()
            print "space at Level 1:",available_space
            print "----"
            available_space=level_2.allocate_space()
            print "space at Level 2:",available_space
            print "----"
        
        elif(choice==2):
            level_list=['1','2']
            select_level=raw_input("Enter the level:")
            vehicle_ID=raw_input("Enter the vehicle ID:")
            if(select_level==level_list[0]):
                level_1.get_vehicle(vehicle_ID) 
                print "Filled slots at level_1:",level_1.level
                available_space=level_1.get_release_space(available_space)
                print "L1:available space",available_space
                print "The slots that is available to park:",vehicle_ID
                print "-----"
            elif(select_level==level_list[1]):
                level_2.get_vehicle(vehicle_ID) 
                print "Filled slots at level_2:",level_2.level
                available_space=level_2.get_release_space(available_space)
                print "L2:available space",available_space
                print "The slots that got cleared:",vehicle_ID

        if(len(level_1.level)== level_1.level_capacity and len(level_2.level)==level_2.level_capacity):
            process=False

