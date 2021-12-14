import sys
import os
import pathlib
import math
import minecart
from PyPDF2 import PdfFileReader

def getSize(sizeMatrix):
        """
        Returns matrix with sizes from inches recalculated to mm.
        It assumes that pdf.getPage(0).mediaBox returns always same matrix
        """
        widthInMm = sizeMatrix[(2)]*0.352
        heightInMm = sizeMatrix[(3)]*0.352
        mmSizes = []
        #mmSizes = list(mmSizes)
        mmSizes.append(widthInMm)
        mmSizes.append(heightInMm)
        return mmSizes

def getNoOfA4Formats(mmSizes):
        """
        Returns no. of A4 formats of a given page 
        """
        A4 = math.ceil (mmSizes[0]*mmSizes[1]/62370)
        return A4

def totalNoOfFormatsInDir(a4formats):
        sumOfA4 = 0
        for i in a4formats:
                sumOfA4 += i
        return sumOfA4 

def getFileColors(file):
        """
        returns all colors used in a pdf file - not working ...
        """
        colors = set()
        document = minecart.Document(file)
        page = document.get_page(0)
        for shape in page.shapes:
                if shape.fill:
                        colors.add(shape.fill.color.as_rgb())
        return colors
        #for color in colors: print color


path = False

if len(sys.argv) > 1:
        path = sys.argv[1]

if (path):
        listOfFiles = os.listdir(path)
else:        
        listOfFiles = os.listdir(pathlib.Path().resolve())

pathSlashed = path + "/"

print (listOfFiles)
a4formats = []

for pdfFile in listOfFiles:
        absPathFile = pathSlashed + pdfFile
        
        with open(absPathFile, 'rb') as f:
                ###getting info about colors in a file
                #colors = getFileColors(f)
                ###
                pdf = PdfFileReader(f)
                pagesNo = pdf.getNumPages()
                sizeMatrix = pdf.getPage(0).mediaBox
                mmSizes = getSize(sizeMatrix)
                #print(getNoOfA4Formats(mmSizes))
                a4formats.append(getNoOfA4Formats(mmSizes))

print (totalNoOfFormatsInDir(a4formats)) 


#print(a4formats)

#print (getSize(sizeMatrix))
#print (getNoOfA4Formats(mmSizes))
