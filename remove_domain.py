import json
import pathlib

class Remove_Domain:
  cwd = pathlib.Path(__file__).parent.resolve()
  sites_list = cwd.as_posix() + "/sites.json"

  sites = []

  enter_url = 'Enter the url for the domain you would like to remove:\n'
  example = 'For example:  https://photon.software.\n'

  new_site_msg = enter_url + example

  def __init__(self) -> None:
    self.get_sites()

  def get_sites(self):
    _sites = open(self.sites_list, 'r')
    self.sites = json.load(_sites)
  
  def remove_site(self):
    url = input(self.new_site_msg)
    if url.count('://') == 0: 
      print('ERROR: Not a url')
      self.remove_site()
      return
    index = self.find_index(url)
    if (-1 == index): 
      print('ERROR: URL not found in sites.')
      return
    removed = self.sites.pop(index)
    print('Site removed: ', removed)
    print('New sites file: ', self.sites)
    self.update_sites()

  def find_index(self, url: str):
    for idx, site in enumerate(self.sites):
      if site["url"] == url:
        return idx
    return -1
  
  def update_sites(self):
    list = open(self.sites_list, 'w')
    list.write(json.dumps(self.sites))

if (__name__ == '__main__'):
  add = Remove_Domain()
  add.remove_site()
