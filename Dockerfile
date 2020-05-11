# Docker file for the dsdircopy plugin app

FROM fnndsc/ubuntu-python3:latest
MAINTAINER fnndsc "dev@babymri.org"

ENV APPROOT="/usr/src/dsdircopy"
COPY ["dsdircopy", "${APPROOT}"]
COPY ["requirements.txt", "${APPROOT}"]

WORKDIR $APPROOT

RUN pip install -r requirements.txt

CMD ["dsdircopy.py", "--help"]
