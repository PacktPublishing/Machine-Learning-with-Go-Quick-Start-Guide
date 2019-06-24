mkdir -p datasets/housing && \
wget https://ndownloader.figshare.com/files/5976036 -O datasets/housing/data.tgz && \
tar xzvf datasets/housing/data.tgz -C datasets/housing && \
rm datasets/housing/data.tgz
