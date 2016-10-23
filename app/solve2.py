#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from random import randint

import json
import config
import math
import numpy as np
from models import Course, Section
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from score import score
import heapq
engine = create_engine(config.SQLALCHEMY_DATABASE_URI)

DBSession = sessionmaker(bind=engine)
session = DBSession()

am = 0

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

def solve2(nCourse, sectionsForCourse, slns, chosenSections, start, end, freeDays):
    if nCourse == len(sectionsForCourse):
        schedule = produceMatrix(chosenSections)

        if schedule is not None:
            priority = -1 * score(schedule, start, end, freeDays)

            global am
            am += 1
            heapq.heappush(slns, (priority, am, schedule))

            #print 'Found solution ' + str(len(slns)) + '.'

        return

    course = sectionsForCourse[nCourse][0]
    sections = sectionsForCourse[nCourse][1]

    for section in sections:
        chosenSections[nCourse] = section
        solve2(nCourse + 1, sectionsForCourse, slns, chosenSections, start, end, freeDays)

def getSolutions(courses, start, end, freeDays):
    solutions = []
    sectionsForCourse = []
    for course in courses:
        if course is not None:
            sectionsForThisCourse = {}

            for section in course.sections:
                hash = section.time_hash

                if not hash in sectionsForThisCourse:
                    sectionsForThisCourse[hash] = section

            sectionsForCourse.append((course, [value for key,value in sectionsForThisCourse.iteritems()]))

    schedule = np.empty(7, dtype=object)
    for i in range(0, len(schedule)):
        schedule[i] = np.empty(config.SLOTS_PER_DAY, dtype=object)

    chosenSections = np.empty(len(sectionsForCourse), dtype=object)

    solve2(0, sectionsForCourse, solutions, chosenSections, start, end, freeDays)

    return solutions