import tweepy as tp
from time import sleep
import pickle
import json

# Authorization infos
consumer_key = "yXSdqn2g9pOIQjpE64CuNeR7d"
consumer_secret = "do2qpFDDRXasIi0YZI6lhzrZdHGgd9joeFUOeUiXuij8YRRtUj"
access_token = "1096653841251094530-7mFKPZYcFevWZlhjnmncp6CyrFDWSg"
access_token_secret = "GwNjVIHEeSUDFtEPIwpEiYHRa0ohSvyfJyq8q97vVqRNL"

# Twitter IDs
# BAY_ID = 137319302
# HON_ID = 64764487
# MMM_ID = 378197959
# SYN_ID = 16366375

if __name__ == '__main__':
    # Get Twitter API
    auth = tp.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tp.API(auth)

    res = []
    # curmaxid = 1096499443770245121 + 1    # Bayer
    # curmaxid = 1096553786527703045 + 1    # Honeywell
    # curmaxid = 1096074662394646528 + 1    # 3M
    curmaxid = 1096523014223478784 + 1    # Honeywell
    for i in range(20):
        cur = api.user_timeline(screen_name='synchrony', count=200, max_id = curmaxid)
        for st in cur:
            res.append((st.created_at, st.text))
        curmaxid = cur[-1].id
        print(cur[-1].created_at)
        print(curmaxid)

    with open("sync", "wb+") as file:
        pickle.dump(res, file)
    # print(res)
