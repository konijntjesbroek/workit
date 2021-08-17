#!/usr/bin/python3
'''
WorkIt
created by: Arlo Gittings
created on: 2021-07-12
last modified: 2021-08-12
description:
    A time tracking todo list designed to enable users to log repeated tasks
    automatically while allowing for ad hoc project additions in the flow of 
    the day with minimal interruption. Additionally, this will allow for evals
    on a regular basis to increase time spent working on what you want to work
    on and decrease the number of daily tasks that are missed because you get
    trapped in work and forget basics. It will also help to identify time sucks
    that are keeping you engaged longer than you want to be.
'''
from datetime import datetime as dt

class Activity():
    '''
    A model of a single task
    '''
    def __init__(self, task_id, name, context, category, project, flag, due, priority):
        self.task_id = task_id
        self.name = name
        self.context = context
        self.category = category
        self.project = project
        self.flag = flag
        self.due = due
        self.priority = priority


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
        self.active = {}
        self.hold = {}
        self.canceled = {}

def get_list(file):
    '''
    get_list:
        retrieve a list of tasks from a given file
    '''
    with open(file) as fh:
        lines = fh.readlines()
    return lines

def display_list(tasks):
    '''
    display_list:
        format the task list to be human readable
    '''
    comp_color = f'[38;2;195;225;145m'
    hold_color = f'[38;2;95;145;225m'
    header = [ h.strip() for h in tasks[0].split(',') ]
    f_tasks = 'To do list:\n'
    l_tasks = fieldify(header, tasks[1:])

    for task in l_tasks:
        if "comp" in task['flags']:
            f_tasks += f"{comp_color}{task['list_pos']}\t{task['task_name']}[0m\n"
        elif "hold" in task['flags']:
            f_tasks += f"{hold_color}{task['list_pos']}\t{task['task_name']}[0m\n"
        else:
            f_tasks += f"{task['list_pos']}\t{task['task_name']}\n"
    return f_tasks

def fieldify(fields, rows):
    result = [{}] * len(rows)
    for row in rows:
        fc = 0
        d_row = {}
        in_quote = False
        q_char = ''
        curr = ''
        for c in row:
            if in_quote:
                if c == q_char:
                    q_char = ''
                    in_quote = False
                else:
                    curr += c
            elif c == '"' or c == "'":
                q_char = c
                in_quote = True
            elif c == ',':
                d_row[fields[fc]] = curr.strip()
                fc += 1
                curr = ''
            else:
                curr += c
        result[int(d_row['list_pos'])] = d_row 

    return result
    
def main():
    path = '/data/data/com.termux/files/home/docs/dailies'
    date = dt.today().strftime('%Y/%m/%d')
    fname = f'{path}/{date}/tasks.csv'
    tasks = get_list(fname)
    print(display_list(tasks))

if __name__ == '__main__':
    main()
