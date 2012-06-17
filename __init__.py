#!/usr/bin/python
#By Rabih
#Translation by SullenLook

import os

def at_uptime():

     try:
         f = open( "/proc/uptime" )
         contents = f.read().split()
         f.close()
     except:
        return "Uptime Datei kann nicht geöffnet werden: /proc/uptime"

     total_seconds = float(contents[0])

     MINUTE  = 60
     HOUR    = MINUTE * 60
     DAY     = HOUR * 24

     days    = int( total_seconds / DAY )
     hours   = int( ( total_seconds % DAY ) / HOUR )
     minutes = int( ( total_seconds % HOUR ) / MINUTE )
     seconds = int( total_seconds % MINUTE )

     string = ""
     if days > 0:
         string += str(days) + " " + (days == 1 and "tag" or "tage" ) + ", "
     if len(string) > 0 or hours > 0:
         string += str(hours) + " " + (hours == 1 and "stunde" or "stunden" ) + ", "
     if len(string) > 0 or minutes > 0:
         string += str(minutes) + " " + (minutes == 1 and "minute" or "minuten" ) + ", "
     string += str(seconds) + " " + (seconds == 1 and "sekunde" or "sekunden" )

     return string;

from plugin import *
class uptime(Plugin):

    @register("de-DE", "(.*Betriebszeit.*)|(.*Serverstatus.*)|(.*Server.*)")
    def st_uptime(self, speech, language):
        if language == 'de-DE':
            self.say("SiriServer läuft seit" + at_uptime())
        self.complete_request()

