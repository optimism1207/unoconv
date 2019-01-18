# unoconv
Dockerfile and python-script for unoconv
first time learn to build with Dockerfile
# how to build 

git clone this

cd unoconv

docker build -t unoconv .

docker run -v sourcedir:dirindocker unoconv -i inputfilepath -o outputfilepath


