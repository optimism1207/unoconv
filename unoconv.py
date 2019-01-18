#!/usr/bin/env python3

import sys,os,argparse,re

#convert to pdf using unoconv
def convert2pdf(outputFilePath, inputFilePath):
    for root,dirs,filenames in os.walk(inputFilePath):
        for filename in filenames:
            if str(filename).endswith("docx") or str(filename).endswith("doc"):
                inputFile = inputFilePath + filename
                if str(filename).endswith("docx"):
                    os.system("unoconv -f pdf -o %s %s" % (outputFilePath, inputFile))
                    print("%s convert to %s.pdf" % (str(filename), str(filename)[:-5]))
                else:
                    os.system("unoconv -f pdf -o %s %s" % (outputFilePath, inputFile))
                    print("%s convert to %s.pdf" % (str(filename), str(filename)[:-4]))

os.system("unoconv --listener")
    
arse = argparse.ArgumentParser(description="test!!")
parse.add_argument("-i", help="path to inputfile")
parse.add_argument("-o", help="path to outputfile")
args = parse.parse_args()
inputFilePath = args.i
outputFilePath = args.o

convert2pdf(outputFilePath, inputFilePath)


