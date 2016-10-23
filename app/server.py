#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import datetime
import time

import config
from flask import Flask, render_template, request, redirect
from models import Course
from prettyprint import sch2str, sch2tab
from solve2 import getSolutions
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

engine = create_engine(config.SQLALCHEMY_DATABASE_URI)

DBSession = sessionmaker(bind=engine)
session = DBSession()

def datetimestrptime(time_string,time_fmt):
     t = time.strptime(time_string,time_fmt)
     return datetime.time(hour=t.tm_hour,minute=t.tm_min,second=t.tm_sec)

@app.route('/')
def display_index():
    return render_template('index.html')
    #return redirect('/schedule', 302)

@app.route('/schedule')
def display_scheduled():
    return render_template('form.html')

@app.route('/result', methods=['GET', 'POST'])
def display_watch():
    courses = request.form.get('listCourses')
    freeDays = request.form.get('freeDays')
    startTimeStr = request.form.get('startTime')
    endTimeStr = request.form.get('endTime')

    courseData = courses.split(',')
    chosenCourses = []
    for courseItem in courseData:
        fullCourse = courseItem.strip()
        courseParts = fullCourse.split(" ")
        dept = courseParts[0]
        code = courseParts[1]

        course = session.query(Course).filter(Course.department_code == dept).filter(Course.course_number == code).first()
        if course is not None:
            chosenCourses.append(course)

    startTime = datetimestrptime(startTimeStr,"%I:%M %p")
    endTime = datetimestrptime(endTimeStr,"%I:%M %p")

    intFreeDays = int(freeDays)

    if startTime is not None and endTime is not None and intFreeDays is not None and len(chosenCourses) > 0:
        slns = getSolutions(chosenCourses, startTime, endTime, intFreeDays)
        schedules = [sch2tab(sln) for sln in slns][0:10]

        if len(schedules) > 1:
            return render_template('result.html', message="Only the top 10 results are shown:", schedules=schedules)
        else:
            return render_template('result.html', message="Sorry, an error occurred.", schedules=[])
    else:
        return render_template('result.html', message="Sorry, an error occurred.", schedules=[])
        #return render_template('result.html', message="You suck." + str(startTime) + " " + str(endTime) + " " + str(intFreeDays) + " " + str(chosenCourses), schedules=[])