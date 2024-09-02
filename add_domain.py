import json
import pathlib

class Add_Domain:
  cwd = pathlib.Path(__file__).parent.resolve()
  sites_list = cwd.as_posix() + "/sites.json"

  sites = None

  enter_url = 'Enter the url for the domain you would like to add:\n'
  example = 'For example:  https://photon.software.\n'

  new_site_msg = enter_url + example

  def __init__(self) -> None:
    self.get_sites()
    self.start()

  def get_sites(self):
    _sites = open(self.sites_list, 'r')
    self.sites = json.load(_sites)
    _sites.close()
  
  def start(self):
    url = input(self.new_site_msg)
    url_a = url.split(',')
    for s in url_a:
      self.add_site(s)
    self.update_sites()
  
  def add_site(self, url: str):
    if url.count('://') == 0: 
      print('ERROR: Not a url')
      self.start()
      return
    urlA = url.split('://')
    newSite = {
      "status": "unset",
      "protocol": urlA[0],
      "domain": urlA[1],
      "url": url,
    }
    print('Adding the following site: ', newSite)
    self.sites.append(newSite)
  
  def update_sites(self):
    list = open(self.sites_list, 'w')
    list.write(json.dumps(self.sites))
    list.close()

if (__name__ == '__main__'):
  Add_Domain()
