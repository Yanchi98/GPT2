
import sys
sys.path.append('.')

from bpe import Encoder

test_corpus = '''
    old older finest finer best 
'''

encoder = Encoder(30, pct_bpe=0.88)  # params chosen for demonstration purposes
encoder.fit(test_corpus.split('\n'))
print("test corpus:", test_corpus)
print("BPE dictionary:", encoder.bpe_vocab)
example = "oldest"
print("example:", example)
print("tokenize result:", encoder.tokenize(example))
# ['__sow', 'vi', 'z', 'zi', 'ni', '__eow', '__sow', ':', '__eow', 'he', 'didn', "'", 't', 'fall', '__sow', '?', '__eow', '__sow', 'in', 'co', 'n', 'ce', 'iv', 'ab', 'le', '__eow', '__sow', '!', '__eow']
print("encode:", next(encoder.transform([example])))
# [24, 108, 82, 83, 71, 25, 24, 154, 25, 14, 10, 11, 12, 13, 24, 85, 25, 24, 140, 59, 39, 157, 87, 165, 114, 25, 24, 148, 25]
print("decode:", next(encoder.inverse_transform(encoder.transform([example]))))
# vizzini : he didn ' t fall ? inconceivable !