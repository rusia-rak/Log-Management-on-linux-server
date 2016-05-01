# Log-Management-on-linux-server
Management of logs on linux server.

This script checks all the logs in a particular directory and then checks for log files with a size greater that any pre specified size constant in script, if it is greater, a archive is created, and a specified number of archives for a log file is kept on the file system and finally when that number exceeds the oldest log is deleted and so on.
