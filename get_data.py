import yaml
import os
from os.path import splitext
from datetime import datetime

import numpy as np
import matplotlib.pyplot as plt

log_dir = "logs/"

with open("config.yaml", 'r') as config:
    config = yaml.load(config)

event_types = [*config]
event_type_time = [0] * len(event_types)

start_time = datetime(2018, 9, 4, 0, 0).timestamp()
end_time = datetime.datetime.now().timestamp()

span = end_time - start_time

for file_ in os.listdir("logs"):
    file_name = float(splitext(file_)[0])

    if file_name >= start_time and file_name <= end_time:
        print("Parsing... ", file_)

        with open(log_dir + file_, 'rb') as f:

            for log in f.readlines():
                log = str(log).split(" ")

                end_time, duration, event = log[0], log[1], " ".join(log[2:])[:-3]
                event_type = 'other'

                for event_type, event_ in config.items():
                    if event.endswith(event_[0]):
                        ind_ = event_types.index(event_type)
                        event_type_time[ind_] += float(duration)/3600.
                        break

print(event_types)
print(event_type_time)

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