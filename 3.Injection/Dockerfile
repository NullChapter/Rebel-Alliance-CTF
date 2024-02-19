# Use a Node.js base image
FROM node:14

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json separately to leverage Docker cache
COPY package*.json ./

# Install Node.js dependencies
RUN npm install

# Copy the rest of the application files
COPY . .

# Install 'wait-for-it' script to wait for MongoDB
COPY wait-for-it.sh .
RUN chmod +x wait-for-it.sh

# Use the official MongoDB image as a service
# This won't install MongoDB in the Node.js image, but it will run it in a separate container
# and link it to the Node.js container
CMD ["./wait-for-mongo.sh", "node", "index.js", "&&", "node", "puppeteerBot.js"]
