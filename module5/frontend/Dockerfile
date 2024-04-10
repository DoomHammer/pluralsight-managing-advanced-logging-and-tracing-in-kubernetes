FROM node:20.4-alpine3.18

COPY package.json yarn.lock .yarnrc /app/

WORKDIR /app

RUN yarn && \
    mkdir -p /mnt/c/Windows/System32/WindowsPowerShell/v1.0 && \
    touch /mnt/c/Windows/System32/WindowsPowerShell/v1.0/powershell.exe && \
    chmod +x /mnt/c/Windows/System32/WindowsPowerShell/v1.0/powershell.exe

COPY . /app/

EXPOSE 3000

CMD ["npx", "react-scripts", "start"]
