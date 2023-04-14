from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('chatbot', read_only =False, 
              logic_adapter = [
    {
                'import_path':'chatter.logic.BestMatch',
                'default_response':'Sorry, I dont know what do you mean',
                'maximum_similarity_threshold':0.90
    }
    ])

list_to_train = [
    "hi",
    "Hi there, How are you?",
    "What's is your fav food",
    "My fav food is you!",
    "what's your name",
    "I am a chatbot",
    "Do you have children",
    "No",

]
# nlp = spacy.load("en_core_web_sm")

list_trainer = ListTrainer(bot)
list_trainer.train(list_to_train)

def index(request):
    return render(request, 'blog/index.html')
    # return HttpResponse("This is my first url")

def specific(request):
    return HttpResponse("killer")

def getResponse(request):
    userMessage = request.GET.get('userMessage')
    chatResponse = (bot.get_response(userMessage))
    return HttpResponse(chatResponse)


