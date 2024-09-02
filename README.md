# site-monitor

Monitors a list of domains. This will check for a `200` response for each url on a list. You can control the cadence by running the `monitor.py` from a cron job.

## Getting Started

### Install Sengrd to send email notifications

Make sure to install sengrid as this uses it for sending email notifications. You will need a sendgrid api key, you can get one for free. There is good documentation about this [here](https://pypi.org/project/sendgrid/).

```sh
# Make sure to export the `SENDGRID_API_KEY`
pip install sendgrid
```

### Rename 2 files

Rename the files `sites_down.sample.json` and `sites.sample.json` to remove 'sample' from the name: `sites_down.json` and `sites.json`. These files will keep track of the sites that are down, and the list of sites to monitor, respectively.

### Add sites to monitor

To add or remove urls to/from the list of sites to monitor, use the respective scritps:

```sh
# Add a site
python3 add_domain.py

# Remove a site
python3 remove_domain.py
```

You will have to enter the whole url - i.e. `https://photon.software` - in order to add or remove sites. I will probably update this to be easier in the future. Maybe allow bulk updates, and simply passing the domain `photon.software` would be nice.

### Stort monitoring

When you are ready to start monitoring, push to a server and setup a cron job:

```sh
# Update the path below to match your system.
0 * * * * python3 ~/site-monitoring/monitor.py

# OR, You could do something a little fancier where you keep track of logs
0 * * * * /root/check_monitor.sh >> /root/site_monitor.log
```