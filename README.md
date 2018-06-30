# Check-N-Download

A program for automatically downloading images and videos submitted by a Reddit user.

### Requirements:
* **Python 3** - For installation see [here](https://www.python.org/downloads/).
* **pip** for Python 3 - For installation see [here](https://packaging.python.org/guides/installing-using-linux-tools/#installing-pip-setuptools-wheel-with-linux-package-managers) and [here](https://pip.pypa.io/en/stable/installing/).
* **PRAW** - Install by running `pip3 install praw`.

### Obtaining Reddit API access credentials:
1. Create a [Reddit](https://www.reddit.com/) account, and while logged in, navigate to preferences > apps.
2. Click on the **are you a developer? create an app...** button.
3. Fill in the details:
    * name: Name of your bot/script
    * Select the option 'script'
    * decription: Put in a description of your bot/script
    * redirect uri: `http://localhost:8080`
4. Click **create app**.
5. You will be given a `client_id` and a `client_secret`. Keep them confidential.

### How to run it:
1. Clone this repository and navigate to its directory.
2. Install necessary packages.
2. Run `python3 check_n_download.py` to start the program.
3. A file named *praw.ini* will be created in the current directory of the program.
4. Enter the values needed in *praw.ini*.
5. Run `python3 check_n_download.py` again.

### Additional notes:
1. Due to Reddit API restrictions, accounts with more than 1000 submissions won't work. 
2. The program currently only works for files that are directly linked and which address ends with a known file format.
3. Files downloaded using this program may, or may not be copyrighted, use with caution.
