#!/bin/bash
#  takes in a URL, displays the size of the body of the response
curl -sw "%{size_request}\n" "$@"
