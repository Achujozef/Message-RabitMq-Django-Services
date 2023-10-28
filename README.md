# Message-RabitMq-Django-Services
This Git repository contains two services: an Admin service and a UserApp service built using Django Rest Framework. The Admin service is responsible for CRUD operations on products, while the UserApp service allows users to interact with and like products.

Both services communicate with each other using RabbitMQ as the message broker. The services are containerized using Docker and orchestrated using Docker Compose. Additionally, the `consumer.py` script is provided to consume messages from RabbitMQ.

## Table of Contents

1. [Project Structure](#project-structure)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Docker Compose](#docker-compose)
6. [Message Queue](#message-queue)
7. [Contributing](#contributing)
8. [License](#license)

## Project Structure

The project structure is organized as follows:

- `admin_service/`: Django Admin service
- `userapp_service/`: UserApp service
- `docker-compose.yaml`: Docker Compose configuration
- `consumer.py`: RabbitMQ message consumer

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Docker: Install [Docker](https://www.docker.com/get-started) on your machine.
- Docker Compose: Install [Docker Compose](https://docs.docker.com/compose/install/) on your machine.
- RabbitMQ: Ensure you have RabbitMQ up and running, either locally or in a remote server. You'll need to configure the services to connect to the RabbitMQ server.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
