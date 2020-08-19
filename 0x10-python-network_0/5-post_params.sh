#!/bin/bash
#  display allowed methods
curl -s "$@" -X POST --data-binary "email: hr@holbertonschool.com&subject: I will always be here for PLD"
