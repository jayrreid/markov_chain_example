__author__ = 'jrreid'
from fetch_data import fetch_tweets
from markov_python.cc_markov import MarkovChain

# Essentially, the state transition from one state to another is probability based.
# In the case of a text-based Markov Chain, the transition probability is based on the
# frequency of words following the selected word. So the selected word represents
# the previous state and the frequency table or words represents the (possible) successive states.
# You find the successive state if you know the previous state (that's the only way you get
# the right frequency table), so this fits in with the definition where
# the successive state is dependent on the previous state.


#@realdonaldtrump
#@Donald_Trump_16
#@BarackObama
#@CameronNewton
#@KingJames
#@StephenCurry30

twitter_handle = raw_input("Enter Twitter Handle (specify @handle_name): ")
mc = MarkovChain()

tweets = fetch_tweets(twitter_handle)
for tweet in tweets:
    mc.add_string(tweet)

nextTweet= mc.generate_text(100)
print "\n"
print "Using Markov Chain. Here's the next possible tweet for " + twitter_handle
print " ".join(nextTweet)
