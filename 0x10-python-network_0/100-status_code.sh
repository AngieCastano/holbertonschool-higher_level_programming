#!/bin/bash
#  takes in a URL, displays the size of the body of the response
curl -s --write-out "%{http_code}" -s --output /dev/null "$1"
