# creating-virtual-serial-port-in-linux

# install tool named as socat
>sudo apt-get install socat

# create serial port using the command
>socat -d -d pty,raw,echo=0 pty,raw,echo=0
	2020/05/27 12:04:54 socat[4306] N PTY is /dev/pts/2
	2020/05/27 12:04:54 socat[4306] N PTY is /dev/pts/3
	2020/05/27 12:04:54 socat[4306] N starting data transfer loop with FDs [5,5] and [7,7]

# open another tab and use this serial port for recieving purpose
	cat  </dev/pts/2

# Open another tab for the sending port and type
	echo "its working" > /dev/pts/3

# you will see the output on /dev/pts/2 ports
