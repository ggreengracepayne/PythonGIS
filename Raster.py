#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      f006hj8
#
# Created:     28/04/2025
# Copyright:   (c) f006hj8 2025
# Licence:     <your licence>
#------------------------------------------------------------------------------
#This script uses map algebra to find values in an
#elevation raster greater than 3500 (meters).

import arcpy
from arcpy.sa import *

#Specify the input raster
inRaster = "D:/info/Lesson1/foxlake"
cutoffElevation = 3500

#Check out the Spatial Analyst extension
arcpy.CheckOutExtension("Spatial")

# Make a map algebra expression and save the resulting raster
outRaster = Raster(inRaster) > cutoffElevation
#outRaster.save("D:/info/Lesson1/foxlake/foxlake_hi_10") #Save the Raster

#Make a new raster and call it outRaster. Do this by taking all the cells
#of the raster dataset at the path of inRaster that are greater than the number
#I assigned to the variable cutoffElevation.

# Check in the Spatial Analyst extension now that you're done
print(arcpy.CheckInExtension("Spatial"))

