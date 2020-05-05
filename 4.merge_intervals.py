class Interval:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return f"[{self.start}, {self.end}]"


class Job:
    def __init__(self, start, end, cpu_load):
        self.start = start
        self.end = end
        self.cpu_load = cpu_load


def merge_intervals(intervals):
    """
    Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.
    """
    pass


def insert_interval(instervals, new_interval):
    """
    Given a list of non-overlapping intervals sorted by their start time, insert a given interval at the correct position and merge all necessary intervals to produce a list that has only mutually exclusive intervals.
    """
    pass


def interval_intersection(intervals_a, intervals_b):
    """
    Given two lists of intervals, find the intersection of these two lists.
    Each list consists of disjoint intervals sorted on their start time.
    """
    pass


def can_attend_all_appointments(appointments):
    """
    Given an array of intervals representing ‘N’ appointments, find out if a person can attend all the appointments.
    """
    pass


def minimum_meeting_rooms(meetings):
    """
    Given a list of intervals representing the start and end time of ‘N’ meetings, 
    find the minimum number of rooms required to hold all the meetings.
    """
    pass


def maximum_cpu_loads(jobs):
    """
    We are given a list of Jobs. Each job has a Start time, an End time, and a CPU load when it is running.
    Our goal is to find the maximum CPU load at any time if all the jobs are running on the same machine.
    """
    pass


def find_employee_free_time(schedule):
    """
    For ‘K’ employees, we are given a list of intervals representing the working hours of each employee.
    Our goal is to find out if there is a free interval that is common to all employees. 
    You can assume that each list of employee working hours is sorted on the start time.
    """
    pass
