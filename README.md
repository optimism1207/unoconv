# unoconv
Dockerfile and python-script for unoconv

First time learn to build with Dockerfile

# To build 
git clone this

cd unoconv

docker build -t unoconv .

# To use
docker run -v sourcedir:dirindocker unoconv -i inputfilepath -o outputfilepath


