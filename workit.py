#!/usr/bin/python3
'''
WorkIt
created by: Arlo Gittings
created on: 2021-07-12
last modified: 2021-07-12
description:
    A time tracking todo list designed to enable users to log repeated tasks
    automatically while allowing for ad hoc project additions in the flow of 
    the day with minimal interruption. Additionally, this will allow for evals
    on a regular basis to increase time spent working on what you want to work
    on and decrease the number of daily tasks that are missed because you get
    trapped in work and forget basics. It will also help to identify time sucks
    that are keeping you engaged longer than you want to be.
'''

class Task_List():
    '''
    Task_List:
        available methods:
            new_activity()
            start_activity(id, time)
            stop_activity(id, time)
            complete_activity(id, time)
            cancel_activity(id)
            show_activities()
            load_activities(file)
            save_activities(file)
    '''
    def __init__(self):
        self.activities = {}
        self.cancels = {}
