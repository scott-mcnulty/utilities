# Python cx_Oracle Connector

Dockerfile that has the cx_Oracle python connector installed so any python code can connect to a specified Oracle DB.

See the `example-usage` directory for example usage in a simple app to test connection.

Oracle Instant Client version (the [.zip](install/instantclient-basic-linux.zip)) is `linux.x64-18.3.0.0.0dbru`

## Using the Docker image

Set the environment variables for connecting to a database:

- CX_ORACLE_MAIN_USER
- CX_ORACLE_MAIN_PASSWORD
- CX_ORACLE_CONNECT_STRING

Other environment variables are below:

- CX_ORACLE_EDITION_USER
- CX_ORACLE_EDITION_NAME
- CX_ORACLE_EDITION_PASSWORD

See the [connection_config.py](example-usage/src/connection/connection_config.py) for an example.

<!-- ## Example Playbook

Build the image:

```sh
docker build . -t python-oracle-connector-test
```

Run the container:

```sh
docker run -it --name python-oracle-connector-test python-oracle-connector-test:latest run.sh
```

If you're able to connect successfully you should see output like:

```sh
[(1,)]
``` -->

## Important Links

[cx-oracle Read the Docs](https://cx-oracle.readthedocs.io/en/latest/index.html)

[Oracle ODPI Docs Home](https://oracle.github.io/odpi/doc/)

[Installation Docs](https://oracle.github.io/odpi/doc/installation.html)

[Oracle Instant Client Downlaods](https://www.oracle.com/technetwork/database/database-technologies/instant-client/downloads/index.html)
