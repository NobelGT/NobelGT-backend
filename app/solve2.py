#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import config
import math
import numpy as np
from twisted.internet import reactor, threads
from score import score

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

def solve2(socket, nCourse, sectionsForCourse, chosenSections, timeEquivalencies, start, end, freeDays):
    # TODO: A better implementation here?
    if nCourse <= 4:
        cancelled = threads.blockingCallFromThread(socket.isCancelled)
        if cancelled:
            raise ValueError("The request has been cancelled")

    if nCourse == len(sectionsForCourse):
        schedule = produceMatrix(chosenSections)

        if schedule is not None:
            sc = score(schedule, start, end, freeDays)

            # We can push the thing back! Hooray!
            # TODO: Call it without fucking up
            # TODO: Add progress
            progress = 0
            reactor.callFromThread(socket.sendProgress, schedule, sc, progress)

        return

    course = sectionsForCourse[nCourse][0]
    sections = sectionsForCourse[nCourse][1]

    for section in sections:
        chosenSections[nCourse] = section
        solve2(nCourse + 1, sectionsForCourse, chosenSections, start, end, freeDays)

def startSolution(socket, courses, start, end, freeDays):
    solutions = []
    sectionsForCourse = []
    timeEquivalencies = {}
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

            sectionsForCourse.append((course, [value for key,value in sectionsForThisCourse.iteritems()]))

    chosenSections = np.empty(len(sectionsForCourse), dtype=object)

    solve2(socket, 0, sectionsForCourse, chosenSections, timeEquivalencies, start, end, freeDays)

    reactor.callFromThread(socket.sendCompletion)