import json
import urllib
import urllib.request
import pathlib
from notifications import Notification

class Monitor:
  cwd = pathlib.Path(__file__).parent.resolve()
  sites_list = cwd.as_posix() + "/sites.json"

  sites = None

  def __init__(self) -> None:
    self.get_sites()
    self.check_sites()
    self.update_sites()

  def get_sites(self):
    _sites = open(self.sites_list, 'r')
    self.sites = json.load(_sites)
  
  def check_sites(self):
    if self.sites is not None:
      for u in self.sites:
          print(u)
          try:
            self.check_url(u["url"])
            u["status"] = "on"
          except Exception as err:
            print('Error', err)
            u["status"] = "off"
  
  def update_sites(self):
    list = open(self.sites_list, 'w')
    list.write(json.dumps(self.sites))

  def check_url(self, host):
      print(host)
      url = urllib.request.urlopen(host)
      return 200 == url.getcode()

if (__name__ == '__main__'):
  Monitor()
  Notification()