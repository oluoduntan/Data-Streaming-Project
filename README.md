# Realtime Data Streaming | End-to-End Data Engineering Project

## Table of Contents
- [Introduction](#introduction)
- [System Architecture](#system-architecture)
- [What You'll Learn](#what-youll-learn)
- [Technologies](#technologies)
- [Getting Started](#getting-started)
- [Watch the Video Tutorial](#watch-the-video-tutorial)

## Introduction

This project provides a comprehensive guide to building an end-to-end data engineering pipeline. It covers every stage, from data ingestion and processing to storage, using a robust tech stack that includes Apache Airflow, Apache Kafka, Apache Zookeeper, Apache Spark, and Cassandra. The entire system is containerized with Docker, ensuring easy deployment and scalability.

## System Architecture

![System Architecture](https://github.com/airscholar/Data-Streaming-Project/blob/main/Data%20engineering%20architecture.png)

The project is designed with the following components:

- **Data Source**: We use `randomuser.me` API to generate random user data for our pipeline.
- **Apache Airflow**: Responsible for orchestrating the pipeline and storing fetched data in a PostgreSQL database.
- **Apache Kafka and Zookeeper**: Used for streaming data from PostgreSQL to the processing engine.
- **Control Center and Schema Registry**: Helps in monitoring and schema management of our Kafka streams.
- **Apache Spark**: For data processing with its master and worker nodes.
- **Cassandra**: Where the processed data will be stored.


## Technologies

- Apache Airflow
- Apache Spark
- Apache Kafka
- Apache Zookeeper
- Cassandra
- PostgreSQL
- Docker

## Getting Started

1. Clone the repository:
    ```bash
    git clone https://github.com/oluoduntan/Data-Streaming-Project.git
    ```

2. Navigate to the project directory:
    ```bash
    cd Data-Streaming-Project
    ```

3. Run Docker Compose to spin up the services:
    ```bash
    docker-compose up
    ```
