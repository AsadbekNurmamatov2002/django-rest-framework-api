FROM node:20.4

WORKDIR /frontend

COPY . .

RUN npm install

EXPOSE 5173

CMD [ "npm", "run", "dev" ]