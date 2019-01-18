#!/usr/bin/env python3

import sys,os,argparse

#for convert and printing 
def convertCommon(neededFileName, outputPath, inputPath):
    if str(neededFileName).endswith("docx"):
        os.system("unoconv -f pdf -o %s %s" % (outputPath, inputPath))
        if os.path.exists(outputPath + str(neededFileName)[:-5] + ".pdf"):
            print("%s ====> %s.pdf Success!" % (str(neededFileName), str(neededFileName)[:-5]))
        else:
            print("%s convert failed!" % (str(neededFileName)))
    else:
        os.system("unoconv -f pdf -o %s %s" % (outputPath, inputPath))
        if os.path.exits(outputPath + str(neededFileName)[:-5] + ".pdf"):
            print("%s ====> %s.pdf Success!" % (str(neededFileName), str(neededFileName)[:-4]))
        else:
            print("%s convert failed!" % (str(neededFileName)))

#convert to pdf using unoconv
def convert2pdf(outputFilePath, inputFilePath):
    if os.path.isfile(inputFilePath):
        convertCommon(os.path.basename(inputFilePath), outputFilePath, inputFilePath) 
    elif os.path.isdir(inputFilePath) and ( not inputFilePath.endswith("/") ):
        inputFilePath = inputFilePath + "/" 
        for root,dirs,filenames in os.walk(inputFilePath):
            for filename in filenames:
                if str(filename).endswith("docx") or str(filename).endswith("doc"):
                    inputFile = inputFilePath + filename
                    convertCommon(filename, outputFilePath, inputFile)
    else:
        for root,dirs,filenames in os.walk(inputFilePath):
            for filename in filenames:
                if str(filename).endswith("docx") or str(filename).endswith("doc"):
                    inputFile = inputFilePath + filename
                    convertCommon(filename, outputFilePath, inputFile)

os.system("unoconv --listener")
    
parse = argparse.ArgumentParser(description="test!!")
parse.add_argument("-i", help="path to inputfile")
parse.add_argument("-o", help="path to outputfile")
args = parse.parse_args()
inputFilePath = args.i
outputFilePath = args.o
if not outputFilePath.endswith("/"):
    outputFilePath = outputFilePath + "/"

convert2pdf(outputFilePath, inputFilePath)


