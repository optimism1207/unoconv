from centos:latest

MAINTAINER GX

ENV REFRESHED_AT 2019-01-17

RUN yum install -y unoconv libreoffice-langpack-zh-Hans gcc make zlib zlib-devel libffi-devel \
                    gcc-c++ bzip2 

COPY ./Python-3.7.2.tgz /tmp

WORKDIR /tmp

RUN tar zxvf Python-3.7.2.tgz 

WORKDIR /tmp/Python-3.7.2

RUN ./configure && make && make install

RUN rm -rf /tmp/*

COPY ./unoconv.py /usr/local/bin/unoconv.py

RUN chmod +x /usr/local/bin/unoconv.py

ENV PATH=/usr/local/bin/unoconv.py:$PATH

ENTRYPOINT ["unoconv.py"] 

CMD ["-h"]

