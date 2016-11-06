#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import config
import math
import numpy as np
from twisted.internet import reactor, threads
from score import score

class ProgressBox:
    def __init__(self, nPossibilities):
        self.nPossibilities = nPossibilities
        self.nCompleted = 0

    def getProgress(self):
        return float(self.nCompleted) / self.nPossibilities

    def getPercentProgress(self):
        return (self.nCompleted * 100) / self.nPossibilities

    def addCompleted(self):
        if self.nCompleted < self.nPossibilities:
            self.nCompleted = self.nCompleted + 1

def produceMatrix(chosenSections):
    schedule = np.empty(7, dtype=object)
    for i in range(0,7):
        schedule[i] = np.empty(config.SLOTS_PER_DAY, dtype=object)

    for section in chosenSections:
        sessions = section.sessions
        for sess in sessions:
            tss = sess.timeslots
            for ts in tss:
                sday = int(math.floor(ts / config.SLOTS_PER_DAY))
                sslot = ts % config.SLOTS_PER_DAY

                if schedule[sday][sslot] is not None:
                    return None

                schedule[sday][sslot] = sess

    return schedule

def solve2(socket, nCourse, sectionsForCourse, chosenSections, timeEquivalencies, progressBox, start, end, freeDays):
    # TODO: A better implementation here?
    if nCourse <= 3:
        progress = progressBox.getPercentProgress()
        reactor.callFromThread(socket.sendProgress, progress)

        cancelled = threads.blockingCallFromThread(reactor, socket.isCancelled)
        if cancelled:
            raise ValueError("The request has been cancelled")

    if nCourse == len(sectionsForCourse):
        schedule = produceMatrix(chosenSections)
        progressBox.addCompleted()
        progress = progressBox.getPercentProgress()

        if schedule is not None:
            sc = score(schedule, start, end, freeDays)

            # Copy sections
            chosenSectionsForOutput = []
            for chosenSection in chosenSections:
                chosenSectionsForOutput.append(chosenSection)

            reactor.callFromThread(socket.sendProgress, progress, chosenSectionsForOutput, timeEquivalencies, sc)

        return

    course = sectionsForCourse[nCourse][0]
    sections = sectionsForCourse[nCourse][1]

    for section in sections:
        chosenSections[nCourse] = section
        solve2(socket, nCourse + 1, sectionsForCourse, chosenSections, timeEquivalencies, progressBox, start, end, freeDays)

def startSolution(socket, courses, start, end, freeDays):
    solutions = []
    sectionsForCourse = []
    timeEquivalencies = {}

    nPossibilities = 1
    for course in courses:
        if course is not None:
            sectionsForThisCourse = {}

            for section in course.sections:
                hash = section.time_hash

                if not hash in sectionsForThisCourse:
                    sectionsForThisCourse[hash] = section
                else:
                    timeEquivalentSection = sectionsForThisCourse[hash]

                    if not section in timeEquivalencies:
                        timeEquivalencies[timeEquivalentSection] = []

                    timeEquivalencies[timeEquivalentSection].append(section)

            sectionList = [value for key,value in sectionsForThisCourse.iteritems()]
            sectionsForCourse.append((course, sectionList))

            nPossibilities = nPossibilities * len(sectionList)

    chosenSections = np.empty(len(sectionsForCourse), dtype=object)
    progressBox = ProgressBox(nPossibilities)

    solve2(socket, 0, sectionsForCourse, chosenSections, timeEquivalencies, progressBox, start, end, freeDays)

    reactor.callFromThread(socket.sendCompletion)