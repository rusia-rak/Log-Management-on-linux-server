# Log-Management-on-linux-server
Management of logs on linux server. (Python Scripting)

This script checks all the logs in a particular directory and then checks for log files with a size greater that any pre specified size constant in script, if it is greater, a archive is created, and a specified number of archives for a log file is kept on the file system and finally when that number exceeds the oldest log is deleted and so on.

To get the script working - 
1. Edit the script to match your need. Edit the constants pths, mx and nm accordingly.
2. Make sure that the user for which cron would be set, have correct permissions on the paths defined.
3. Add a cron for the file. For eg - 
    0 0 * * * /path/to/logmng.py 
    This would run your script once every 24 hours. Adjust it according to your log usage.
