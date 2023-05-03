#!/bin/bash

echo "Creating requirements.txt file"
poetry export --without-hashes --without-urls -o requirements.txt
