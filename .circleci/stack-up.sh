#!/bin/bash
for arg; do
    docker stack deploy -c "$arg" $(basename $arg .yml)
done
