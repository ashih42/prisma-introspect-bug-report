#!/usr/bin/env bash

export PYTHONPATH='python_src'

DB_FILE='doge.db'

# Delete old database file
rm -f ${DB_FILE}

# Define database tables in Python
venv/bin/python scripts/create_tables.py

# Generate Prisma schema from database tables
prisma introspect

# Generate Prisma client
prisma generate
