# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 18:36:56 2019

@author: c1896292
"""
import random
# used to check how many Trucks and how many small cars are in the random que (for checking end points) 
def checkRandomCars(vehicleQue):
    x=0
    for i in range(len(vehicleQue)):
        if vehicleQue[i]>600:
            x = x +1
    print("number of trucks: " + str(x))
    x=0
    for i in range(len(vehicleQue)):
        if vehicleQue[i]<400:
            x = x +1
    print("number of small cars: "+ str(x))
    

#calculates a uniform distrebution based on the max and min vehicle lengths specified by problem
def uniformDist(a , b):
    a = int(a)
    b = int(b)
    length = a + (b-a)*random.random()
    return length

#calcultes a cumulative probability of a matrix density function of a matrix
def cdf (vehicles):
    dist = []
    for i in range(len(vehicles)):
        dist.append(vehicles[i]/sum(vehicles))
        if i >0: 
            dist [i] = dist[i]+dist[i-1]
    return dist

# Generates a que of 500 vehicles maintaining the same number of each type of vehicle specified by the problem
#All vehicle types are uniformly distrebuted with maximum and minimums specified
def get_Q( problemSpecs):
    vehicles = []
    for i in range(len(problemSpecs)): 
        vehicles.append(int(problemSpecs[i].get("numVehicles"))) #makes an array containing amounts of different types of vehicles
    que = []   
    for j in range (sum(vehicles)): 
        x = random.random()
        for i in range(len(problemSpecs)): 
            if sum(vehicles) != 0:
                cdfDist = cdf (vehicles) #calculates a cdf of different vehicle types based on the current number of vehicles
                if i == 0 and x < cdfDist [i]:
                    vehicles[i] = vehicles[i] - 1
                    que.append(uniformDist(problemSpecs[i].get("minLength"), problemSpecs[i].get("maxLength"))) #gets the minimum and maximum length of the smallest vehicle, creates a uniformly distrebuted length, and adds this to a list of lengths
                elif x < cdfDist[i] and x > cdfDist[i-1]:
                    vehicles [i] = vehicles[i]-1 
                    que.append(uniformDist(problemSpecs[i].get("minLength"), problemSpecs[i].get("maxLength")))#gets the minimum and maximum length of the vehicle which correlates to random variable x in the cdf, creates a uniformly distrebuted length, and adds this to a list of lengths
    return que    


# creating an array of dictionaries containing:
# (number of vehicles of a certain type, minimum length of vehicle, maximum length of vehicle) for each vehicle type
problemSpec = []
with open ("problemSpecs.txt", "r") as f: #problem specs is a txt file that has number of vehicle type, maximum car length and minimum car length for each type vehicle
    for line in f:
        specifacations = line.split(",")
        specs = {"numVehicles": specifacations[0], "minLength": specifacations[1], "maxLength": specifacations[2]}
        problemSpec.append(specs)
           
vehicleQue = get_Q(problemSpec)

#checking the que is as required
print ("maximum length of vehicle: " + str(max(vehicleQue)))
print ("minimum length of vehicle: " + str(min(vehicleQue)))
checkRandomCars(vehicleQue)
print(vehicleQue)



            
            