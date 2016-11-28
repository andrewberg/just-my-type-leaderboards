# just-my-type-leaderboards
Leaderboard backend written in Python using Flask

Usage:
1. Open up a UNIX-based command line terminal.
2. Go through process of having Python2.7 or Python3+ installed, most Linux distros come with preinstalled.
3. Do: pip install --upgrade pip setuptools
4. Do: pip install Flask
5. Clone this repository onto your UNIX based system.
6. Do: python createdb.py
7. Do: python leaderboards.py
8. You should receive this: 
      * Running on http://0.0.0.0:80/ (Press CTRL+C to quit)
      * Restarting with stat
      * Debugger is active!
      * Debugger pin code: 333-045-521
9. You will now be able to locally access the server API by IP, 127.0.0.1.  
    Example: 127.0.0.1/jmt/typingtest/list will list the leaderboards for the TypingTest.
10. In the JustMyType project, change the IPs in the LeaderboardHelper.swift to http://127.0.0.1
  instead of http://bergcode.com if you want to run the system on your local machine.
