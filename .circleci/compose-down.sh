#!/bin/bash
for arg; do
    docker-compose -f "$arg" stop
    docker-compose -f "$arg" rm -f
done