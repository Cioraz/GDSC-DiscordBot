FROM node:latest

WORKDIR /app

COPY . .

RUN npm install
RUN npm install -g nodemon

CMD ["nodemon", "index.js"]