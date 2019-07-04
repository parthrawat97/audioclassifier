from pydub import AudioSegment
from scipy.io import wavfile
import pandas as pd

df = pd.read_csv('data.csv') 											   #csv file
df.set_index('fname', inplace=True)

for f in df.index:
	rate, signal = wavfile.read('gun/'+f) 								#path of stereo data 
	signal = AudioSegment.from_wav('gun/'+f)                    #path of stereo data     
	signal = signal.set_channels(1)
	signal.export('guns/'+f, format="wav")								#path of mono data
