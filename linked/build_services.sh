#! /bin/bash
# This module provides a helper script for building the application structures"
# for each of our micro services."
for VARIABLE in library
do
    echo "    1. Clearing previous build for $VARIABLE..."
    rm $VARIABLE

    echo "    2. Creating containing folder for the $VARIABLE service..."
    ln -s ../core  $VARIABLE

    echo "    3. Linking in the $VARIABLE service folder..."
    mkdir -p $VARIABLE/services
    ln -sf ../services/$VARIABLE  $VARIABLE/services/$VARIABLE

    echo "    4. Linking in the $VARIABLE servie specific requirements..."
    ln -sf ../services/$VARIABLE/service_requirements.txt  $VARIABLE/service_requirements.txt
done