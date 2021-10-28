#!/bin/bash

#Test the forward sort
printf '1\n\1\n' | python3 nameSorter.py "Sort Me.txt" > "output1.txt"
if diff -b "output1.txt" "sortedShortLong.txt";
then
	echo "Short to long sort pass"
else
	echo "Short to long sort fail"
fi

#Test the backwards sort
printf '2\n\1\n' | python3 nameSorter.py "Sort Me.txt" > "output2.txt"
if diff -b "output2.txt" "sortedLongShort.txt";
then
	echo "Long to short sort pass"
else
	echo "Long to short sort fail"
fi