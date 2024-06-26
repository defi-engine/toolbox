from pathlib import Path
from brownie import *
import json
from loguru import logger

from utils.utils import get_multicall_3_contract, get_contract

script_root = Path(__file__).resolve().parent.parent


class FunctionNotSupported(Exception):
    pass

class NetworkNotConfigure(Exception):
    pass


def _message(name, address, decoded_calldata):
    print(f"contract name: {name}")
    print(f"contract address: {address}")
    print(f"decoded calldata: {decoded_calldata}")
    print(40*"*")    


def main():
    _network = network.show_active()
    try:
        multicall3_contract = get_multicall_3_contract(_network.upper())
    except KeyError:
        logger.error(f"KeyError, can't find contract for {_network} network ")
        raise NetworkNotConfigure

    with open(f"{script_root}/scripts/encoded_multicall3.json", 'r') as file:
        data = json.load(file)

    for _data in data:
        if _data["method"] != "eth_call":
            continue
        for param in _data["params"]:
            if isinstance(param, dict):
                decoded_data = multicall3_contract.decode_input(param["data"])
                if "aggregate3((address,bool,bytes)[])" in decoded_data[0]:
                    for call in decoded_data[1][0]:
                        contract_address = call[0]
                        calldata = call[2]

                        contract = get_contract(_network.upper(), contract_address)
                        _message(contract._name, contract.address, contract.decode_input(calldata))
                else:
                    raise FunctionNotSupported
        print(40*"=")
