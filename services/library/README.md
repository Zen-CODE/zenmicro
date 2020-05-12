# ZenPLayer Library Component

To build:

    docker build . -t library/v1

To run:

    docker run -p 8001:8001 library/v1

To run with our folder mounted:

    docker run -v ~/Music:/app/Music -p 8001:8001 library/v1
