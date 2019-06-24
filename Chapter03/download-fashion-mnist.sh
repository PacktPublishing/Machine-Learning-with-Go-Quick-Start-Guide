mkdir -p datasets/mnist && \
wget http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/train-images-idx3-ubyte.gz -O datasets/mnist/images.gz && \
wget http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/train-labels-idx1-ubyte.gz -O datasets/mnist/labels.gz
