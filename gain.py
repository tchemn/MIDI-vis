import pretty_midi
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.io.wavfile import write

speedfactor = 1
midi_file = pretty_midi.PrettyMIDI('zan-sayonara-zetsubou-sensei-main-theme.mid')
track = (midi_file.synthesize(fs=11025, wave=np.sin))

print(str(len(track)))
print(type(track))
print(track[45691])

mod = track
last = 0
diff = 0
for index, entry in enumerate(mod):
    diff = (np.sin((3.14 / 1500) * (150 * abs(entry - last))))
    last = entry
    mod[index] -= diff

result = np.asarray(mod, dtype=np.float32)
# result -= track
# plt.scatter(time, track, color='darkblue', marker='x', label="item 1")
# plt.show()

scaled = np.int16(result / np.max(np.abs(result)) * 32767)
write('res.wav', 11025 * speedfactor, scaled)
