import tweepy
import json

consumer_key = "SOlICITALA EN TWITTER"
consumer_secret = "SOlICITALA EN TWITTER"
access_token = "SOlICITALA EN TWITTER"
access_token_secret = "SOlICITALA EN TWITTER"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Llamadas al API
api = tweepy.API(auth)

#Obtener informacion de mi usario
data = api.me()
#print (data) #todo corrido
#Lo muestra mas ordenado en formato json
print json.dumps(data._json, indent=4)
