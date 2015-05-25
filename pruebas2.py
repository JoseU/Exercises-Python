import tweepy

consumer_key = 'O82viv9gqRgStE2FKzPswFDH0'
consumer_secret = 'wr78xh1jgVB01k7yJTY14yPuzfyo8QDXr4IKEBes8BdiSWnbcl'
access_token = '197481156-OufHbI2EdEp32mF9rQGCftl9pcFbiWrmKWyWGEAe'
access_token_secret = 'MXjqQaUCGXtwFZImYh4JYaPUPORGIkM6FUVxRHah5VCYw'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

jose = tweepy.API(auth)

jose.update_status(status='probando tweetpy para el #ea5')
