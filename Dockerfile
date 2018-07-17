FROM ubuntu:xenial
MAINTAINER Jon Howell
COPY phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin
RUN apt-get update && \
    apt-get -y install \
    python python-pip fontconfig
RUN pip install selenium
VOLUME /tmp
ENV SCREENSHOT_URL=slipsnet.com
COPY screenshot.py /opt
ENTRYPOINT python  /opt/screenshot.py -s ${SCREENSHOT_URL}
