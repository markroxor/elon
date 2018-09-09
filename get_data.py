import yaml
import os
from os.path import splitext
from datetime import datetime, timedelta

import numpy as np
import matplotlib.pyplot as plt

import argparse

def main(args):

    if args.days is None:
        days = 1
    elif args.days < 1:
        raise ValueError("--days should be greater than 0.")
    else:
        days = args.days

    print("Plotting for last", days, "day(s).")

    log_dir = "logs/"

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    with open("config.yaml", 'r') as config:
        config = yaml.load(config)

    event_types = [*config]
    event_type_time = [0] * len(event_types)

    log_start_time = datetime.today() - timedelta(days=days)
    log_start_time = log_start_time.timestamp()

    log_end_time = datetime.now().timestamp()

    print("From", datetime.fromtimestamp(log_start_time), "to", datetime.fromtimestamp(log_end_time))

    span = log_end_time - log_start_time

    for file_ in os.listdir("logs"):
        file_name = float(splitext(file_)[0])
        if file_name >= log_start_time and file_name <= log_end_time:
            print("Parsing... ", file_)

            with open(log_dir + file_, 'rb') as f:
                for log in f.readlines():
                    log = str(log).split(" ")

                    end_time, duration, event = log[0], log[1], " ".join(log[2:])[:-3]
                    event_type = 'other'

                    for event_type, event_ in config.items():
                        for e in event_:
                            if e in event:
                                ind_ = event_types.index(event_type)
                                event_type_time[ind_] += float(duration)/3600.
                                break

    fig, ax = plt.subplots(figsize=(10, 5), subplot_kw=dict(aspect="equal"))

    data = event_type_time
    Tasks = event_types


    def func(pct, allvals):
        absolute = pct/100.*np.sum(allvals)
        return "{:.3f}%\n({:.3f} hrs)".format(pct, absolute)


    wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                    textprops=dict(color="w"))

    ax.legend(wedges, Tasks,
            title="Tasks",
            loc="center left",
            bbox_to_anchor=(1, 0, 0.5, 1))

    plt.setp(autotexts, size=8, weight="bold")

    ax.set_title("Logs for today.")

    plt.show()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="An app for logging your daily routines.")

    parser.add_argument('--days', type=int, help='Number of days since today to plot.')

    args = parser.parse_args()
    main(args)
