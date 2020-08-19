#!/bin/bash
#  display allowed methods
curl -s "$1" -I GET | grep -i ALLOW | awk '{print $2 $3 $4 $5 $6}'
