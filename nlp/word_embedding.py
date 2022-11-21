# This is a word embedding process. Here we use sentence tranformer model, which trains based on "BERT". This transformation
# is more precise than our enwiki.model, which used "word2vec". Therefore, since our attention is on sentiment analysis 
import faulthandler
import pandas as pd
from sentence_transformers import SentenceTransformer
import json
faulthandler.enable()
def feature_vector(csv_file):
    df = pd.read_csv(csv_file,sep=",")
    df = df.loc[2:,"processed_comments"]
    lst = list(df)
    model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
    embeddings = model.encode(lst)
    print(embeddings)
    # with open("new.json",'w') as j:
    #     for line in embeddings:
    #         j.write(json.dumps(line)+'\n')
    

# csv_file = sys.argv[1]
csv_file = "/Users/zhangyuanxin/Desktop/ML/nlp/labeled_data.csv"
feature_vector(csv_file)