import random 
import time

# Emergencies: 
# Regular 0
# Disabled/Pregrnant/etc 1
# Emergency (injured/heart attack/etc) 2

class Patient:
    def __init__(self, ticket, emergency):
        self.ticket = ticket 
        self.emergency = emergency 

    def __str__(self):
        return "Ticket: " + str(self.ticket) + " with priority: " + str(self.emergency)


waiting_list = []
ticket = 1


while True:
    action = random.randint(1, 100)
    if action > 30:
        type = random.randint(1, 100)
        if type >= 20:
            print("Regular patient", ticket)
            waiting_list.append(Patient(ticket, 0))
        elif type >= 5:
            print("Disabled patient", ticket)
            waiting_list.append(Patient(ticket, 1))
        else:
            print("Emergency patient", ticket)
            waiting_list.append(Patient(ticket, 2))
        ticket += 1
    else:
        # Decide who's next
        if len(waiting_list) == 0:
            print("Front Desk: No patients waiting")
        else: 
            waiting_list.sort(key=lambda x: x.emergency, reverse=True)
            next = waiting_list.pop(0)
            print("Front Desk: ", next, "is examined")
    # delay for a while
    time.sleep(random.randint(2,5))