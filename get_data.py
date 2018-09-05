import yaml
import os
from os.path import splitext
from datetime import datetime
import matplotlib.pyplot as plt

log_dir = "logs/"

with open("config.yaml", 'r') as config:
    config = yaml.load(config)

event_types = [*config]
event_type_time = [0] * len(event_types)

start_time = datetime(2018, 9, 4, 0, 0).timestamp()
end_time = datetime(2018, 9, 5, 0, 0).timestamp()

span = end_time - start_time

print(start_time)
print(end_time)
print("")

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
                        event_type_time[ind_] += int(duration)
                        # print(event_type, duration)
                        break
print(event_types)
print(event_type_time)
labels = event_types
sizes = event_type_time
# explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
