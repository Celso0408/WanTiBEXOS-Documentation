FROM sphinxdoc/sphinx:latest

RUN apt-get -y update && apt-get -y install git
RUN pip install sphinx-rtd-theme

ARG BRANCH

ENV BRANCH=$BRANCH

RUN git clone https://github.com/Celso0408/WanTiBEXOS-Documentation -b $BRANCH  /main

WORKDIR /WanTiBEXOS-Documentation/docs

CMD make html
