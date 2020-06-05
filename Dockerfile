FROM centos:latest

RUN yum install python36 -y

RUN python3 -m pip install --upgrade pip

RUN pip3 install --upgrade setuptools

RUN pip3 install pandas

RUN pip3 install numpy

RUN pip3 install sklearn

RUN pip3 install joblib

RUN pip3 install matplotlib