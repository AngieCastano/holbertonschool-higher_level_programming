#!/bin/bash
#  takes in a URL, displays the size of the body of the response
curl -sI "$@" | grep -i Content-Length | awk '{print $2}'
