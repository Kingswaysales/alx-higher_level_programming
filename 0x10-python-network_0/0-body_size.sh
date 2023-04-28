#!/bin/bash
#Displays size of the body response
curl -sI "s1" | grep "Content-Length" | cut -d' ' -f 2
