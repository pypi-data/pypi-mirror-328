#!/usr/bin/env python3

from fire import Fire
from console import fg, bg
import shutil
import os
import datetime as dt
import shlex
import subprocess as sp


#=========================================================================
#
#-------------------------------------------------------------------------
#

def enter_screen(scrname):
    """
    it enters when run from here
    """
    sessions = list_screen_sessions()
    print(sessions)
    print(scrname)
    if is_in_screen(scrname, sessions):
        CMD = f"screen -x {scrname}"
        args = shlex.split(f"xterm -e bash -c '{CMD}'")
        process = sp.Popen(args,  stdout=sp.DEVNULL, stderr=sp.DEVNULL)
        process.poll()

#=========================================================================
#
#-------------------------------------------------------------------------
#

def stop_screen(scrname):
    """
    it enters when run from here
    """
    sessions = list_screen_sessions()
    print(sessions)
    print(scrname)
    if is_in_screen(scrname, sessions):
        CMD = f"screen -X -S {scrname} quit"
        args = shlex.split(f"xterm -e bash -c '{CMD}'")
        process = sp.Popen(args,  stdout=sp.DEVNULL, stderr=sp.DEVNULL)
        process.poll()


#=========================================================================
#
#-------------------------------------------------------------------------
#

def list_screen_sessions():
    """
    return the existing screen sessions
    """
    try:
        result = sp.run(['screen', '-ls'], capture_output=True, text=True, check=True)
        #print(result.stdout)
        return result.stdout.strip().split('\n')[1:-1]
    except sp.CalledProcessError as e:
        #print(f"x... screen ls - error occurred: {e}")
        return None




#=========================================================================
#
#-------------------------------------------------------------------------
#

def is_in_screen(TAG, sessions):
    """
    if tag in screen list => True
    """
    if sessions is None:return False
    for i in sessions:
        #print(i, TAG, i.find(TAG) )
        if i.find(TAG) > 0:
            return True
    return False

#=========================================================================
#
#-------------------------------------------------------------------------
#


def del_job_anycommand( cron, tag):
    """
    older
    """
    ACT = False
    RMTG = f"screen -dmS {tag} " #SPACE IMPORTANT
    for job in cron:
        if job.command.find(RMTG) > 0:
            print(f"i... removing /{RMTG}/ ")#... {job}")
            cron.remove(job)
            ACT = True
    if ACT:
        cron.write()

if __name__ == "__main__":
    Fire({"e": enter_screen
        }
         )
