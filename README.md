# SETUP GUIDE FOR INFRA

1. Add your Solidity files to the `config/src/` directory. For the setup contract, use the format provided in `config/src/Setup.sol`.
2. Update the user balance, Setup contract balance, and flag values in the `config/.env` file.
3. Run the following command inside the `deployers/` directory:
```bash
sudo docker-compose up --build
```
4. By default, the `docker-compose.yml` file binds port **9000** for the Anvil proxy and port **8888** for the launch service.
5. Adjust the ports as needed according to your CTF instance configuration.
6. Run the following to launch a instance
```bash
nc 127.0.0.1 8888
```

