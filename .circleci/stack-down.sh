#!/bin/bash
for arg; do
    docker stack rm "$(basename $arg .yml)"
done