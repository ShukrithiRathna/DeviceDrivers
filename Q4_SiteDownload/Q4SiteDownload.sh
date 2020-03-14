#!/bin/sh


# the output file
FILE=/home/Shukrithi/College/DeviceDrivers/Q4SiteDownload.out

# the url to retrieve
URL=https://itsfoss.com

# write header information to the log file
start_date=`date`
echo "START-------------------------------------------------" >> $FILE
echo "" >> $FILE

# retrieve the web page using curl. time the process with the time command.
time wget --connect-timeout 100 $URL >> $FILE 2>&1


# write additional footer information to the log file
echo "" >> $FILE
end_date=`date`
echo "STARTTIME: $start_date" >> $FILE
echo "END TIME:  $end_date" >> $FILE
echo "" >> $FILE
