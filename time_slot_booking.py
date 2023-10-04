'''
NOTE:
IT JUST WORKS AND I DONT EVEN KNOW WHY. I DONT KNOW WHY IT ONLY WORKED PROPERLY WHEN I REMOVED THE BLANK ELEMENT AND ADDED NAME IT WOULDNT WORK OTHERWISE IM NOT CHANGING THIS OMG
'''

#classroom booking
#import libraries and creating variables
from tabulate import tabulate
time_slot1 = ['', '08.30 - 09.50', 'Not booked', '(1)']
time_slot2 = ['', '10.15 - 11.30', 'Not booked', '(2)']
time_slot3 = ['', '11.30 - 12.50', 'Not booked', '(3)']
time_slot4 = ['', '13.30 - 14.40', 'Not booked', '(4)']
time_slot5 = ['', '14.40 - 15.50', 'Not booked', '(5)']
time_booking = [time_slot1, time_slot2, time_slot3, time_slot4, time_slot5]

#schedule table
schedule = [['Name', 'Time','Status'],
         time_slot1,
         time_slot2,
         time_slot3,
         time_slot4,
         time_slot5]

#code
i = 0
while i<5:
    print('Classroom booking schedule','\n',tabulate(schedule))
    chosen_slot = input('Choose an available time slot by entering number adjacent to it: ').strip()
    if time_booking[int(chosen_slot)-1][2] == 'Booked':
        print("Error, time slot is already booked. Please choose another slot")
    
    else:
        name = input("Enter name: ")
        
        if chosen_slot == '1':
            time_slot1[2] = 'Booked'
            time_slot1.pop(0)
            time_slot1.insert(0,name)
            i += 1
            
        elif chosen_slot == '2':
            time_slot2[2] = 'Booked'
            time_slot2[0] = name
            time_slot2.pop(0)
            time_slot2.insert(0,name)
            i += 1
            
        elif chosen_slot == '3':
            time_slot3[2] = 'Booked'
            time_slot3[0] = name
            time_slot3.pop(0)
            time_slot3.insert(0,name)
            i += 1

        elif chosen_slot == '4':
            time_slot4[2] = 'Booked'
            time_slot4[0] = name
            time_slot4.pop(0)
            time_slot4.insert(0,name)
            i += 1

        elif chosen_slot == '5':
            time_slot5[2] = 'Booked'
            time_slot5[0] = name
            time_slot5.pop(0)
            time_slot5.insert(0,name)
            i += 1

        else:
            print("Error, please choose another time slot")


print('Classroom booking schedule','\n',tabulate(schedule))
