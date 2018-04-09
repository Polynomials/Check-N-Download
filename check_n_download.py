import praw
import os
import sys
import time
import configparser
import urllib.request


def create_config():
    config = configparser.ConfigParser()
    if os.path.isfile(f"{str(os.getcwd())}/praw.ini") is False:
        print("praw.ini not found. Creating...")
        file = open("praw.ini", "w+")
        config["Authentication"] = {"username": "Your reddit username",
                                    "password": "Your reddit password",
                                    "client_id": "Find at: https://www.reddit.com/prefs/apps",
                                    "client_secret": "Find at: https://www.reddit.com/prefs/apps"}
        config["Settings"] = {"path": "The path for saving the fetched items"}
        config["Users"] = {"user": "What user do you want to check?"}
        config.write(file)
        print("praw.ini created! Please enter your values to the file.")
        for second in range(5, 0, -1):
            print("Exiting program in: " + str(second))
            time.sleep(1)
        sys.exit(0)
    elif os.path.isfile(f"{str(os.getcwd())}/praw.ini") is True:
        config.read("praw.ini")
        print("praw.ini found! Proceeding with download...")
    get_settings()


def get_settings():
    config = configparser.ConfigParser()
    config.read("praw.ini")
    get_settings.path = config["Settings"]["path"]
    get_settings.user = config["Users"]["user"]


def authenticate():
    reddit = praw.Reddit("Authentication", user_agent="Check'N'Download-Reddit")
    return reddit


def download_submissions(path, post_id, url):
    if url[-4:] == ".jpg" or url[-4:] == ".png" or url[-5:] == ".jpeg":
        name = os.path.join(path, str(post_id) + ".png")
        urllib.request.urlretrieve(url, name)
    elif url[-4:] == ".mp4" or url[-5:] == ".webm" or url[-4:] == ".wmv":
        name = os.path.join(path, str(post_id) + ".mp4")
        urllib.request.urlretrieve(url, name)
    elif url[-4:] == ".gif":
        name = os.path.join(path, str(post_id) + ".gif")
        urllib.request.urlretrieve(url, name)
    else:
        exception_url = open(f"{get_settings.path}/{get_settings.user}-links.txt", "a+")
        exception_url.write(f"{url}\n")


def initialization(path, user):
    old_submission_amount = 0
    for submission in user.submissions.new(limit=None):
        download_submissions(path, submission.id, submission.url)
        old_submission_amount += 1
        time.sleep(2)
    print("Initialization successful!")
    print("Submission amount: " + str(old_submission_amount))
    return old_submission_amount


def check_submissions(path, user, old_submission_amount):
    while True:
        new_submission_amount = 0
        for submission in user.submissions.new(limit=None):
            new_submission_amount += 1

        if old_submission_amount < new_submission_amount:
            print("\n" + time.strftime("%H:%M:%S ") + "New submission found!")
            print("Old submission amount: " + str(old_submission_amount))
            print("New submission amount: " + str(new_submission_amount))
            old_submission_amount = 0
            for submission in user.submissions.new(limit=None):
                download_submissions(path, submission.id, submission.url)
                old_submission_amount += 1
        elif old_submission_amount > new_submission_amount:
            print("\n" + time.strftime("%H:%M:%S ") + "Submission removed!")
            print("Old submission amount: " + str(old_submission_amount))
            print("New submission amount: " + str(new_submission_amount))
            old_submission_amount = 0
        time.sleep(10)


def main():
    create_config()
    reddit = authenticate()
    path = get_settings.path
    user = reddit.redditor(get_settings.user)
    old_submission_amount = initialization(path, user)
    check_submissions(path, user, old_submission_amount)


if __name__ == "__main__":
    main()