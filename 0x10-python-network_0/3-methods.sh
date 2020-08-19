#!/bin/bash
#  display allowed methods
curl -sI "$@" | grep -i allow | awk '{print $2}'
