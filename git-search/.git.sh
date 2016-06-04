if [ -z "$1" ]
then 
    echo "please supply a search string"
    exit
fi


hist=`git log --pretty=format:"%h"`

for i in $hist
do
    count=`git show $i |grep "$1" -c`
    if [ $count -gt 0 ]
    then
        git show $i --pretty="%h%n%an%n%ar%n%ad" --no-patch
        git show $i |grep "$1" --colour
        read -n 1 -s
    fi
done
