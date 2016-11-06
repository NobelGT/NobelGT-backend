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

engine = create_engine(config.SQLALCHEMY_DATABASE_URI, connect_args={'check_same_thread': False})
DBSession = sessionmaker(bind=engine)

def datetimestrptime(time_string,time_fmt):
     t = time.strptime(time_string,time_fmt)
     return datetime.time(hour=t.tm_hour,minute=t.tm_min,second=t.tm_sec)

class NobelGTServerProtocol(WebSocketServerProtocol):
    def __init__(self):
        WebSocketServerProtocol.__init__(self)
        log.msg(u"[INFO] Starting new protocol instance")
        self.cancelled = False
        self.session = DBSession()


    def onConnect(self, request):
        log.msg("Client connecting: {0}".format(request.peer))

    def onMessage(self, payload, isBinary):
        if not isBinary:
            data = json.loads(payload.decode('utf8'))

            if data.get("COMMAND") == "REQUEST":
                parameters = data.get("PARAMETERS")
                try:
                    self.startSolution(parameters)
                except ValueError as e:
                    self.sendError(e.message)


    def onClose(self, wasClean, code, reason):
        self.cancelSolution()
        self.session.close()

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
        credits = 0
        for courseItem in courseData:
            fullCourse = courseItem.strip()
            courseParts = fullCourse.split(" ")

            if len(courseParts) != 2:
                raise ValueError("You specified an invalid course: %s. It needs to be in the format of CS 1337: a department code and a class code, separated by a space." % fullCourse)

            dept = courseParts[0]
            code = courseParts[1]

            course = self.session.query(Course).filter(Course.department_code == dept).filter(Course.course_number == code).first()

            if course is None:
                raise ValueError("A course you specified cannot be found: %s. Please make sure it is being offered this semester, at GT's Atlanta campus." % fullCourse)

            chosenCourses.append(course)
            credits = credits + course.credit_hours

        if credits > 21:
            raise ValueError("At Georgia Tech, you can only take up to 21 credit hours. Your current selection adds up to $d." % credits)

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
            if intFreeDays < 0:
                raise ValueError("Negative Value!")
        except ValueError:
            raise ValueError("You specified an invalid number of free days. It needs to be a nonnegative integer.")

        reactor.callInThread(startSolution, self, chosenCourses, startTime, endTime, intFreeDays)

    def cancelSolution(self):
        self.cancelled = True

    def sendProgress(self, progress, sections=None, timeEquivalencies=None, score=None):
        data = {"COMMAND": "PROGRESS"}
        parameters = {'progress': progress}

        if sections is not None and timeEquivalencies is not None and score is not None:
            courses = []

            for section in sections:
                code = section.course.department.code + " " + section.course.course_number
                creditHours = section.course.credit_hours
                name = section.course.name

                timeEquivalents = []
                timeEquivalents.append({
                    'crn' : section.crn,
                    'code' : section.code
                })

                foundEquivalents = timeEquivalencies.get(section)
                if foundEquivalents is not None:
                    for equivalent in foundEquivalents:
                        timeEquivalents.append({
                            'crn' : equivalent.crn,
                            'code' : equivalent.code
                        })

                sessions = []
                for sess in section.sessions:
                    sessions.append({
                        'day' : sess.day,
                        'instructors' : sess.instructors,
                        'location' : sess.location.name + " " + sess.room,
                        'type' : sess.type,
                        'startTime' : sess.start_time.strftime("%I:%M %p"),
                        'endTime' : sess.end_time.strftime("%I:%M %p")
                    })


                courseObject = {'code': code, 'name': name, 'credit_hours': creditHours, 'sessions': sessions, 'sections': timeEquivalents}
                courses.append(courseObject)

            parameters['score'] = score
            parameters['courses'] = courses

        data["PARAMETERS"] = parameters
        self.sendMessage(json.dumps(data))

    def sendCompletion(self):
        data = {"COMMAND": "COMPLETION"}

        self.sendMessage(json.dumps(data))
        self.sendClose()

    def sendError(self, error):
        data = {"COMMAND": "ERROR", "PARAMETERS": {"MESSAGE": error}}

        self.sendMessage(json.dumps(data))
        self.sendClose()

    def isCancelled(self):
        return self.cancelled

    def cancelRealized(self):
        self.cancelled = False

class NobelGTServerFactory(WebSocketServerFactory):
    protocol = NobelGTServerProtocol

    def __init__(self, url):
        WebSocketServerFactory.__init__(self, url)

if __name__ == '__main__':
    import sys

    log.startLogging(sys.stdout)

    factory = NobelGTServerFactory(u"ws://127.0.0.1:9000")

    reactor.listenTCP(9000, factory)
    reactor.run()