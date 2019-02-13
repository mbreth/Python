import praw
import time

def main():
    reddit = praw.Reddit(client_id='client_id',
                         client_secret='client_secret',
                         user_agent='user_agent',
                         username='username',
                         password='password')


    subreddit = reddit.subreddit('all')

    for comment in subreddit.stream.comments():
        process_submission(comment)


def process_submission(comment):
    author = comment.author

    if (comment.body == 'Hello There' or comment.body == 'Hello there' or comment.body == 'hello there' or comment.body == 'Hello There!' or comment.body == 'Hello there!' or comment.body == 'hello there!'):
        print("General Kenobi Commented!")
        print("reddit.com" + comment.permalink)
        if (author != 'username'):
            time.sleep(10)
            comment.reply('General Kenobi')


    if (comment.body == 'I am the senate'):
        print('Chancellor Palpatine Commented!')
        print('reddit.com' + comment.permalink)
        if (author != 'username'):
            time.sleep(10)
            comment.reply('Not yet')


if __name__ == '__main__':
main()
