# medchat/Dockerfile

# Use the official Node.js image.
# https://hub.docker.com/_/node
FROM node:16 AS build

# Set the working directory
WORKDIR /app

# Install dependencies
COPY src/package*.json ./
RUN npm install

# Copy the rest of the application code
COPY src/ .

# Build the application
RUN npm run build

# Use the official Nginx image to serve the app
# https://hub.docker.com/_/nginx
FROM nginx:alpine

# Copy the build output from the previous stage
COPY --from=build /app/dist /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
