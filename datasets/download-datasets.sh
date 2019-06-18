mkdir -p datasets/words && \
wget http://www.cs.jhu.edu/~mdredze/datasets/sentiment/processed_acl.tar.gz -O datasets/words-temp.tar.gz && \
tar xzvf datasets/words-temp.tar.gz -C datasets/words && rm datasets/words-temp.tar.gz

