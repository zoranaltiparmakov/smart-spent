# base image
FROM node:10.12.0

# install chrome for protractor tests
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
RUN apt-get update && apt-get install -yq google-chrome-stable

ARG DIR="/frontend"
# set working directory
RUN mkdir ${DIR}
WORKDIR ${DIR}

# add `/usr/src/app/node_modules/.bin` to $PATH
ENV PATH ${DIR}/node_modules/.bin:$PATH

# install and cache app dependencies
COPY package.json ${DIR}/package.json
RUN npm install

# add app
COPY . ${DIR}
