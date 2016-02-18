from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from Quiz.models import *
from Quiz.serializers import *

from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics


#@login_required(redirect_field_name='')
def home(request):
    languages = Language.objects.all()
    context = {
        'languages': languages
    }
    print("Home")
    return render(request, 'Quiz/home.html', context)


def login_template(request):
    return render(request, 'Quiz/login.html')


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


def sign_up(request):
    if request.method == 'POST':
        print("POST working")
        # serializer = AccountSerializer(data=request.data)
        request_data = JSONParser().parse(request)
        account = Account.objects.create_user(email=request_data.get('email'))
        account.first_name = request_data.get('first_name')
        account.last_name = request_data.get('last_name')
        account.gender = request_data.get('gender')
        account.set_password(request_data.get('password'))
        account.save()
        return JSONResponse(data=request_data, status=201)


def user_session(request):
    print('session : ', request.user)
    if request.user.is_authenticated():
        return HttpResponse(request.user, status=200)
    else:
        return HttpResponse(status=400)


def user_login(request):
    if request.method == 'POST':
        print(request.user)
        request_data = JSONParser().parse(request)
        #print(request_data)
        username = request_data['username']
        password = request_data['password']
        #print(username, password)
        user = authenticate(username=username, password=password)
        print(username, password)
        if user is not None:
            print(user)
            if user.is_active:
                login(request, user)
                print("login")
                return HttpResponse(username)
            else:
                print('user is not active')
                return JSONResponse(data='Your account is not active', status=500)
        else:
            return JSONResponse(
                    data='username and password does not match', 
                    status=500
            )


def user_logout(request):
    logout(request)
    print('logout')
    return HttpResponse(status=200)


def save_user_score(request):
    print('storing scores')
    if request.method == 'POST':
        request_data = JSONParser().parse(request)
        account = Account.objects.get(email=request_data.get('account'))
        language = Language.objects.get(pk=request_data['language'])
        level = Level.objects.get(pk=request_data['level'])
        user_score = UserScore.objects.create(
            account=account,
            language=language,
            level=level,
            total_time=request_data['total_time'],
            total_question=request_data['total_question'],
            time_taken=request_data['time_taken'],
            total_correct=request_data['total_correct'],
            score=request_data['score']
        )
        user_score.save()
        print('score created')
        return JSONResponse(request_data, status=201)


class UserList(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    lookup_field = 'email'


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    lookup_field = 'email'


class LanguageDetail(generics.RetrieveAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class LevelDetail(generics.RetrieveAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelWithQuestion


class UserScoreList(generics.ListCreateAPIView):
    queryset = UserScore.objects.all()
    serializer_class = UserScoreSerializer


class UserScoreDetail(generics.RetrieveDestroyAPIView):
    queryset = UserScore.objects.all()
    serializer_class = UserScoreSerializer


def play_data(request, language_id, level_id, total_questions):
    if request.method == 'GET':
        language = Language.objects.get(pk=language_id)
        level = Level.objects.get(pk=level_id)
        questions = Question.objects.filter(language=language, level=level)
        print(language_id, " ", level_id, " ", questions)
        total_questions = int(total_questions)
        if total_questions > questions.count():
            question_serializer = QuestionSerializer(questions, many=True)
        else:
            question_serializer = QuestionSerializer(questions[:total_questions], many=True)
        return JSONResponse(question_serializer.data)


@api_view(['GET', 'POST'])
def account_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Account.objects.all()
        serializer = AccountSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        print("POST working")
        serializer = AccountSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            print('Invalid')
            return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, email):
    """
    Retrieve, update or delete a snippet instance.
    """
    try:
        account = Account.objects.get(email=email)
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AccountSerializer(account)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AccountSerializer(account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def question_list(request):
    """
     List a set of questions with options
    """
    if request.method == 'GET':
        questions = Question.objects.all()
        que_serializer = QuestionSerializer(instance=questions, many=True)
        return JSONResponse(que_serializer.data)


def questions_list(request):
    questions = Question.objects.all()[0]
    from django.core import serializers
    # qs = serializers.serialize('json', questions)
    print(questions)
    serializer = QuestionSerializer(many=True, instance=questions)
    print(serializer.data)
    return JSONResponse(serializer.data)


# Templates

def get_user_template(request):
    return render(request, 'Quiz/user_detail.html')


def get_language_template(request):
    language = Language.objects.get(pk=1)
    context = {
        'language': language
    }
    print(request.user)
    return render(request, 'Quiz/language_detail.html', context=context)


def get_play_template(request):
    print("Play")
    return render(request, 'Quiz/play.html', context={})


def get_sign_up_template(request):
    return render(request, 'Quiz/signup.html', context={})


def get_login_template(request):
    return render(request, 'Quiz/login.html')


def get_home_page_template(request):
	return render(request, 'Quiz/home_page.html')