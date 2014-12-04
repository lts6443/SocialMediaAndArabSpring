#! /usr/bin/env bash
lineNumber=0
rm tweets.json
echo "[" > tweets.json
count=0
max=20
while [ $count -lt $max ]; do
echo $count 
if [ $count -eq `expr $max - 1` ]; then
./TwitterStuff.py $lineNumber True >> tweets.json
fi
if [ $count -lt `expr $max - 1` ]; then
./TwitterStuff.py $lineNumber False >> tweets.json
fi
lineNumber=`expr $lineNumber + 90`
count=`expr $count + 1`
sleep 30 
done
echo "]" >> tweets.json
