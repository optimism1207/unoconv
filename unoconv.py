#!/usr/bin/env python3

import sys,os,argparse

#filename split
def fileNameSplit(targetFile):
    fileArgs = targetFile.split(".")
    return fileArgs
 
#for convert and printing 
def convertCommon(neededFileName, fileType, outputPath, inputPath):
    fileValue = fileNameSplit(neededFileName)
    os.system("unoconv -f %s -o %s %s" % (fileType, outputPath, inputPath))
    if os.path.exists(outputPath + fileValue[0] + "." + fileType):
        print("%s ====> %s.%s Success!" % (neededFileName, fileValue[0], fileType))
    else:
        print("%s convert failed!" % (neededFileName))

#find target file and call convertCommon
def findTargetFile(outputFilePath, inputFilePath):
    if os.path.isfile(inputFilePath): #判断输入是不是文件
        filename = os.path.basename(inputFilePath)
        fileValue = fileNameSplit(filename)
        if fileValue[1] in convertRelation and fileType == convertRelation[fileValue[1]]:      
            convertCommon(filename, fileType, outputFilePath, inputFilePath) 
    else:
        for root,dirs,filenames in os.walk(inputFilePath):
            for filename in filenames:
                fileValue = fileNameSplit(filename)
                if fileValue[1] in convertRelation and fileType == convertRelation[fileValue[1]]: 
                    inputFile = inputFilePath + filename
                    convertCommon(filename, fileType, outputFilePath, inputFile)

os.system("unoconv --listener ")

convertRelation={'doc':'pdf', 'docx':'pdf', 'pdf':'doc', 'pdf':'docx', 'jpg':'png', 'png':'jpg', 'txt':'csv', 'csv':'txt'}
    
parse = argparse.ArgumentParser(description="test!!")

parse.add_argument("-f", help="filetype needed to convert")
parse.add_argument("-i", help="path to inputfile")
parse.add_argument("-o", help="path to outputfile")

args = parse.parse_args()
fileType = args.f
inputFilePath = args.i
outputFilePath = args.o

if inputFilePath != None and outputFilePath != None: #输入输出路径不为空
    if not outputFilePath.endswith("/"): #输出路径没"/",自动加"/"
        outputFilePath = outputFilePath + "/"
    if os.path.isdir(inputFilePath) and (not inputFilePath.endswith("/")): #输入为路径并且没"/",自动加"/"
        inputFilePath = inputFilePath + "/"
    findTargetFile(outputFilePath, inputFilePath)
else:
    print("Input and output file path needed.")


