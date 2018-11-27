# Base image
FROM docker.io/ubuntu:16.04

# Install python3 and any other tools
RUN apt-get update && apt-get install -y --no-install-recommends \
	cmake curl git make python3 python3-pip python3-setuptools build-essential unzip libaio1 \
	&& apt-get clean && rm -rf /var/lib/apt/lists/*

# Add source files
COPY src /src

# Set up the Oracle client
COPY src/connection/instantclient-basic-linux.zip /opt/oracle/instantclient-linix/
RUN unzip /opt/oracle/instantclient-linix/instantclient-basic-linux.zip -d /opt/oracle/instantclient-linix
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/oracle/instantclient-linix/instantclient_18_3

WORKDIR /src

# Run pip install to install python packages
RUN pip3 install --upgrade pip -r example_requirements.txt

# Default entrypoint
ENTRYPOINT [ "sh" ]