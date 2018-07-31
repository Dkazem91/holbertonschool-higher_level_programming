#!/bin/bash
#options
curl -sI "$1" | grep -i Allow | cut -d ' ' -f2-
