#! /bin/sh

echo "Beginning script ..."

FILE_NUM=1

# change script to concatenate files 
# echo "File number"
# read FILE_NUM
# touch "${FILE_NUM}.txt"

for i in 45 47 48
do
   cat "$i.txt" >> pr_misc.txt
done

