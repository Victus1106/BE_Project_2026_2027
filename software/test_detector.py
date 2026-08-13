from serial_io.serial_reader import SerialReader

from signal_processing.preprocessing import SignalProcessor

from detection.eye_detector import EyeMovementDetector

import time

reader = SerialReader()

reader.connect()

reader.start()

processor = SignalProcessor()

detector = EyeMovementDetector()

while True:

    sample = reader.latest()

    if sample is None:
        continue

    _, h, v = sample

    fx, fy = processor.process_sample(
        h,
        v
    )

    movement = detector.process(
        fx,
        fy
    )

    print(movement)

    time.sleep(0.004)