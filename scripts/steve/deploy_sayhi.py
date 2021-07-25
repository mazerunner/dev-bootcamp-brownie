#!/usr/bin/python3
from brownie import SayHello, config, network
from scripts.helpful_scripts import fund_with_link, get_account


def main():
    account = get_account()
    say_hi = SayHello[-1]
    tx = fund_with_link(
        say_hi.address, amount=config["networks"][network.show_active()]["fee"]
    )
    tx.wait(1)
    say_hi.sayHello({"from": account})
    print("Requested!")
