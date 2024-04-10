FROM node:20.4-alpine3.18

COPY package.json yarn.lock .yarnrc /app/

WORKDIR /app

RUN yarn

COPY . /app/

EXPOSE 3000

CMD ["npx", "react-scripts", "start"]
