import wave
import contextlib

for i in range(1, 87):
    if i < 10:
        fname = "wav/allende0" + str(i) + "-allende.wav"
    else:
        fname = "wav/allende" + str(i) + "-allende.wav"

    with contextlib.closing(wave.open(fname, 'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        print(fname.split("/")[1] + " " + str(duration))
