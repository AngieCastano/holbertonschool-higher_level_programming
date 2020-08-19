#!/bin/bash
#  display allowed methods
curl -sI "$@" | grep -i Allow | awk '{print $2}'
