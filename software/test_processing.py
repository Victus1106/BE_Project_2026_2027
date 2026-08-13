from serial_io.serial_reader import SerialReader

from signal_processing.preprocessing import SignalProcessor

import time

reader = SerialReader()

reader.connect()

reader.start()

processor = SignalProcessor()

print("\nStreaming...\n")

while True:

    sample = reader.latest()

    if sample is None:

        continue

    timestamp, horizontal, vertical = sample

    fx, fy = processor.process_sample(

        horizontal,

        vertical

    )

    print(

        round(fx,2),

        round(fy,2)

    )

    time.sleep(0.004)