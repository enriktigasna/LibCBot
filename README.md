# LibC Bot written in python
https://twitter.com/LibCBot1

Tweets a explanation of an stdlib C function every 30 minutes

The documentation for the C functions was taken from taken from https://www.ibm.com/docs/en/i/7.1?topic=extensions-standard-c-library-functions-table-by-name and formatted into JSON in functions.json.

## Setup
``git clone https://github.com/enriktigasna/LibCBot``

``python -m pip install -r requirements.txt``

Get your twitter API credentials from https://developer.twitter.com/en/portal and 

Copy ``config example.json`` into ``config.json`` and change the credentials.

Just run main.py and the bot should be up without any issues, if you run into any problems please report them in this repositories Issues.

## Personal use guidelines.

You are free to use this for your own reasons, and it can be very useful if you just want to make your own bot, and rename and change the functions.json + the formatting.

Join the [discord](https://discord.gg/tAVnyWdK9X) and ping me if you want help with that-

Follow the GPL 3.0 when using and forking. I would really appreciate it if you credited me aswell.