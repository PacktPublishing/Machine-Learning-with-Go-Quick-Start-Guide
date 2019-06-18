apk --no-cache \
        --repository http://dl-4.alpinelinux.org/alpine/v3.7/community \
        --repository http://dl-4.alpinelinux.org/alpine/v3.7/main \
        --arch=x86_64 add python3-dev && \
apk add --no-cache \
            --allow-untrusted \
            --repository \
             http://dl-4.alpinelinux.org/alpine/edge/testing \
            hdf5 \
            hdf5-dev && \
apk --no-cache \
        --repository http://dl-4.alpinelinux.org/alpine/v3.7/community \
        --repository http://dl-4.alpinelinux.org/alpine/v3.7/main \
        --arch=x86_64 add gcc gfortran build-base wget freetype-dev libpng-dev openblas-dev && \
pip3 install -r requirements.txt && \
cat << EOT > $HOME/.keras/keras.json 
{
    "epsilon": 1e-07,
    "backend": "theano",
    "floatx": "float32",
    "image_dim_ordering": "th"
}
EOT