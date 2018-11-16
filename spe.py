import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
	r.adjust_for_ambient_noise(source,duration=5)
	r.dynamic_energy_thresheld = True
	print("Say Someting")
	audio = r.listen(source)

try:
	print("you said: " + r.recognize_google(audio))
except sr.UnknownValueError:
	print("Google sppech recognition could not understand audio")
except sr.Requesterror as e:
	print("could not request results from Google speech Recognition service: {0}".format(e))