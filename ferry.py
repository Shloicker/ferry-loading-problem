def printSol(S, c, O):
    # This procedure prints details of a solution to the screen.
    print("\nSOLUTION")
    for i in range(len(S)):
        print("Lane-" + str(i) + " = " + str(S[i]) + " (" + str(sum(S[i])) + " cm of " + str(c) + " cm used)")
    print("Overflow = " + str(O))
    print("Total length in overflow = " + str(sum(O)) + " cm")
              
def getFirstLane(carLen, S, L):
    # Find functions returns the number of the first suitable lane for the current car. 
    # It returns -1 is there is no suitable lane
    for i in range(len(S)):
        if sum(S[i]) + carLen <= c:
            return i
    #If we are here, no lane is suitable.
    return -1

# Main Program -------------------------------------------------------------
# First read in the problem file. All car lengths are put into the list L
L = []
with open("input.txt","r") as f:
    c = int(f.readline())
    numLanes = int(f.readline())
    for line in f:
        L.append(int(line))

# Having read in the file, output some information to the screen
print("Number of vehicles           = " + str(len(L)))
print("Total length of vehicles     = " + str(sum(L)) + " cm")
print("Number of lanes              = " + str(numLanes))
print("Capacity per lane            = " + str(c) + " cm")
print("List of all vehicle lengths  = " + str(L))

# Now declare the data structures used for storing the vehicles in each lane
# and the vehicles in the overflow
S = [[] for i in range(numLanes)]
O = []

# Here is the basic algorithm. It takes each vehicle in turn and places it
# into the first lane observed to have sufficient capacity. When no suitable 
# lane exists, the vehcile is put into the overflow list instead
for i in range(len(L)):
    carLen = L[i]
    lane = getFirstLane(carLen, S, c)
    if lane != -1:
        S[lane].append(carLen)
    else:
        O.append(carLen)

# Print details of the solution to the screen
printSol(S, c, O)
