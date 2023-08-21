#!/bin/bash
echo 'Master Bash'

sh calculate.sh & sh transcoder.sh  & sh source.sh 
sh rename.sh
