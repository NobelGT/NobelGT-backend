#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import datetime
import time

import config
from models import Course
from autobahn.twisted.websocket import WebSocketServerProtocol, \
    WebSocketServerFactory
from twisted.internet import reactor
from twisted.python import log
from solve2 import startSolution
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def datetimestrptime(time_string,time_fmt):
     t = time.strptime(time_string,time_fmt)
     return datetime.time(hour=t.tm_hour,minute=t.tm_min,second=t.tm_sec)

class NobelGTServerProtocol(WebSocketServerProtocol):
    def __init__(self):
        WebSocketServerProtocol.__init__(self)
        log.msg(u"[INFO] Starting new protocol instance")
        self.isCancelled = False

    def onConnect(self, request):
        print("Client connecting: {0}".format(request.peer))

    def onOpen(self):
        print("Incoming connection open.")

    def onMessage(self, payload, isBinary):
        if not isBinary:
            data = json.load(payload.decode('utf8'))

            if data.get("COMMAND") == "REQUEST":
                parameters = data.get("PARAMETERS")
                try:
                    self.startSolution(parameters)
                except ValueError as e:
                    self.sendError(e.message)
                    self.disconnect()


    def onClose(self, wasClean, code, reason):
        self.cancelSolution()
        print("WebSocket connection closed: {0}".format(reason))

    def startSolution(self, parameters):
        courses = parameters.get('listCourses')
        freeDays = parameters.get('freeDays')
        startTimeStr = parameters.get('startTime')
        endTimeStr = parameters.get('endTime')

        if courses is None:
            raise ValueError("You need to specify at least one course.")

        if freeDays is None:
            raise ValueError("You need to specify a number of desired free days.")

        if startTimeStr is None:
            raise ValueError("You need to specify a desired daily start time.")

        if endTimeStr is None:
            raise ValueError("You need to specify a desired daily end time.")

        courseData = courses.split(',')
        chosenCourses = []
        for courseItem in courseData:
            fullCourse = courseItem.strip()
            courseParts = fullCourse.split(" ")

            if len(courseParts) != 2:
                raise ValueError("You specified an invalid course: %s. It needs to be in the format of CS 1337: a department code and a class code, separated by a space." % fullCourse)

            dept = courseParts[0]
            code = courseParts[1]

            course = self.factory.session.query(Course).filter(Course.department_code == dept).filter(Course.course_number == code).first()

            if course is None:
                raise ValueError("A course you specified cannot be found: %s. Please make sure it is being offered this semester, at GT's Atlanta campus.")

            chosenCourses.append(course)

        if len(chosenCourses) == 0:
            raise ValueError("You must specify at least one course.")

        try:
            startTime = datetimestrptime(startTimeStr,"%I:%M %p")
        except ValueError:
            raise ValueError("You specified an invalid start time. It needs to be in the format of HH:MM (A/P)M: for example, 9:00 AM.")

        try:
            endTime = datetimestrptime(endTimeStr,"%I:%M %p")
        except ValueError:
            raise ValueError("You specified an invalid end time. It needs to be in the format of HH:MM (A/P)M: for example, 9:00 AM.")

        try:
            intFreeDays = int(freeDays)
            if intFreeDays <= 0:
                raise ValueError("Negative Value!")
        except ValueError:
            raise ValueError("You specified an invalid number of free days. It needs to be a positive integer.")

        reactor.callInThread(startSolution, self, chosenCourses, startTime, endTime, intFreeDays)

    def cancelSolution(self):
        self.isCancelled = True

    def sendProgress(self, schedule, score, progress):
        data = {}

        self.sendMessage(json.dump(data))

    def sendCompletion(self):
        data = {}

        self.sendMessage(json.dump(data))
        self.disconnect()

    def sendError(self):
        data = {}

        self.sendMessage(json.dump(data))

    def isCancelled(self):
        return self.isCancelled

    def cancelRealized(self):
        self.isCancelled = False

class NobelGTServerFactory(WebSocketServerFactory):
    protocol = NobelGTServerProtocol

    def __init__(self, url, session):
        WebSocketServerFactory.__init__(self, url)

        engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
        DBSession = sessionmaker(bind=engine)
        self.session = DBSession()

if __name__ == '__main__':
    import sys

    from twisted.python import log

    log.startLogging(sys.stdout)

    factory = NobelGTServerFactory(u"ws://127.0.0.1:9000")
    factory.protocol = NobelGTServerProtocol
    # factory.setProtocolOptions(maxConnections=2)

    # note to self: if using putChild, the child must be bytes...

    reactor.listenTCP(9000, factory)
    reactor.run()