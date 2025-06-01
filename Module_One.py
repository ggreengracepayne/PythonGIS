#-------------------------------------------------------------------------------
# Name:        Data in Python
# Purpose:
#
# Author:      f006hj8
#
# Created:     05/05/2025
# Copyright:   (c) f006hj8 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Spatial Reference
import arcpy

#Opens a feature class from a geodatabase and prints the spatial reference
featureClass = "D:/info/Lesson1/USA.gdb/Boundaries"

#Describe the feature class and get its spatial reference
desc = arcpy.Describe(featureClass)
spatialRef = desc.spatialReference

#Print the spatial reference name
print (spatialRef.Name)


#Lists - 2.1.1
suits = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
values = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']

#Indexing syntax
print (suits[0])
print (values[12])

#Sorting
suits.sort()
print (suits)
suits.reverse()
print (suits)

#Combining lists
listOne = [101,102,103]
listTwo = [104,105,106]
listThree = listOne + listTwo #Appending the list, not actually adding
print (listThree)
listThree.reverse()
print(listThree)

#Inserting items
listThree += [107] #listThree += [107] is a shortened form of saying listThree = listThree + [107]
print (listThree)

listThree.append(108)
print (listThree)

#If you need to insert some items in the middle of the list, you can use the insert() method:
listThree.insert(4, 999) #0,1,2,3, 4 ...
print (listThree)

#Length of list
myList = [4,9,12,3,56,133,27,3]
print (len(myList))

#2.1.2 Loops
for name in ["Carter", "Reagan", "Bush"]:
    print (name + " was a U.S. president.")

for name in ["Grace", "Sam", "Ella"]:
    print(name + " is awesome.")

x = 2
multipliers = [1,2,3,4]
for num in multipliers:
     print (x * num)

x = 2
for num in range(1,18):
     print (x * num)

#While loops
x = 0
while x < 18:
      print (x * 2)
      x += 1 #Stops when x = 17

#Nesting loops - one loop inside another
suits = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
values = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
for suit in suits:
      for value in values:
          print (str(value) + " of " + str(suit))

colors = ['Green', 'Pink', 'White', 'Yellow']
peoples = ['Grace', 'Ella', 'Sam', 'Rowan']
for color in colors:
        for people in peoples:
            print(str(people) + " likes " + str(color))


#Looping GIS Models

import arcpy

try:
    arcpy.env.workspace = "D:/info/Lesson2"

    # List the feature classes in the Lesson 2 folder
    fcList = arcpy.ListFeatureClasses()

    # Loop through the list and copy the feature classes to the Lesson 2 PracticeData folder
    for featureClass in fcList:
        arcpy.CopyFeatures_management(featureClass, "D:/info/Lesson2/PracticeData/" + featureClass) #Made new folder, PracticeData

except:
    print ("Script failed to complete")
    print (arcpy.GetMessages(2))


#Looping through tables

import arcpy
inTable = "D:/info/Lesson2/CityBoundaries.shp"
inField = "NAME"

rows = arcpy.SearchCursor(inTable)

#This loop goes through each row in the table
#  and gets a requested field value

for row in rows:
    currentCity = row.getValue(inField)
    print (currentCity)


#2.1.3 Decision structures -----------------------------------------------------

#IF
x = 3
if x > 2:
    print ("Greater than two")

#IF - ELSE
x = 1
if x > 2:
        print ("Greater than two")
else:
        print ("Less than or equal to two")

#ELIF - 2 or more conditions

x = 5
if x > 2:
    print ("Greater than two")
elif x == 2 & x == 5:
    print ("Equal to two")
else:
    print ("Less than two")

#Multiple possibilities:

import random

# Choose a random school from a list and print it
schools = ["Penn State", "Michigan", "Ohio State", "Indiana"]
randomSchoolIndex = random.randrange(0,4) #Setting up the range and index
chosenSchool = schools[randomSchoolIndex]
print (chosenSchool)

# Depending on the school, print the mascot
if chosenSchool == "Penn State":
    print ("You're a Nittany Lion")
elif chosenSchool == "Michigan":
    print ("You're a Wolverine")
elif chosenSchool == "Ohio State":
    print ("You're a Buckeye")
elif chosenSchool == "Indiana":
    print ("You're a Hoosier")
else:
    print ("This program has an error")

#2.1.4 String manipulation ----------------------------
x = 0
while x < 10:
    print (x)
    x += 1

print ("You ran the loop " + str(x) + " times.") #setting x as a string instead of an integer

#Select Exercises -------------------------

#Create copies of a template shapefile

#Imagine that you're again working with the Nebraska precipitation data from
#Lesson 1 and that you want to create copies of the Precip2008Readings shapefile
#for the next 4 years after 2008 (e.g., Precip2009Readings, Precip2010Readings, etc.).
#Essentially, you want to copy the attribute schema of the 2008 shapefile, but not the data points themselves


#Creates an empty feature class in a geodatabase or a shapefile in a folder.

#Error handling
try:
    arcpy.env.workspace =  "D:/info/Lesson2" #Set up the workspace into a string variable

    template = "D:/info/Lesson1/Precip2008Readings.shp" #define our template

    for year in range(2009,2013): #for loop through 2009 to 2012
        newfile = "Precip" + str(year) + "Readings.shp"
        arcpy.CreateFeatureclass_management(arcpy.env.workspace, newfile, "POINT", template,
                                            "DISABLED", "DISABLED", template)

except:
    print (arcpy.GetMessages()) #Retrieves detailed error messages from ArcGIS


#Your task is to write a script that programmatically clips all the feature classes
#in the USA geodatabase to the Iowa state boundary. The clipped feature classes
# should be written to the Iowa geodatabase. Append "Iowa" to the beginning of all the clipped feature class names.

#Your script should be flexible enough that it could handle any number of feature
# classes in the USA geodatabase. For example, if there were 15 feature classes in
# the USA geodatabase instead of three, your final code should not need to change in any way.


#Define pathways in variable
Start = "D:/info/Lesson2/Lesson2PracticeExercise/USA.gdb"
Target = "D:/info/Lesson2/Lesson2PracticeExercise/Iowa.gdb"
Clip = "D:/info/Lesson2/Lesson2PracticeExercise/Iowa.gdb/Iowa"

#Set workspace and get feature classes

arcpy.env.workspace = Start
featureClassList = arcpy.ListFeatureClasses()

try:
#Start the for loop
    for featureClass in featureClassList:
    #Output path
        OutputFC = Target + "/Iowa" + featureClass
    #Clip
        arcpy.Clip_analysis(featureClass, Clip, OutputFC)
        arcpy.AddMessage("Wrote clipped file " + OutputFC)
        print ("Wrote clipped file " + OutputFC)

except:
    #Report if there was an error
    arcpy.AddError("Could not clip feature classes")
    print ("Could not clip feature classes")
    print (arcpy.GetMessages())

####


#Practice 1.7

#2 - Concatenate two strings
#Create a string variable called first and assign to it your first name.
#Likewise, create a string variable called last and assign to it your last name.
#Concatenate (merge) the two strings together, making sure to also include a space between them.

first = "Grace"
last = "Payne"
name = first + " " + last
print(name)

#3 - Pass a value to a script as a parameter
#For this exercise, write a script that accepts a single string value using the
#GetParameterAsText method. The value entered should be a name, and that name should be
#concatenated with the literal string "Hi, " and displayed in the console.
#Test the script from within PyScripter, entering a name (in double quotes) in the
#Command line options text box as outlined above prior to clicking the Run button.

import arcpy

name = arcpy.GetParameterAsText(0)
print ("Hi, " + name)  #Command Line Parameters, dialog box

#4 - For this exercise, use the Describe function again; this time, to determine
#the type of geometry (point, polyline or polygon) stored in a feature class.
#I won't tell you the name of the property that returns this information.
#But I will give you the hint that feature classes have this mystery property
#not because they're a type of Dataset as with the spatialReference property,
#but because they're objects of the type FeatureClass.

import arcpy

path = "D:/info/Lesson1//USA.gdb/Boundaries"

desc = arcpy.Describe(path)
shapeType = desc.shapeType

print ("The geometry type of " + path + " is " + shapeType)


#5 - Compute the sum and average of these values and output to the Console the following messages, filling in the blanks:
#The sum of these scores is ______. / Their average is ______.
score1 = 90
score2 = 80

sum = score1 + score2
average = sum/2

print("The sum of these scores is " + str(sum) + ".")
print("Their average is " + str(average) + ".")



#Project 1, part II

import arcpy
from arcpy.sa import *

#Specify the input raster
inRaster = "D:/info/Lesson1/foxlake"
outRaster = "D:/info/Lesson1/foxlake_contour"
interval = 25

# Make a map algebra expression and save the resulting raster
outRaster = Contour(inRaster, outRaster , interval)
#outRaster.save("D:/info/Lesson1/foxlake_contour")
