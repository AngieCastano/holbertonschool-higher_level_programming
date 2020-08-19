#!/bin/bash
# displays the body of the response, 200 status code response
curl -s -X GET --header "status: 200" "$@"
