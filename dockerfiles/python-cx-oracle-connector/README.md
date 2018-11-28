# Python cx_Oracle Connector

Dockerfile that has the cx_Oracle python connector installed so any python code can connect to a specified Oracle DB.

Update the username, password, and database connection values in the [connection_config.py file](src/connection/connection_config.py) or set them as environment variables using the names in the file.

Test out your connection by using something similar to what is done in [app.py](src/app.py).

Oracle Instant Client version (the [.zip](src/connection/instantclient-basic-linux.zip)) is `linux.x64-18.3.0.0.0dbru`

## Example Playbook

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
```

## Important Links

[cx-oracle Read the Docs](https://cx-oracle.readthedocs.io/en/latest/index.html)

[Oracle ODPI Docs Home](https://oracle.github.io/odpi/doc/)

[Installation Docs](https://oracle.github.io/odpi/doc/installation.html)

[Oracle Instant Client Downlaods](https://www.oracle.com/technetwork/database/database-technologies/instant-client/downloads/index.html)
