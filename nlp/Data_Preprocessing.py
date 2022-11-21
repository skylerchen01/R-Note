import pandas as pd
import re
import sys

def preprocess_word(word):
    # Remove punctuation
    word = word.strip('\'"?!,.():;')
    # Convert more than 2 letter repetitions to 2 letter
    # sooooo --> so
    word = re.sub(r'(.)\1+', r'\1\1', word)
    # Remove - & '
    word = re.sub(r'(-|\')', '', word)
    return word

def is_valid_word(word):
    # Check if word begins with an alphabet
    return (re.search(r'^[a-zA-Z][a-z0-9A-Z\._]*$', word) is not None)

def preprocess_rmp(comment):
    processed_rmp = []
    # Convert to lower case
    comment = comment.lower()
    # Replaces URLs with the word URL
    comment = re.sub(r'((www\.[\S]+)|(https?://[\S]+))', ' URL ', comment)
    # Replaces #hashtag with hashtag
    comment = re.sub(r'#(\S+)', r' \1 ', comment)
    # Replace 2+ dots with space
    comment = re.sub(r'\.{2,}', ' ', comment)
    # Strip space, " and ' from tweet
    comment = comment.strip(' "\'')
    # Replace multiple spaces with a single space
    comment = re.sub(r'\s+', ' ', comment)
    words = comment.split()

    for word in words:
        word = preprocess_word(word)


    return ' '.join(processed_rmp)

def preprocess_csv(csv_file_name, processed_file_name):
    df = pd.read_csv(csv_file_name,sep=",")
    professor_name = df.loc[:,"professor_name"]
    comments = df.loc[:,"comments"]
    raw = list(comments)
    processed = []
    for line in raw:
        processed.append(preprocess_rmp(line))
    new_df = pd.DataFrame(list(zip(professor_name,processed)),columns=["professor_name","processed_comments"])
    new_df.to_csv(processed_file_name)
    print('\n Saved processed comments to: %s' % processed_file_name)
    return processed_file_name

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print ('Usage: python preprocess.py <raw-CSV>')
        exit()
    csv_file_name = sys.argv[1]
    processed_file_name = sys.argv[1][:-4] + '-processed.csv'
    preprocess_csv(csv_file_name, processed_file_name)
