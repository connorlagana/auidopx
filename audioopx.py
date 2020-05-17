import audioop
import wave
SUMMER = "../../../Desktop/summer.wav"

#print(SUMMER)

wav = wave.open(SUMMER, 'r')

print(audioop.avg(wav.readframes(wav.getnframes()), wav.getsampwidth()))
