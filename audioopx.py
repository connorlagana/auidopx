import audioop
import wave
#from playsound import playsound

SUMMER = "../../../Desktop/summer.wav"

#print(SUMMER)

wav = wave.open(SUMMER, 'r')

print(audioop.avg(wav.readframes(wav.getnframes()), wav.getsampwidth()))

wav.rewind()

print('Number of audio channels: ', wav.getnchannels())
print('Sample width in bytes: ', wav.getsampwidth())
print('Sampling Frequency: ', wav.getframerate())
print('Number of audio frames: ', wav.getnframes())
print('Compression type: ', wav.getcomptype())
print('Compression name: ', wav.getcompname())

#playsound(SUMMER)
