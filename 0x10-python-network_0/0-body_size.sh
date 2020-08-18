#!/usr/bin/env bash
#  takes in a URL, displays the size of the body of the response
curl -w "%{size_request}\n" "$@"
