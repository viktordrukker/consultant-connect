FROM node:18-alpine
WORKDIR /app
COPY package.json vite.config.js index.html ./
COPY src ./src
RUN npm install && npm run build
CMD ["npx", "vite", "preview", "--host", "0.0.0.0", "--port", "3000"]
