#!/bin/bash
#  display allowed methods
curl -s "$1" -H "Allow:True"
