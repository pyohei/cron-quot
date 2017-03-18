#!/bin/bash

# Check comparable file.
DIFF_FILE="test/test_result.csv"
if [ ! -e $DIFF_FILE ]; then
    echo "No diff file($DIFF_FILE)."
    exit 1
fi

# Black Box test for cron parser.
rm result.csv

python ../cronquot/cronquot.py -s 20161230200000 -e 20170104010000 -d crontab

RESULT=`diff result.csv test/test_result.csv`

if [ -z $RESULT ]; then
    echo "Success!"
else
    echo "Failure! Your diff is below."
    echo ${RESULT}
fi
