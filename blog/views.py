from django.shortcuts import render
from django.http import HttpResponse
import openai, os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_KEY", None)
print(api_key)

def index(request):
    return render(request, 'blog/index.html')

def specific(request):
    return HttpResponse("killer")

def getResponse(request):
    chatResponse = None
    if api_key is not None:
        openai.api_key=api_key
        userMessage = request.GET.get('userMessage')
        prompt = userMessage

        chatResponse = openai.Completion.create(
            engine='text-davinci-003',
            prompt=prompt,
            max_tokens = 256,
            temperature =0.3
        )
    return HttpResponse(chatResponse["choices"][0]["text"])



