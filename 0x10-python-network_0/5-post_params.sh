#!/bin/bash
#  display allowed methods
curl -s "$@" -X POST -d "email: hr@holbertonschool.com" -d "subject: I will always be here for PLD"
