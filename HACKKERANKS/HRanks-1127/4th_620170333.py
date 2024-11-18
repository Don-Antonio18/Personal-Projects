def mkAircraft(iD, fuelLvl):
    #create aircraft dictionary
    aircraft = {"id": iD, "fuel": fuelLvl}
    return aircraft

def getiD(aircraft):
    #retrives id val from dict
    #* return aircraft['id'] OR: 
    return aircraft.get("id")

def getFueLvl(aircraft):
    #retrives fuel val from dict
    return aircraft.get("fuel")

def mkPriorityQueue():
    #initialize an empty queue
    return []

def getContents(Priority_Queue):
#returns all elmnts in queue
    return Priority_Queue[:]

def isPriQueueEmpty(Queue_Contents):
    #check if queue is empty --> returns (true/false)
    return Queue_Contents == []

def getPosition(aircraft, Queue_Contents):
    #enumerate loop thru list n assigns index for each item
    # hence, two iterables needed. 1 for index, one for plane object
    for pos, plane in enumerate(Queue_Contents):
        if getiD(aircraft) == getiD(Queue_Contents[plane]):
            return pos
        
    else: return None


#! ALTERNATELY:

def getPosition2(aircraft, Queue_Contents):
    #enumerate loop thru  n assigns index for each item
    # hence, two iterables needed. 1 for index, one for plane object
    for plane_position, queued_plane in enumerate(Queue_Contents):
        #! Ask chatgpt how code is able to retrieve dict val from queued_plane
        if queued_plane["id"] == aircraft["id"]:
            return plane_position
        
    else: return None


def addAirCraftToQueue(Priority_Queue, aircraft):
    inserted = False
    if isPriQueueEmpty(Priority_Queue) == False:
        for index in range(len(Priority_Queue)):
            if aircraft["fuel"] < Priority_Queue[index]["fuel"]:
                Priority_Queue.insert(index, aircraft)
                inserted = True
                break
        if not inserted:
                Priority_Queue.append(aircraft)
            

def popAirCraftFromQueue(Priority_Queue):
    #check to see if queue is empty:
    if isPriQueueEmpty(Priority_Queue) ==  False:
        # removes first index value, aka front of queue
        return Priority_Queue.pop(0)
    return []

# if __name__ == '__main__':
#     c = int(input().strip())  # Number of commands
#     priQueue = mkPriorityQueue()  # Initialize priority queue

#     for _ in range(c):
#         command = input().strip().split()  # Parse the command
#         if command[0] == "add":
#             iD = command[1]
#             fuelLvl = int(command[2])
#             aircraft = mkAircraft(iD, fuelLvl)
#             addAirCraftToQueue(priQueue, aircraft)
#         elif command[0] == "land":
#             landedAircraft = popAirCraftFromQueue(priQueue)
#             if landedAircraft:
#                 print(getiD(landedAircraft))  #
