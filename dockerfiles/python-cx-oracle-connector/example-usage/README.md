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

```sh
docker run -it --rm python-oracle-connector-test:latest
```

If you're able to connect successfully you should see output like:

```sh
[(1,)]
```