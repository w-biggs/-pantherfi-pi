#!/bin/sh
speedtest-cli --json >> raw.json && python3 cleandata.py >> clean.json && python3 senddata.py && rm clean.json && rm raw.json
