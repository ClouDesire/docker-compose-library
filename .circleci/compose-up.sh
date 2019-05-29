#!/bin/bash
for arg; do
    docker-compose -f "$arg" pull
    docker-compose -f "$arg" up -d
done
