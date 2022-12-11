import tweepy
import random 
from secrets_1 import consumer_key, consumer_secret, access_token, access_token_secret

# Authenticate with the Twitter API using your app's keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Generate a random quote from Stephen Hawking

quotes = [
    "The greatest enemy of knowledge is not ignorance, it is the illusion of knowledge.",
    "Look up at the stars and not down at your feet. Try to make sense of what you see, and wonder about what makes the universe exist. Be curious.",
    "Intelligence is the ability to adapt to change.",
    "We are just an advanced breed of monkeys on a minor planet of a very average star. But we can understand the Universe. That makes us something very special.",
    "However difficult life may seem, there is always something you can do and succeed at.",
    "The universe doesn't allow perfection.",
    "The human race is just a chemical scum on a moderate-sized planet, orbiting around a very average star in the outer suburb of one among a hundred billion galaxies.",
    "We only have to look at ourselves to see how intelligent life might develop into something we wouldn't want to meet.",
    "Life would be tragic if it weren't funny.",
    "I have noticed that even people who claim everything is predetermined and that we can do nothing to change it, look before they cross the road.",
]

random_quote = random.choice(quotes)

# Post the quote as a tweet
api.update_status(random_quote)
