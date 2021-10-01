import pretty_midi
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write


midi_data = pretty_midi.PrettyMIDI('zan-sayonara-zetsubou-sensei-main-theme.mid')

test = (midi_data.synthesize(fs=11025, wave=np.sin))

time = []
print(str(len(test)))
i = 0

# for entry in test:
#     time.append(i)
#     i = i + 1
#     if i % 100000 == 0:
#         print(i)
# 
# plt.scatter(time, test, color='darkblue', marker='x', label="item 1")
# plt.show()

scaled = np.int16(test / np.max(np.abs(test)) * 32767)
write('test.wav', 11025, scaled)
