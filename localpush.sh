files=`find . -newermt "-3600 secs" | sed 's|^./||'`

for file in $files
do
       scp -P 41301 "$file" "akilan@217.76.63.222:/home/akilan/Alloc-Test/CHERI-Allocator/$file"
done
