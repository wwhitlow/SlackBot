import datetime
#Imports messages from another python file
from messages import *
import os
import random
from slackclient import SlackClient
import sqlite3
import sys
import time

slack_token = os.environ["SLACK_API_TOKEN"]
sc = SlackClient(slack_token)

date = datetime.datetime.today()

    
def parseMessage():
    if "--help" in lowercaseString:
        sc.rtm_send_message(message[u'channel'], commandMsg)
    elif "help" in lowercaseString:
        sc.rtm_send_message(message[u'channel'], helpMsg)

    if "meeting" in lowercaseString or "business" in lowercaseString:
        if "minutes" in lowercaseString:
            sc.rtm_send_message(message[u'channel'], minutesMsg)
        else:
            sc.rtm_send_message(message[u'channel'], meetingMsg)

    if "mass" in lowercaseString:
        sc.rtm_send_message(message[u'channel'], massMsg)

    if "calendar" in lowercaseString:
        sc.rtm_send_message(message[u'channel'], calendarMsg)

    if "rosary" in lowercaseString or "mystery" in lowercaseString or "mysteries" in lowercaseString:
        weekday = date.weekday()
        if (weekday == 0 or weekday == 5):
            sc.rtm_send_message(message[u'channel'], joyfulMsg)
        elif (weekday == 1 or weekday == 4):
            sc.rtm_send_message(message[u'channel'], sorrowfulMsg)
        elif (weekday == 2 or weekday == 6):
            sc.rtm_send_message(message[u'channel'], gloriousMsg)
        else:
            sc.rtm_send_message(message[u'channel'], luminousMsg)

    if "what's the good word" in lowercaseString:
        sc.rtm_send_message(message[u'channel'], THWg)
    if "how about them dawgs" in lowercaseString or "how about them dogs" in lowercaseString:
        sc.rtm_send_message(message[u'channel'], pissOnThem)

    if "dice roll" in lowercaseString:
        sc.rtm_send_message(message[u'channel'], "Dice Value: " + str(random.randint(1,6)))
    if "random number" in lowercaseString:
        sc.rtm_send_message(message[u'channel'], "True Random Number " + str(random.randint(-sys.maxint, sys.maxint)))
    if "coin flip" in lowercaseString:
        coin = random.randint(0,1)
        if (coin):
            sc.rtm_send_message(message[u'channel'], "Heads")
        else:
            sc.rtm_send_message(message[u'channel'], "Tails")



if sc.rtm_connect():
    #Starts scanning loop
    while True:
        json = sc.rtm_read()
        if len(json) == 1:
            message = json[0]
            #print message have Andrew DM bot to see what stays constant
            #Confirms that the api response contains text from a user to parse
            if u'text' in message.keys() and u'channel' in message.keys():
                #print message
                #Message in lowercase to ignore funky spelling
                lowercaseString = message[u'text'].lower()
                #Checks to see if lackeybot is mentioned in the text
                if "lackeybot" in lowercaseString or "@u5gqdkhn2" in lowercaseString or message[u'channel'][0] == "D" and message[u'user'] != "U5GQDKHN2":
                    #Searches for keywords in messages
                    if "request" in lowercaseString or "requests" in lowercaseString:
                        if "prayer" in lowercaseString:
                            conn = sqlite3.connect('.kofcDb.db')
                            c = conn.cursor()
                            if "delete" in lowercaseString or "remove" in lowercaseString and '"' in lowercaseString:
                                rm = message[u'text'].split('"')
                                rf = (message[u'user'], rm[1],)
                                c.execute("DELETE FROM requests WHERE user_id = ? AND prayer_intention = ?", rf)
                                conn.commit()
                                sc.rtm_send_message(message[u'channel'], "Delete Command Run!")
                            elif "add" in lowercaseString:
                                request = message[u'text'].split('"')
                                pR = (message[u'user'], request[1], date.now(),)
                                c.execute("INSERT INTO requests VALUES (?,?,?)", pR)
                                conn.commit()
                            elif "list" in lowercaseString:
                                c.execute('SELECT * FROM requests')
                                requests = c.fetchall()
                                msg = "List of Prayer Requests Submitted by the Council:"
                                for req in requests:
                                    msg =  msg + "\n" + req[1]
                                sc.rtm_send_message(message[u'channel'], msg)
                                sc.rtm_send_message(message[u'channel'], "Consider saying this prayer for the above requests:\n" + canonizationPrayer)
                            else:
                                sc.rtm_send_message(message[u'channel'], requestMessage)
                            conn.close()
                        elif "feature" in lowercaseString:
                            if '"' in lowercaseString:
                                request = message[u'text'].split('"')
                                sc.rtm_send_message(message[u'channel'], "Your request has been recorded and forwarded to '@will' current developer")
                                sc.rtm_send_message("D5FDFE517", "New Feature Idea: " + request[1])
                            else:
                                sc.rtm_send_message(message[u'channel'], requestMessage)
                        else:
                            sc.rtm_send_message(message[u'channel'], "Sorry couldn't parse request make sure to differentiate between a prayer and feature request")
                    else:
                        parseMessage()
        time.sleep(1)
else:
    print("Connection Failed")
