import datetime
import os
import random
from slackclient import SlackClient
import sqlite3
import sys
import time


slack_token = os.environ["SLACK_API_TOKEN"]
sc = SlackClient(slack_token)

methodDict = {}

#helpMessage apparently crashes the slack client...
helpMsg = "The slack bot searches for keywords in your messages for replies. You can ask it various questions such as when are the meetings, what are today's Rosary mysteries, or who is the Grand Knigt. As well as various other useful information including Knight's mass sign up link, meeting minutes, and prayer requests that brothers have added. Try '--help' for a complete list of commands"
commandMsg = "List of keywords that the bot searches for (All commands are case insensitive):\nhelp\nmeeting minutes\nbusiness meeting\nmass\ncalendar\nrosary mysteries\nwhat's the good word\nhow about them dawgs\nrussian roulette\ndice roll\nrandom number\ncoin flip\nwho is (officer or director position)\nlist prayer requests\nadd prayer request\ndelete prayer request\nrequest feature\nlist degrees\nlist first degrees\nlist second degrees\nlist third degrees"
meetingMsg = "Meetings are the First Thursday of every month at 7pm in the Classroom at the CC(if you don't know where that is start in the basement and someone should be able to help you)! Please remember to bring your Membership Card and Rosary!!!!!!!"
#minutesMessage also does not work...
#                                                                                                                                                                                           spacing here is to force new line break
requestMsg = "This Slack bot is in continuous development. If you have an idea or believe something should be changed feel free to message '@will' on Slack or message the bot with keyword request and \n\"<Request here in strings>\""
calendarMsg = "Public Calendar for all events for the Fraternal year can be found at this link https://calendar.google.com/calendar/embed?src=ekacorqf8u5djofr8egll3il4s%40group.calendar.google.com&ctz=America/New_York"

joyfulMsg = "The Joyful Mysteries Are:\n1. The Anunciation\n2. The Visitation\n3. The Nativity\n4.The Presentation of Jesus in the Temple\n5. The Finding of Jesus in the Temple"
sorrowfulMsg = "The Sorrowful Mysteries Are:\n1. The Agony of Jesus in the Garden\n2. The Sourging at the Pillar\n3. The Crowning with Thorns\n4. Jesus Carrying the Cross\n5. The Crucifixion of our Lord"
gloriousMsg = "The Glorious Mysteries Are:\n1. The Resurrection of Jesus Christ\n2. The Acension of Jesus to Heaven\n3. The Descent of the Holy Spirit at Pentecost\n4. The Assumption of Mary into Heaven\n5. Mary is Crowned as Queen of Heaven and Earth"
luminousMsg = "The Luminous Mysteries Are:\n1. The Baptism in the Jordan\n2. The Wedding at Cana\n3. The Proclamation of the Kingdom of God\n4. The Transiguration\n5. The Institution of the Eucharist"

canonizationPrayer = """God, our Father, protector of the poor and
defender of the widow and orphan, you called
your priest, Father Michael J. McGivney, to
be an apostle of Christian family life and to
lead the young to the generous service of their
neighbor. Through the example of his life and
virtue may we follow your Son, Jesus Christ,
more closely, fulfilling his commandment of
charity and building up his Body which is the
Church. Let the inspiration of your servant
prompt us to greater confidence in your love
so that we may continue his work of caring
for the needy and the outcast. We humbly
ask that you glorify your venerable servant
Father Michael J. McGivney on earth
according to the design of your holy will.
Through his intercession, grant the favor I
now present (here make your request).
Through Christ our Lord. Amen.
Our Father, Hail Mary, and Glory Be """ 



#sc.rtm_connect()

def helpMessage(channel):
    sc.rtm_send_message(channel, helpMsg)

methodDict['help'] = helpMessage

def minutesMessage(channel):
    sc.rtm_send_message(channel, minutesMsg)

methodDict['minutes'] = minutesMessage

def meetingMessage(channel):
    sc.rtm_send_message(channel, meetingMsg)

methodDict['meeting'] = meetingMessage

def massMessage(channel):
    sc.rtm_send_message(channel, massMsg)

methodDict['mass'] = massMessage

def requestMessage(channel):
    sc.rtm_send_message(channel, requestMsg)

methodDict['request'] = requestMessage

def calendarMessage(channel):
    sc.rtm_send_message(channel, calendarMsg)

methodDict['calendar'] = calendarMessage

def joyfulMessage(channel):
    sc.rtm_send_message(channel, joyfulMsg)

methodDict['joy'] = joyfulMessage

def sorrowfulMessage(channel):
    sc.rtm_send_message(channel, sorrowfulMsg)

methodDict['sorrow'] = sorrowfulMessage

def gloriousMessage(channel):
    sc.rtm_send_message(channel, gloriousMsg)

methodDict['glorious'] = gloriousMessage

def luminousMessage(channel):
    sc.rtm_send_message(channel, luminousMsg)

methodDict['luminous'] = luminousMessage




