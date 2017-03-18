#!/bin/bash

# Check comparable file.
DIFF_FILE="test/test_result.csv"
if [ ! -e $DIFF_FILE ]; then
    echo "No diff file($DIFF_FILE)."
    exit 1
fi

# Delete previous result file.
RESULT_FILE="result.csv"
if [ -e $RESULT_FILE ]; then
    rm result.csv
    echo "Delte old result file"
fi

# Execute test
python ../cronquot/cronquot.py -s 20161230200000 -e 20170104010000 -d crontab

# Compare result is correct or not
RESULT_CMD="diff -c result.csv test/test_result.csv"
RESULT_COUNT=`$RESULT_CMD | wc -c | tr -d " "`
if [ $RESULT_COUNT -eq 0 ]; then
    echo "Success!"
    exit 0
else
    echo "Failure! Your diff is below."
    echo "---------------------------------->"
    eval $RESULT_CMD
    exit 1
fi
