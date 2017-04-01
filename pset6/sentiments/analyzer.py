import nltk



class Analyzer():
    """Implements sentiment analysis."""
    
    pos_words = []
    neg_words = []


    def __init__(self, positives, negatives):
        """Initialize Analyzer."""

        # list of positive words
        with open(positives) as fp:
            for i, line in enumerate(fp):
                if i > 34:
                    self.pos_words.append(line)
                elif i > 2041:
                    break

        # list of negative words
        with open(negatives) as fp:
            for i, line in enumerate(fp):
                if i > 35:
                    self.neg_words.append(line)
                elif i > 4818:
                    break

        # strip newlines from words
        self.pos_words = [x.strip('\n') for x in self.pos_words]
        self.neg_words = [x.strip('\n') for x in self.neg_words] 
        
        
        

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        # strip newlines and puncuation from each word in list, and initialize score variable
        user_tweets = [x.strip('\n').strip(',').strip('.') for x in text] # a list of tweets
        score = 0
        
        # for each tweet:
        for tweet in user_tweets:
            
            # split the tweet into an array of words
            tweet = tweet.split()

            # for each word in tweet:
            for word in tweet:
                
                # run the scoring loop
                if word in self.pos_words:
                    score += 1
                elif word in self.neg_words:
                    score -= 1        

         
        return score
        
    def analyze_single_tweet(self, text):
        """Analyze text for sentiment, returning its score."""
        # strip newlines and puncuation from each word in list, and initialize score variable
        user_tweet = [x.strip('\n').strip(',').strip('.') for x in text] # a list of characters
        user_tweet = "".join(user_tweet)
        user_tweet = user_tweet.split()
        score = 0
        
       # split the tweet into an array of words
        # tweet = user_tweet.split()

        # for each word in tweet:
        for word in user_tweet:
                
            # run the scoring loop
            if word in self.pos_words:
                score += 1
            elif word in self.neg_words:
                score -= 1        
         
        return score   
