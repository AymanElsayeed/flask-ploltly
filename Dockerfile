FROM centos
RUN yum upgrade -y

RUN dnf install gcc openssl-devel bzip2-devel libffi-devel make wget git sqlite-devel -y
RUN yum install -y xz-devel

ENV APYTHON_VERSION 3.9.6
ENV PYTHON_CMD python3.9

RUN mkdir /project

WORKDIR /opt
RUN wget https://www.python.org/ftp/python/${APYTHON_VERSION}/Python-${APYTHON_VERSION}.tgz
RUN tar xzf Python-${APYTHON_VERSION}.tgz
RUN cd Python-${APYTHON_VERSION}
RUN /opt/Python-${APYTHON_VERSION}/configure --enable-optimizations --enable-loadable-sqlite-extensions
RUN make altinstall

WORKDIR /project

RUN pip3.9 install pipenv
RUN pip3.9 install --user --upgrade pipenv
RUN export PATH=/root/.local/bin/pipenv:$PATH

COPY requirements.txt ./
RUN pip3.9 install -r requirements.txt

MAINTAINER "Ayman Elsayeed"
LABEL python_version="3.9.6"
LABEL python_cmd="python3.9"