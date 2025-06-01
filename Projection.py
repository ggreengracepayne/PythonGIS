#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      f006hj8
#
# Created:     07/05/2025
# Copyright:   (c) f006hj8 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Project 2 ------------------------------------------------
import arcpy
import os

targetFolder = "D:/info/Lesson2"
targetProjectionFolder = "D:/info/Lesson2/Ferries.shp"
outputLocal = "D:/info/Lesson2"

arcpy.env.workspace = targetFolder

desc = arcpy.Describe(targetProjectionFolder)
target_sr = desc.spatialReference
feature_classes = arcpy.ListFeatureClasses()

try:
    for fc in feature_classes:
        rootName = fc
        if rootName.endswith(".shp"):
            rootName = rootName.replace(".shp","")

            current_sr = arcpy.Describe(fc).spatialReference
            if current_sr.name == target_sr.name:
                arcpy.AddMessage(f"Skipping {fc} - already in target projection")
            else:
                outPath = os.path.join(outputLocal, rootName + "_projected.shp")
                arcpy.Project_management(fc, outPath, target_sr)
                arcpy.AddMessage(f"Projected {fc} -> {outPath}")

except:
    arcpy.AddError("Unsuccessful")
    print("Unsuccessful")
    print(arcpy.GetMessages())



