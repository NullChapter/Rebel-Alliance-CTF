#!/bin/bash
set -e

# Wait for MongoDB to be ready
./wait-for-it.sh $DB_URI --timeout=30 --strict -- echo "MongoDB is up"

# Run the command passed as arguments
exec "${@}"
