# py-etherscan-api module

arbiscan.io API python bindings based on py-etherscan from corey petty

## Description

In order to use the API, you must provide an API key at runtime, which can be found at the arbiscan.io API website.
JSON file `api_key.json` must be stored in the base directory. Its format is as follows:

    { "key" : "YourApiKeyToken" }

with `YourApiKeyToken` is your provided API key token from arbiscan.io

## Installation

To install the package to your computer, simply run the following command in the base directory:

    pip install git+https://github.com/krille-ericsson/py-arbiscan-api.git

## Available bindings

Currently, only the following arbiscan.io API modules are available:

- accounts
- contracts
- stats
- tokens
- proxies
- blocks
- transactions
- Logs
- Gas Tracker

## Examples

All possible calls have an associated example file in the examples folder to show how to call the binding

## tip corey if you wanna tip!

BTC: 16Ny72US78VEjL5GUinSAavDwARb8dXWKG

ETH: 0x5E8047fc033499BD5d8C463ADb29f10f11165ed0
