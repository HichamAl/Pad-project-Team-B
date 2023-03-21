from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Challenge, UserPoints
from django.db.models import Sum

# Create your views here.

# work in progress
@login_required(login_url='/login/')
def profile(request):
    user_points = UserPoints.objects.filter(user=request.user).values('user__username').annotate(total_points=Sum('points')).all()
    if len(user_points) == 0:
        return render(request, "main/profile.html", {'user_points': user_points, 'total_points': 0})
    user_points = user_points[0]
    return render(request, "main/profile.html", {'user_points': user_points, 'total_points': user_points['total_points']})

# home page view
@login_required(login_url='/login/')
def home(response):
    return render(response, "main/home.html")
 
# index page/challenge view
def index(request):
    # if user has not seen index is redirected to index.html 
    # else redirected to the enterpage 
    if 'has_seen_index' not in request.session:
        request.session['has_seen_index']= True
        return render (request, 'main/index.html')
    else:
        return redirect("/enter/")

# enter view
def enter(response):
    return render(response, "main/enter.html")

# credit view
@login_required(login_url='/login/')
def credit(response):
    return render(response, "main/credit.html")

# challenge page view
@login_required(login_url='/login/')
def challenges(request):
    user_points = UserPoints.objects.filter(user=request.user).values('user__username').annotate(total_points=Sum('points')).all()
    if len(user_points) == 0:
        return render(request, "main/challenges.html", {'user_points': user_points, 'total_points': 0})
    user_points = user_points[0]
    # SELECT *, SUM(points) AS total_points WHERE user.username=username GROUP BY user.username;
    # dits voor leader board
    # user_points = UserPoints.objects.values('user__username').annotate(total_points=Sum('points')).all()[:10]
    print(user_points['total_points'])
    # print(user_points.points)
    return render(request, "main/challenges.html", {'user_points': user_points, 'total_points': user_points['total_points']})








#points system
@login_required(login_url='/login/')
def challenges1(request):
    if request.method == 'POST':
        flag = request.POST.get('flag')
        try:
            challenge = Challenge.objects.get(flag=flag)
            print('c', challenge)
            try:
                up = UserPoints.objects.get(user=request.user, challenges__flag=flag)
                print('i', up)
                messages.error(request, 'You have already submitted this flag.')
                
            except UserPoints.DoesNotExist:
                user_points = UserPoints.objects.create(user=request.user, points=challenge.points, challenges=challenge)
                user_points.save()
                messages.success(request, f'You earned {challenge.points} points for submitting the flag!')
                
        except Challenge.DoesNotExist:
            messages.error(request, 'Wrong flag code.')
        
    return render(request, 'main/challenges-1.html')


@login_required(login_url='/login/')
def leaderboard(request):
    user_points = UserPoints.objects.values('user__username').annotate(total_points=Sum('points')).order_by('-total_points')[:10]
    return render(request, 'main/leaderboard.html', {'user_points': user_points})


