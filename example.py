import wfprogressbar as pb
import time


# Default Usage
bar = pb.ProgressBar()
total = 10
for i in range(total):
    bar.progress(i, total)
    time.sleep(1)


# Custom Usage
bar = pb.ProgressBar(label="Downloading - ", bar_length=25, full_marker="X", empty_marker="O")
total = 9
for i in range(total):
    bar.progress(i, total)
    time.sleep(1)