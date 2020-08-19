#!/bin/bash
#  display allowed methods
curl -s "$1" -I GET | grep -i ALLOW | cut -d ":" -f2 | cut -b 2-
