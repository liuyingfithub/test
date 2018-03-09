#! /bin/sh

echo "is it morning"
read YES_OR_NO
case "$YES_OR_NO" in
yes|y|Yes|YES)
	echo "good morning"
	echo "good morning";;
[nN]*)
	echo "good afternoon";;
*)
	echo "sorry"
	exit 1;;
esac
