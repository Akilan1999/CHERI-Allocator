files=`find . -newermt "-3600 secs" | sed 's|^./||'`

for file in $files
do
       sshpass -p "" scp "$file" "akilan@192.168.0.10:/home/akilan/Alloc-Test/CHERI-Allocator/$file"
done
