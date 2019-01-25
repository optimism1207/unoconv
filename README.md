# unoconv
Dockerfile and python-script for unoconv

First time learn to build with Dockerfile &

A coding practice in python learning

# To build 
git clone this

cd unoconv

docker build -t unoconv .

# To use
docker run -v sourcedir:dirindocker unoconv -f filetype -i inputfilepath -o outputfilepath(可选，默认和源文件同目录) --depth(可选，默认1)

批量转换文件夹中的文档
已测试  docx，doc ==> pdf
        jpg <==> png

dockerfile里把ENTRYPOINT 设成/usr/bin/unoconv 直接用也可以
