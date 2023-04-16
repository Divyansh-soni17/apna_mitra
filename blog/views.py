from django.shortcuts import render
from django.http import HttpResponse
import openai, os
from dotenv import load_dotenv
import speech_recognition as sr
import pyttsx3
import json
load_dotenv()

api_key = os.getenv("OPENAI_KEY", None)
print(api_key)

def index(request):
    return render(request, 'blog/index.html')

def getResponse(request):
    chatResponse = None
    if api_key is not None:
        openai.api_key=api_key
        userMessage = request.GET.get('userMessage')
        prompt = userMessage

        chatResponse = openai.Completion.create(
            engine='text-davinci-003',
            prompt=prompt,
            max_tokens = 100,
            temperature =0.3
        )

    return HttpResponse(chatResponse["choices"][0]["text"])

# def SpeakText(request):
     
#     # Initialize the engine
#     engine = pyttsx3.init()
#     engine.say(request.POST.get('Message'))
#     engine.runAndWait()

def speechtotext(request):
		
	r = sr.Recognizer()
	Query = {
		"success": "False",
		"text": None
	}
	with sr.Microphone() as source:

		print('Listening')
		r.pause_threshold = 0.7
		audio = r.listen(source,phrase_time_limit=6)
	try:
		print("Recognizing")
		Query["text"] = r.recognize_google(audio)
		Query["success"] = "True"
	except Exception:
		# Query = False
		Query["text"] = "Sorry I didnt understand, can you please repeat that again."

	print(Query["text"])
	return HttpResponse(json.dumps(Query))

