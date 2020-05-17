import audioop
import wave
#from playsound import playsound

SUMMER = "../../../Desktop/summer.wav"

#print(SUMMER)

wav = wave.open(SUMMER, 'r')

print(audioop.avg(wav.readframes(wav.getnframes()), wav.getsampwidth()))

wav.rewind() 
print(audioop.max(wav.readframes(wav.getnframes()), wav.getsampwidth()))

#playsound(SUMMER)
