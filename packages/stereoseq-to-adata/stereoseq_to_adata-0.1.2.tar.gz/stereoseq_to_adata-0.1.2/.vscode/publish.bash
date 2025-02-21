#!/usr/bin/expect -f
spawn uv publish
expect "Enter username"
send "__token__\r"
expect "Enter password"
send "pypi-AgEIcHlwaS5vcmcCJGZkYTY3ZGNkLTcwNTUtNGNkMS1iOTJkLTkwNTJhZjEyZWFhZAACKlszLCJkM2QwNzZhNC0yZDZmLTQ1OGItYTk4OS1lMTQ0ZTdiNmI4NmYiXQAABiDp3Wz0JFIjlgLq2c-Iz19aF2XS5oom8ijcy8oruYXr3A\r"
expect eof