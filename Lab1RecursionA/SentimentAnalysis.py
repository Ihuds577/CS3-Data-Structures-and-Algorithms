import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import praw

positiveCommentList = []
negativeCommentList = []
neutralCommentList = []

reddit = praw.Reddit(client_id='n9GmTDulB-QDGQ',
                     client_secret='9zeh2ofqXUooI4gjH8WZzv8vxAc',
                     user_agent='my user agent'
                     )


nltk.download('vader_lexicon')
sid = SentimentIntensityAnalyzer()


def get_text_negative_proba(text):
   return sid.polarity_scores(text)['neg']


def get_text_neutral_proba(text):
   return sid.polarity_scores(text)['neu']


def get_text_positive_proba(text):
   return sid.polarity_scores(text)['pos']


def get_submission_comments(url):
    submission = reddit.submission(url=url)
    submission.comments.replace_more()

    return submission.comments


def main():

    commentsModerate = get_submission_comments('https://www.reddit.com/r/learnprogramming/comments/5w50g5/eli5_what_is_recursion/')
    commentsLarge = get_submission_comments('https://www.reddit.com/r/funny/comments/9fca26/my_dad_and_brother_recreated_this_photo_26_years/')
    commentsSmall = get_submission_comments('https://www.reddit.com/r/SuggestALaptop/comments/8e4l23/laptop_for_a_computer_science_undergrad/')


    # Test cases for a post with a small number of comments, moderate number of comments, and significantly large number of comments

    #processComments(commentsLarge)
    #processComments(commentsModerate)
    processComments(commentsSmall)

    print(len(commentsSmall))

    # Used to test and check the number of comments collected on each list
    print(len(positiveCommentList), len(negativeCommentList), len(neutralCommentList))


def processComments(comments):

    # The for loop functions as a base case and iterates through the initial comment lists
    for i in range(len(comments)):
        print(comments[i].body)
        neg = get_text_negative_proba(comments[i].body)
        pos = get_text_positive_proba(comments[i].body)
        if (neg >= 0.15):
            negativeCommentList.append(comments[i].body)
        elif (pos >= 0.15):
            positiveCommentList.append(comments[i].body)
        else:
            neutralCommentList.append(comments[i].body)
        if len(comments[i].replies) != 0:
            # Recursive call that covers traversing the replies themselves
            processComments(comments[i].replies)


# Calling the main method
main()