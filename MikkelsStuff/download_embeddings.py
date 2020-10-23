#from danlp.models.embeddings  import load_wv_with_gensim
#word_embeddings = load_wv_with_gensim('conll17.da.wv')
#word_embeddings.save("word2vec.model")  # save it on your computer


#from danlp.download import download_model, DEFAULT_CACHE_DIR

#DEFAULT_CACHE_DIR

#download_model('conll17.da.wv', cache_dir=DEFAULT_CACHE_DIR)

from gensim.models.keyedvectors import KeyedVectors

model = KeyedVectors.load_word2vec_format('C:/Users/Mikkel/Desktop/GoogleNews-vectors-negative300.bin', binary=True)
