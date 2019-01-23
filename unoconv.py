#!/usr/bin/env python3

import sys,os,argparse

#filename split
def fileNameSplit(targetFile):
    fileArgs = targetFile.split(".")
    if len(fileArgs) == 1:
        fileArgs.append("placeHolder")
    return fileArgs
 
#for convert and printing 
def convertCommon(neededFileName, fileType, outputPath, inputPath):
    fileValue = fileNameSplit(neededFileName)
    if outputPath == None:
        os.system("unoconv -f %s %s" % (fileType, inputPath))
        (currentPath, currentFile) = os.path.split(inputPath)
        if os.path.exists(currentPath + "/" +  fileValue[0] + "." + fileType):
            print("%s ====> %s.%s Success!" % (neededFileName, fileValue[0], fileType))
        else:
            print("%s convert failed!" % (neededFileName))
    else:
        os.system("unoconv -f %s -o %s %s" % (fileType, outputPath, inputPath))
        if os.path.exists(outputPath + fileValue[0] + "." + fileType):
            print("%s ====> %s.%s Success!" % (neededFileName, fileValue[0], fileType))
        else:
            print("%s convert failed!" % (neededFileName))

#find target file and call convertCommon
def findTargetFile(outputFilePath, inputFilePath, depth=1):
    if os.path.isfile(inputFilePath): #判断输入是不是文件
        filename = os.path.basename(inputFilePath)
        fileValue = fileNameSplit(filename)
        if fileValue[1] in convertRelation and fileType == convertRelation.get(fileValue[1], 'nokey'):      
            convertCommon(filename, fileType, outputFilePath, inputFilePath) 
    else:
        neededDepth = len(inputFilePath.split(os.path.sep)) + depth - 1
        for dirpath,dirs,filenames in os.walk(inputFilePath):
            for filename in filenames:
                currentDepth = len(os.path.join(dirpath, filename).split(os.path.sep))
                if currentDepth <= neededDepth and not filename.startswith("."):
                    fileValue = fileNameSplit(filename)
                    if fileValue[1] in convertRelation and fileType == convertRelation.get(fileValue[1], 'nokey'): 
                        inputFile = os.path.join(dirpath, filename)
                        convertCommon(filename, fileType, outputFilePath, inputFile)

os.system("unoconv --listener ")

convertRelation={'doc':'pdf', 'docx':'pdf', 'pdf':'doc', 'pdf':'docx', 'jpg':'png', 'png':'jpg', 'txt':'csv', 'csv':'txt'}
    
parse = argparse.ArgumentParser(description="test!!")

parse.add_argument("-f", help="filetype needed to convert")
parse.add_argument("-i", help="path to inputfile")
parse.add_argument("-o", help="path to outputfile")
parse.add_argument("--depth", nargs='?', help="path depth, default=1")

args = parse.parse_args()
fileType = args.f
inputFilePath = args.i
outputFilePath = args.o
depth = int(args.depth)

if inputFilePath != None: #输入路径不为空
    if outputFilePath != None and not outputFilePath.endswith("/"): #输出路径没"/",自动加"/"
        outputFilePath = outputFilePath + "/"
    if os.path.isdir(inputFilePath) and (not inputFilePath.endswith("/")): #输入为路径并且没"/",自动加"/"
        inputFilePath = inputFilePath + "/"
    findTargetFile(outputFilePath, inputFilePath, depth)
else:
    print("Input and output file path needed.")


