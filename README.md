# send-to-kodi-with-webui
This is a basic webpage which sends a video URL to a Kodi Media Player PC.

Only thing that you will need to change is the IP address' and names in the HTML page. The page can be changed @ ```/fws/templates/index.html```

Currently you can't provide login details for Kodi, Nor can you specify port.
If you want to change to port on line 21 in ```/fws/app.py``` Change "8080" to whichever port is most applicable for you.

To run this server use the command `python3 app.py`

Currently Kodi responses aren't shown. From a diagnostic standpoint that'd be good but currently that is not something that happens.