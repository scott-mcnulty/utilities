# Example Usage

This directory contains an example python app to demostrate a simple case to test if you're able to connect to the database.

Update the username, password, and database connection values in the [connection_config.py](src/connection/connection_config.py) file or set them as environment variables using the names in the file.

Test out your connection by using something similar to what is done in [app.py](src/app.py).

## Example Playbook

Build the image:

```sh
docker build . -t python-oracle-connector-test
```

Run the container:

If you modified the [connection_config.py](src/connection/connection_config.py) file directly:

```sh
docker run -it --rm python-oracle-connector-test:latest
```

Or if you want to use environment variables:

```sh
docker run -it --rm \
-e "CX_ORACLE_MAIN_USER=<user>" \
-e "CX_ORACLE_MAIN_PASSWORD=<pass>" \
-e "CX_ORACLE_CONNECT_STRING=<host>/<service>" \
python-oracle-connector-test:latest
```

If you're able to connect successfully you should see output like:

```sh
[(1,)]
```