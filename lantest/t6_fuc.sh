#! /bin/sh

fun(){
	echo "hello"
	echo $0
	echo $1
	echo $2
	echo $3
	echo "hello"
}

echo "-----start-------"
fun aa bb ll
echo "-----end------"
