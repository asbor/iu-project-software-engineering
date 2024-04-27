# Use the official Node.js LTS image as a base
FROM node:20.12.2-buster

# Set the working directory in the container
WORKDIR /app

# Copy package.json and yarn.lock to the container
COPY . .

# Install dependencies using Yarn
RUN yarn install

# Build the Nuxt 3 application
RUN yarn build

# Expose the port that the Nuxt app will run on
EXPOSE 3000

# Set the command to run the Nuxt app
CMD ["yarn", "start"]
