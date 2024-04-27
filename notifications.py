import json
import pathlib
from email_sender import Email_Sender

class Notification:
    cwd = pathlib.Path(__file__).parent.resolve()
    sites_list = cwd.as_posix() + "/sites.json"
    down_list = cwd.as_posix() + "/sites_down.json"

    sites = None
    sites_down = []

    sender = None

    def __init__(self) -> None:
        self.sender = Email_Sender()
        self.get_sites()
        self.get_down_list()
        self.check_down_list()
        self.update_list()

    def get_sites(self):
        list = open(self.sites_list, "r")
        self.sites = json.load(list)

    def get_down_list(self):
        list = open(self.down_list, "r")
        self.sites_down = json.load(list)
    
    def notify(self, domain: str):
        self.sender.try_send(domain, 'off')

    def check_down_list(self):
        if self.sites is not None:
            for u in self.sites:
                status = u["status"]
                doamin = u["domain"]
                if status == "off":
                    if doamin in self.sites_down:
                        # skip, we already notified
                        pass
                    else:
                        self.sites_down.append(doamin)
                        self.sender.try_send(doamin, 'off')
                else:
                    if doamin in self.sites_down:
                        self.sites_down.remove(doamin)
                        self.sender.try_send(doamin, 'on')

    def update_list(self):
        list = open(self.down_list, 'w')
        list.write(json.dumps(self.sites_down))

if (__name__ == '__main__'):
  Notification()