
# coding: utf-8

# In[1]:
'''
#简易数据集，应该用不到
import tweepy           # To consume Twitter's API
import pandas as pd     # To handle data
import numpy as np 


consumer_key = 'yXSdqn2g9pOIQjpE64CuNeR7d'
consumer_secret = 'do2qpFDDRXasIi0YZI6lhzrZdHGgd9joeFUOeUiXuij8YRRtUj'
access_token = '1096653841251094530-7mFKPZYcFevWZlhjnmncp6CyrFDWSg'
access_token_secret = 'GwNjVIHEeSUDFtEPIwpEiYHRa0ohSvyfJyq8q97vVqRNL'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweets = api.user_timeline(screen_name="realDonaldTrump", count=200)
print("Number of tweets extracted: {}.\n".format(len(tweets)))
# We print the most recent 5 tweets:
print("5 recent tweets:\n")
for tweet in tweets[:5]:
    print(tweet.text)
    print()

'''
# In[9]:
import pandas as pd     # To handle data
import numpy as np 
data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])



# In[11]:

data['len']  = np.array([len(tweet.text) for tweet in tweets])
data['ID']   = np.array([tweet.id for tweet in tweets])
data['Date'] = np.array([tweet.created_at for tweet in tweets])
data['Source'] = np.array([tweet.source for tweet in tweets])
data['Likes']  = np.array([tweet.favorite_count for tweet in tweets])
data['RTs']    = np.array([tweet.retweet_count for tweet in tweets])


# In[12]:




# In[16]:



# In[19]:

from textblob import TextBlob
import re
def clean_tweet(tweet):
    '''
    Utility function to clean the text in a tweet by removing 
    links and special characters using regex.
    '''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
def analize_sentiment(tweet):
    '''
    Utility function to classify the polarity of a tweet
    using textblob.
    '''
    
    analysis = TextBlob(clean_tweet(tweet))
    if analysis.sentiment.polarity > 0:
        return 1
    elif analysis.sentiment.polarity == 0:
        return 0
    else:
        return -1
    

    
    
data['SA'] = np.array([ analize_sentiment(tweet) for tweet in data['Tweets'] ])



# In[26]:
#每日的情感倾向均值
#a=data["Date"].dt.strftime("%d%m%y")
daily = data.set_index("Date").groupby(pd.Grouper(freq='D'))["SA"].mean() 



# In[ ]:



