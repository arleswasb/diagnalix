FROM node:20-slim

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

EXPOSE 3000

# O comando npm run dev usa o --watch que configuramos no package.json
CMD ["npm", "run", "dev"]
