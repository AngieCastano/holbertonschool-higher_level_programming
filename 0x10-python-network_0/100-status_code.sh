#!/usr/bash
# writes sttus code without pipelines
curl --write-out "%{http_code}\n" --s --output /dev/null "$1"
