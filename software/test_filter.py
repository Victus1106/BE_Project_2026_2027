from signal_processing.filters import SignalFilters

import config

filters = SignalFilters(config.FS)

while True:

    x = float(input("Horizontal : "))

    y = float(input("Vertical : "))

    fx, fy = filters.process(x, y)

    print(fx, fy)