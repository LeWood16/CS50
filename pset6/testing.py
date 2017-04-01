test_tweet = "Oh man let me tell you my hands are so big, so yuuuge. Everybody tells me that, I have a lot of people call me every day and tell me that, believe me. This wall's gonna be amazing, let me tell you. It's gonna be so big, big as my hands."

test_words = test_tweet.split()

positive_words = []
negative_words = []
score = 0
positive = 0
negative = 0
neutral = 0

# list of positive words
with open("sentiments/positive-words.txt") as fp:
    for i, line in enumerate(fp):
        if i > 34:
            positive_words.append(line)
        elif i > 2041:
            break

# list of negative words
with open("sentiments/negative-words.txt") as fp:
    for i, line in enumerate(fp):
        if i > 35:
            negative_words.append(line)
        elif i > 4818:
            break

# strip any punctuation from words
positive_words = [x.strip('\n') for x in positive_words] # strip newlines from each word in list
negative_words = [x.strip('\n') for x in negative_words] # strip newlines from each word in list
test_words = [x.strip('\n').strip(',').strip('.') for x in test_words] # strip newlines from each word in list

# increment counters of positive, negative and neutral words, along with the overall score
for word in test_words:
    if word in positive_words:
        score += 1
        positive += 1
    elif word in negative_words:
        score -= 1
        negative += 1
    else:
        neutral += 1
        
        
# output scores to console for testing
print("score:", score)
print("positive words:", positive)
print("negative words:", negative)
print("neutral words:", neutral)




