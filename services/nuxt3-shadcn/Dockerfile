# Use the official Node.js LTS image as a base
FROM node:lts-alpine

# Set the working directory in the container
WORKDIR /app

# Copy package.json and yarn.lock to the container
COPY package.json .
COPY package-lock.json .

# Install dependencies using Yarn
RUN npm install

# Copy the rest of the application files to the container
COPY . .

# Build the Nuxt 3 application
RUN npm run build

# Expose the port that the Nuxt app will run on
EXPOSE 3000

# Set the command to run the Nuxt app
CMD ["npm", "run", "start"]
