# SSH Without Needing Password

How to set up an authorized_key on a remote host so you don't have to supply a password each time you ssh into the host.

## Steps

1. Create your `.ssh directory` on your local machine if not already made.

    ```sh
    mkdir -p ~/.ssh
    ```

2. Generate `public and private keys` on your local host. You can leave all the values default if desired.

    ```sh
    ssh-keygen
    ```

3. Open a new terminal and log into the remote server. Create a `.ssh directory` there as well as an `authorized_keys file`.

    ```sh
    mkdir -p ~/.ssh;
    touch ~/.ssh/authorized_keys
    ```

4. On your local machine run a `scp` command to move the public key to the remote server. The command should be something like:

    ```sh
    scp ~/.ssh/id_rsa.pub <id>@<remote_host>:~/id_rsa.pub
    ```

5. In the terminal logged into the remote host, add the contents of the public key to the `authorized_keys file`

    ```sh
    cat ~/id_rsa.pub >> ~/.ssh/authorized_keys
    ```

6. Log out of the remote server and test that you can ssh into the remote server without having to supply a password.

    ```sh
     ssh -i ~/.ssh/id_rsa <id>@<remote_host>
     ```