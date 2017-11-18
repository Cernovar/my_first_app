from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UsernameForm, CommentsForm
from .models import Username
import random



def greeting(request):
    form = UsernameForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form = form.save()
        return HttpResponseRedirect('/choice')
    return render(request, 'game/greeting.html', locals())


def choice(request):
    
    return render(request, 'game/choice.html')


def normal_game(request, id=None):
    if id == '0':
        return HttpResponseRedirect('/results/0')
    elif id == '1':
        return HttpResponseRedirect('/results/1')
    elif id == '2':
        return HttpResponseRedirect('/results/2')
    return render(request, 'game/normal_game.html', locals())


def hard_game(request, id=None):
    if id == '0':
        return HttpResponseRedirect('/hard_results/0')
    elif id == '1':
        return HttpResponseRedirect('/hard_results/1')
    elif id == '2':
        return HttpResponseRedirect('/hard_results/2')
    return render(request, 'game/hard_game.html', locals()) 


def hard_results(request, id):
    player = int(id)
    counts = Username.objects.all()
    
    for count in counts:
        count = count.hard_count

    count += 1
    Username.objects.update(hard_count=count)
    return render(request, 'game/hard_results.html', locals())


def results(request, id):
    player = int(id)
    comp = int(random.randrange(0, 3))
    scores = Username.objects.all()
    
    for score in scores:
        user_score = score.user_score
        comp_score = score.comp_score

    if (comp - player) % 3 == 0:
        alert = "Dead heat."
    elif (comp - player) % 3 == 1:
        alert = "You won!"
        user_score += 1
        Username.objects.update(user_score=user_score)
    elif (comp - player) % 3 == 2:
        alert = "You lose..."
        comp_score += 1
        Username.objects.update(comp_score=comp_score)
       
    return render(request, 'game/results.html', locals())


def about(request):
    form = CommentsForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        form = CommentsForm
        tnx = "Thanks for your comment, dude!"
    return render(request, 'game/about.html', locals())

