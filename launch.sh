#!/usr/bin/env bash
echo "cefFlask booting server"
py -3 main.py &
echo "cefFlask booting embedded browser in 3"
sleep 1
echo 2
sleep 1
echo 1
sleep 1
pid=$!
py -3 cef_boot.py
kill ${pid}