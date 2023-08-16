# PDF to JPG Web App

A simple web application to convert PDF files to JPG images. Built using Flask and deployed in a Docker container.

## Overview

This web application provides an intuitive interface where users can upload PDF files, and the application then converts these files into JPG images. The application is containerized for easy deployment and scalability.

## Features

- Drag and drop interface for easy file uploads.
- Ability to convert multiple PDFs simultaneously.
- Download links for the converted JPG images.
- Deployed using Docker for seamless scaling and distribution.

## Deployment

To deploy this application, use the following Docker Compose command:

```
docker-compose up -d
```

This command will pull the necessary images and start the services defined in the `docker-compose.yml` file. The application will be accessible at `http://localhost:5000`.
