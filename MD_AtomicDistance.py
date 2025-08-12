start_time = time.time()

#coordinateFile = open("/Users/amiromranpoor/Downloads/PhD-data/Tim_MD_Bulk/Output/md.xyz", "r")
coordinateFile = open("MD_trajectory.xyz", "r")

stepNumber = 0
#totalSteps = 500
coordinates = []
for lineIndex, line in enumerate(coordinateFile, start=0):
    if lineIndex == 0:
        atomNumber = int(line.rstrip())
        step = []
        coordinates.append(step)
    if (lineIndex - stepNumber * (atomNumber + 2)) > 1 and (lineIndex - stepNumber * (atomNumber + 2)) < (atomNumber + 2):
            elements = line.split()
            atomIndex = lineIndex - stepNumber * (atomNumber + 2) - 2
            for elementIndex, element in enumerate(elements, start=0):
                atom = []
                coordinates[stepNumber].append(atom)
                if elementIndex == 0:
                    coordinates[stepNumber][atomIndex].append(element)
                else:
                    coordinates[stepNumber][atomIndex].append(float(element))
    if (lineIndex - stepNumber * (atomNumber + 2) == (atomNumber + 2)):
        step = []
        coordinates.append(step)
        stepNumber += 1
        # if stepNumber == totalSteps:
        #     break
coordinateFile.close()
print ("Number of steps=", stepNumber)
#print (coordinates[0][10])

distance = []
#centerOfMassY = []
#centerOfMassZ = []
#mass = 0

#print (coordinates[0][150])
#define a and b
a=4024
b=331
print("Distance between",coordinates[0][a][0],"and", coordinates[0][b][0] )
print("Distance between",a,"and", b )
#for i in range(stepNumber):
#for i in range(2000):
for i in range(0, 1000, 1):

    C_X = 0
    C_Y = 0
    C_Z = 0
    O_X = 0
    O_Y = 0
    O_Z = 0
    #mass = 0
    Distance = 0
    #for j in range(atomNumber):
        #if coordinates[i][atomNumber-9][0] == "C":
         #   if coordinates[i][atomNumber-1][0] == "O":
    C_X = coordinates[i][a][1]
    C_Y = coordinates[i][a][2]
    C_Z = coordinates[i][a][3]
               # print( coordinates[i][atomNumber-9][0],coordinates[i][atomNumber-9][1],coordinates[i][atomNumber-9][2],coordinates[i][atomNumber-9][3])

    O_X =  coordinates[i][b][1]
    O_Y =  coordinates[i][b][2]
    O_Z =  coordinates[i][b][3]

    Distance = math.sqrt( ((C_X - O_X)**2)+((C_Y - O_Y)**2)+((C_Z - O_Z)**2) )
           # mass += 16.0
        #elif coordinates[i][j][0] == "H":
            #coMX += coordinates[i][j][1]
           # coMY += coordinates[i][j][2]
            #coMZ += coordinates[i][j][3]
            #mass += 1.0
    distance.append(Distance)
    #centerOfMassY.append(coMY/mass)
    #centerOfMassZ.append(coMZ/mass)

# xdistance = (coordinates[0][0][1] - coordinates[1][0][1])**2
# ydistance = (coordinates[0][0][2]-coordinates[1][0][2])**2
# zdistance = (coordinates[0][0][3]-coordinates[1][0][3])**2
# distance = math.sqrt(xdistance + ydistance + zdistance)
# print distance

# result = open("data.dat", "w")
# for i in range(stepNumber):
#     result.write(str(coordinates[i][0][1]) + " " + str(coordinates[i][0][2]) + "\n")
# result.close()

#result = open("Distance.dat", "w")
#for i in range(stepNumber):
#    result.write(str(i*0.5) + " " + str(distance[i]) + "\n")
#result.close()

elapsed_time = time.time() - start_time
print ('Elapsed time = %f seconds ' % elapsed_time)
