import twitter

Consumer_Key = "LNRbeqliwFZ8iTzvVRcSawGzW"
Consumer_Secret = "GORPrOup5vshpX0vZdXBhgQhE802ZnWq2SUl7n18EtGSPMvvwr"
access_token="1625107172-rYB3w3hsk31flSvvySz11h79Tyu4NtiDSJVkmjl"
access_token_secret="2omF1qK3Q8LR59580eOuSpSp8WQDoaOM0XdQfneHGuddI"

api = twitter.Api(consumer_key=consumer_key,
                consumer_secret=consumer_secret,
                access_token_key=access_token,
                access_token_secret=access_secret)


print(api.VerifyCredentials())


follwers = api.GetFollowers()
friends = api.GetFriends()