# just-my-type-leaderboards<br />
Leaderboard backend written in Python using Flask<br />
<br />
Usage:<br />
1. Open up a UNIX-based command line terminal.<br />
2. Go through process of having Python2.7 or Python3+ installed, most Linux distros come with preinstalled.<br />
3. Do: pip install --upgrade pip setuptools<br />
4. Do: pip install Flask<br />
5. Clone this repository onto your UNIX based system.<br />
6. Do: python createdb.py<br />
7. Do: python leaderboards.py<br />
8. You should receive this: <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* Running on http://0.0.0.0:80/ (Press CTRL+C to quit)<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* Restarting with stat<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* Debugger is active!<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* Debugger pin code: 333-045-521<br />
9. You will now be able to locally access the server API by IP, 127.0.0.1.<br />
    Example: 127.0.0.1/jmt/typingtest/list will list the leaderboards for the TypingTest.<br />
10. In the JustMyType project, change the IPs in the LeaderboardHelper.swift to http://127.0.0.1<br />
  instead of http://bergcode.com if you want to run the system on your local machine.<br />
