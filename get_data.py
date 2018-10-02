import os
from os.path import splitext
from subprocess import call

from datetime import datetime, timedelta

import argparse

from flask import Flask
from flask import render_template

import yaml
import json


def main(args):
    days = args.days
    topn = args.topn

    if days is None:
        days = 1
    
    if topn is None:
        topn = 5

    if days < 1 or topn < 1:
        raise ValueError("arguments should be greater than 0.")

    print("Plotting for last", days, "day(s).")

    log_dir = "logs/"

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    with open("config.yaml", 'r') as config:
        config = yaml.load(config)

    event_types = [*config]
    event_types += ['Other']

    log_start_time = datetime.today() - timedelta(days=days)
    log_start_time = log_start_time.timestamp()

    log_end_time = datetime.now().timestamp()

    print("From", datetime.fromtimestamp(log_start_time), "to", datetime.fromtimestamp(log_end_time))

    span = log_end_time - log_start_time

    #-------------------------------------------creating chart.js objects----------------------------------#
    bar_chart_data = {}
    bar_chart_data["labels"] = [] #
    chartColors = ['rgb(255, 99, 132)', 'rgb(201, 203, 207)', 'rgb(255, 159, 64)', 
                    'rgb(255, 205, 86)', 'rgb(75, 192, 192)', 'rgb(54, 162, 235)', 'rgb(153, 102, 255)']

    datasets = []
    for i in range(len(event_types)):
        datasets.append({})
        datasets[i]['label'] = event_types[i]
        datasets[i]['backgroundColor'] = chartColors[i]
        datasets[i]['data'] = []
    #------------------------------------------------------------------------------------------------------#

    event_and_duration = {}
    for file_ in sorted(os.listdir("logs")):
        file_name = float(splitext(file_)[0])
        event_type_time = [0] * len(event_types)

        if file_name >= log_start_time and file_name <= log_end_time:
            print("Parsing... ", file_)

            bar_chart_data["labels"].append(str(datetime.fromtimestamp(int(file_name)).date()))

            with open(log_dir + file_, 'rb') as f:
                for i, log in enumerate(f.readlines()):
                    log = str(log).split(" ")

                    if len(log)==2:
                        end_time, duration, event = log[0], log[1][:-3], 'Desktop'
                    else:
                        end_time, duration, event = log[0], log[1], " ".join(log[2:])[:-3]
                    event_type = 'Other'
                    duration = round(float(duration)/3600., 3)

                    if event in event_and_duration:
                        event_and_duration[event] += duration
                    else:
                        event_and_duration[event] = duration

                    for event_type_, event_ in config.items():
                        for e in event_:
                            if e in event:
                                event_type = event_type_
                                break

                        if event_type != 'Other':
                            break

                    ind_ = event_types.index(event_type)
                    event_type_time[ind_] += duration

            for i, event in enumerate(event_type):
                datasets[i]['data'].append(round(event_type_time[i], 3))

    #--------------------------------------save bar_plot data as json-----------------------------
    bar_chart_data['datasets'] = datasets
    with open('static/data.json', 'w') as f:
        json.dump(bar_chart_data, f)
    #--------------------------------------------------------=------------------------------------

    print("Top", topn, "most time consuming jobs are -")
    for w in sorted(event_and_duration, key=event_and_duration.get, reverse=True)[:topn]:
        print (w, event_and_duration[w])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="An app for logging your daily routines.")

    parser.add_argument('--days', type=int, help='Number of days since today to plot.')
    parser.add_argument('--topn', type=int, help='Number of top time consuming jobs to print.')

    args = parser.parse_args()

    main(args)
    call(["npm", "start"])