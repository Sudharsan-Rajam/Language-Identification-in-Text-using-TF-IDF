import string
import re
import sys
import pandas as pd




# method for Preprocessing
def preprocess_data(dataset, language):
    data = []
    lang = []
    for i, tweet in dataset.iterrows():
        tweet = tweet['Tweet']
        if len(tweet) != 0:
            tweet = tweet.lower()
            tweet = re.sub(r'http\S+', '', tweet)
            tweet = re.sub(r"\d+","",tweet)
            tweet = tweet.translate(translate_table)
            tweet = remove_emoji(tweet) 
            data.append(tweet)
            lang.append(language)
    return (data, lang)


english_lang = preprocess_data(td.english_df, "English")
german_lang = preprocess_data(td.german_df, "German")
japanese_lang = preprocess_data(td.japanese_df, "Japanese")
spanish_lang = preprocess_data(td.spanish_df, "Spanish")
french_lang = preprocess_data(td.french_df, "French")
chinese_lang = preprocess_data(td.chinese_df, "Chinese")
hindi_lang = preprocess_data(td.hindi_df, "Hindi")

df_data = pd.DataFrame({"Text":english_lang[0]+german_lang[0]+japanese_lang[0]+spanish_lang[0]+french_lang[0]+chinese_lang[0]+hindi_lang[0], "Language":english_lang[1]+german_lang[1]+japanese_lang[1]+spanish_lang[1]+french_lang[1]+chinese_lang[1]+hindi_lang[1]})
