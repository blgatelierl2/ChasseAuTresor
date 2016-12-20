#!/bin/bash

pr -t -28 sheep/sheep

curr=cow
while true; do
    if [ ! -f "sheep/$curr" ]; then
	break
    fi
    echo "$curr"
    l=$(head -1 "sheep/$curr")
    curr=${l#-->}
done

tr -d '*~{!%+$:+_,/&!?|@(#;\n' < sheep/housings
echo

curr=112
while true; do
    echo $curr
    if [ ! -f "sheep/snake$curr" ]; then
	break
    fi
    nbl=$(wc -l < "sheep/snake$curr")
    if [ $nbl -eq 1 ]; then
	l=$(head -1 "sheep/snake$curr")
	curr=${l#-->snake}
	prem=$(echo $curr | cut -c 1)
	if [ $prem = "<" ]; then
	    curr=${curr#<}
	    curr=${curr%>}
	    curr=$(echo "ibase=2;$curr" | bc)
	fi
    else
	l=$(tail -1 "sheep/snake$curr")
	curr=${l#-->snake}
    fi
done

h=474442b06c2c2d75c7eda1bde7c4a324e1bda72f
shasum sheep/* | grep $h

cp sheep/chameleon /tmp/
tmp1=/tmp/chameleon
tmp2=/tmp/chameleon2
while true; do
    case $(file /tmp/chameleon) in
	*gzip*)
	    gzcat $tmp1 > $tmp2
	    cp $tmp2 $tmp1
	    continue
	    ;;
	*bzip*)
	    bzcat $tmp1 > $tmp2
	    cp $tmp2 $tmp1
	    continue
	    ;;
	*)
	    cat $tmp1
	    break
	    ;;
    esac
done

echo
echo
cp $tmp1 $tmp2
tail -n +3 < $tmp2 > $tmp1
sort -t"," -nk2,2 -nk1,1 $tmp1 > $tmp2
#cat $tmp2


l=1
L=$(cat $tmp2 | head -n $l | tail -n 1)
for i in {0..20}; do
    li=""
    for j in {0..20}; do
	if [ $L = "$j,$i" ]; then
	    li="$li\033[0;37;47m  \033[0m"
	    l=$(($l+1))
	    L=$(cat $tmp2 | head -n $l | tail -n 1)
	else
	    li="$li  "
	fi
    done
    printf "$li\n"
done
echo