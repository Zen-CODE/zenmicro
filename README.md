# ZenMicro

A MicroService Architecture for ZenPlayer.

## Introduction

This project aims to implement the ZenPlayer Medioa Player toy as a collection
of robust microservices that represent abstract components of the player.

Why? The vision is to create independent yet tightly integerated components in
order to support a Media PLayer experience that moves across devices anb
infrastructure.

## Concept

# TODO

## Folder Structure

The folder are as follow:

* *compose*
  The services are controlled via docker-compose. To start the services:

    cd compose
    docker-compose up

* *core*
  The folder contains the core application, which  provide the Swagger UI,
  handles the delegation of requests and builds the API based on the endpoints
  exposed by the service.

* *services*
  The contains a folder for each the miscroservices, each of which should
  contain:
  * The `Dockerfile` used to build the service.
  * The `service_requirements.txt` file.
  * The `service` folder with the following contents:
    * `api.py` - python file that defines the API via puiblic methods.
    * `config.json` - provides metadata around the service e.g. Name, url etc.
