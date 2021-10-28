Testing update README

To test the name sorter program first make sure all .txt, .py, and the test.sh files
are in the same directory.
Then run $./test.sh
If there is a r$ error with this command a potential fix is:
$sed -t -e 's/\r$//' /directory path to test.sh file