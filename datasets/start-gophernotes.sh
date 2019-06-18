sudo docker run -it -p 8888:8888 -e GODEBUG=cgocheck=0 -v $(pwd):/usr/share/notebooks gopherdata/gophernotes:latest-ds
