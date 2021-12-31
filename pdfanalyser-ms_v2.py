import sys
import os
import pathlib
import math
from PyPDF2 import PdfFileReader


def getSize(sizeMatrix):
        """
        Returns matrix with sizes from inches recalculated to mm.
        It assumes that pdf.getPage(0).mediaBox returns always same matrix
        """
        #print (sizeMatrix)
        
        widthInMm = float(sizeMatrix[(2)])*0.352
        heightInMm = float(sizeMatrix[(3)])*0.352
        #exit()
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
counterOfFiles = 0
counterOfPages = 0
pageA4counter = 0
a4OrNot = 0

for pdfFile in listOfFiles:
        absPathFile = pathSlashed + pdfFile
        
        with open(absPathFile, 'rb') as f:
                counterOfFiles += 1
                pdf = PdfFileReader(f, strict=False)
                pagesNo = pdf.getNumPages()
                
                for p in range (pagesNo):       #multipage files support
                        counterOfPages += 1
                        sizeMatrix = pdf.getPage(p).mediaBox
                        mmSizes = getSize(sizeMatrix)
                        #print(getNoOfA4Formats(mmSizes))
                        a4formats.append(getNoOfA4Formats(mmSizes))
                        a4OrNot = getNoOfA4Formats(mmSizes)
                        if (a4OrNot==1):
                                pageA4counter += 1

print ("wszystkie pliki", counterOfFiles)
print ("Wszystkie strony", counterOfPages)
print ("formaty A4: ", totalNoOfFormatsInDir(a4formats)) 
print ("ilość stron A4 - mały format", pageA4counter)


#print(a4formats)

#print (getSize(sizeMatrix))
#print (getNoOfA4Formats(mmSizes))
