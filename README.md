# send-to-kodi-with-webui
The ability to send links to kodi via a webpage

I found a script from https://github.com/allejok96/send-to-kodi which was a shell script of sending videos to Kodi. Which was great. However i didn't want to ssh onto a machine to then paste a link to be able to watch it on my media machine. So I thought what if i could do it from a web interface.

I'm not the best at this stuff, but the way I wanted to play around on getting this working was use the shell script and pass form data to the script which then sent the link to the media machine.

I got it working.... ish. There seems to be an issue where a forward slash "/" (and also semi-colon ";" but not as much of an issue) coupled with a number between 1-7 would cause a specific character to replace the two characters.
I'm not entirely sure if it's due to the shell script processing the form data, a quirk of linux shell or an apache/html thing. If you think you can fix it let me know. I'm sure it'd be a great help. If you need some assistance or want me to make the form page better looking let me know.

I used apache2 for the server and "a2enmod cgid" enables cgi scripts.

Directories:
/usr/lib/cgi-bin
/var/www/html
