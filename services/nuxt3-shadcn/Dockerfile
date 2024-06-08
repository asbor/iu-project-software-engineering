# Use the official Node.js LTS image as a base
FROM node:lts-alpine

# Set the working directory in the container
WORKDIR /app

# Copy package.json and yarn.lock to the container
COPY package.json yarn.lock ./

# Install dependencies using Yarn
RUN yarn install

# Copy the rest of the application files to the container
COPY . .

# Build the Nuxt 3 application
RUN yarn build

# Expose the port that the Nuxt app will run on
EXPOSE 3000

# Set the command to run the Nuxt app
CMD ["yarn", "start"]
