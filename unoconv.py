#!/usr/bin/env python3

import sys,os,argparse,re

#convert to pdf using unoconv
def convert2pdf(outputFilePath, inputFilePath):
    for root,dirs,filenames in os.walk(inputFilePath):
        for filename in filenames:
            if str(filename).endswith("docx"):
                inputFile = inputFilePath + filename
                os.system("unoconv -f pdf -o %s %s" % (outputFilePath, inputFile))
    
        #filenameRegex = re.compile(r'.*\.pdf')
        #fileNeedded = filenameRegex.findall(filename)

           # inputFile = inputFilePath + filenames 
           # os.system("unoconv -f pdf -o %s %s" % (outputFilePath, inputFile))

#opts,args = getopt.getopt(sys.argv[1:], "hio:", ["help", "output="])
parse = argparse.ArgumentParser(description="test!!")
parse.add_argument("-i", help="path to inputfile")
parse.add_argument("-o", help="path to outputfile")
args = parse.parse_args()
print(args)
inputFilePath = args.i
outputFilePath = args.o

convert2pdf(outputFilePath, inputFilePath)


