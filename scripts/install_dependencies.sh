#!/usr/bin/env bash

# Install typescript, prisma, sqlite3
rm -rf node_modules
yarn install

# Create Python virtual environment "venv"
rm -rf venv
python3 -m venv venv

# Install Python dependencies in venv
source venv/bin/activate
pip install sqlalchemy
