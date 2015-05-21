#!/bin/bash
l=0; w=5; O=`echo -e "\033[7m \033[0m"`; n='
'
d[l++]="OOOO    O OOOO OOOO O  O OOOO O    OOOO OOOO OOOO   "
d[l++]="O  O    O    O    O O  O O    O       O O  O O  O O "
d[l++]="O  O    O OOOO OOOO OOOO OOOO OOOO    O OOOO OOOO   "
d[l++]="O  O    O O       O    O    O O  O    O O  O    O O "
d[l++]="OOOO    O OOOO OOOO    O OOOO OOOO    O OOOO    O   "
#
for ((i=0;i<=l+2;i++)); do echo; done; io=`echo -e "\r\033[$((l+2))A"`
while :; do
  o=$io; t=`date -u +%T`; ds="`echo $t | sed 's/\(.\)/\1 /g;s/:/10/g'`"
  for ((i=0;i<l;i++)); do o="$o    "
    for c in $ds; do
      o="${o}${d[i]:c*w:w}"
    done
    o="${o}${n}"
  done
  o="${o}       `date`${n}               `date +%s`${n}"
  echo -n "$o" | sed "s/O/$O/g"
  sleep 1
done
