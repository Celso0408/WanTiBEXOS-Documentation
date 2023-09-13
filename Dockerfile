FROM sphinxdoc/sphinx:latest

RUN apt-get -y update && apt-get -y install git
RUN pip install sphinx-rtd-theme

ARG BRANCH

ENV BRANCH=$BRANCH

RUN git clone https://github.com/simstack/Simstack-Documentation.git -b $BRANCH  /simstack

WORKDIR /simstack/docs

CMD make html
