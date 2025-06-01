#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      f006hj8
#
# Created:     28/04/2025
# Copyright:   (c) f006hj8 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#This script runs the Buffer tool. The user supplies the input
#and output paths, and the buffer distance.

import arcpy
arcpy.env.overwriteOutput = True

try:
     # Get the input parameters for the Buffer tool
     inPath = arcpy.GetParameterAsText(0)
     outPath = arcpy.GetParameterAsText(1)
     bufferDistance = arcpy.GetParameterAsText(2)

#Gets the specified parameter as a text string by its index position from the list of parameters.

     # Run the Buffer tool
     arcpy.Buffer_analysis(inPath, outPath, bufferDistance)

     # Report a success message
     arcpy.AddMessage("All done!")

except:
     # Report an error messages
     arcpy.AddError("Could not complete the buffer")

     # Report any error messages that the Buffer tool might have generated
     arcpy.AddMessage(arcpy.GetMessages())