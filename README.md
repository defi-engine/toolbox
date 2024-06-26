# toolbox

tools for reverse engineering.

## features

- decoding messages from JSON-RPC

## install locally

```bash
poetry install --no-root
poetry shell
```

## add new network

e.g. Linea mainnet

```bash
brownie networks add Linea linea-mainnet chainid=59144 host=https://rpc.linea.build/
```

## env variable

Create a .env file and add the `WEB3_ALCHEMY_PROJECT_ID` or `WEB3_INFURA_PROJECT_ID` environment variables, depending on the selected provider.

## add data for decoing

multicall3 decoding - add JSON-RPC query to the list in the `encoded_multicall3.json` file. The script will automatically read from this file, iterate over each message, and try to decode them.

## commands for RPC-JSON decoding

### decode multicallV3

```bash
brownie run scripts/decode_multicall3_aggregate3.py --network <network-name>

# Example for Linea network:
brownie run scripts/decode_multicall3_aggregate3.py --network linea-mainnet
```
