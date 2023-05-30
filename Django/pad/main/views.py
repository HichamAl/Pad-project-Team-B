from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Challenge, UserPoints
from django.db.models import Sum


# profile page view 
@login_required(login_url='/login/')
def profile(request):
    #shows the points a user has earned, gets the points from UserPoints Table from database then it, filters the points where user is request.user 
    #retrieves the username from the user object, then all of the userpoints has earned are summed up.
    #then all of the userpoints has earned are summed up. then all the points are then ordered, based on total points, and retrieves the first object.
    user_points = UserPoints.objects.filter(user=request.user).values('user__username').annotate(total_points=Sum('points')).order_by('-total_points').first()
    if user_points is None:
        return render(request, "main/profile.html", {'user_points': None, 'total_points': 0, 'rank': None})
    leaderboard = UserPoints.objects.values('user__username').annotate(total_points=Sum('points')).order_by('-total_points')
    rank = list(leaderboard).index(user_points) + 1
    return render(request, "main/profile.html", {'user_points': user_points, 'total_points': user_points['total_points'], 'rank': rank})

# home page view
def home(response):
    return render(response, "main/home.html")

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
    return render(request, "main/challenges.html", {'user_points': user_points, 'total_points': user_points['total_points']})

# points system, 
@login_required(login_url='/login/')
def challenges1(request):
    if request.method == 'POST':
        flag = request.POST.get('flag')
        #Gets the Challenge flags out of the Challenge objects (specific challenge)
        try:
            challenge = Challenge.objects.get(flag=flag)
            print('c', challenge)
            #Goes into the Userpoint objects looks if the user that puts in the flag already sumbitted
            # The flag by checking if the user has completed the specified Challenge object.
            try:
                up = UserPoints.objects.get(user=request.user, challenges__flag=flag)
                print('i', up)
                messages.error(request, 'You have already submitted this flag.')
                #If the User that fills in the flag has not the specified Challenge object in the userpoints
                #field then it wil create the specified Userpoints to the account with the specified Challenge object.
            except UserPoints.DoesNotExist:
                user_points = UserPoints.objects.create(user=request.user, points=challenge.points, challenges=challenge)
                user_points.save()
                messages.success(request, f'You earned {challenge.points} points for submitting the flag!')
                
                #If the challenge flag is not matching, it will give an error.
        except Challenge.DoesNotExist:
            messages.error(request, 'Wrong flag code.')
        
    return render(request, 'main/challenges-1.html')

# Copy this whole function to create a new challenge page.
@login_required(login_url='/login/')
def challenges2(request):
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
        
    return render(request, 'main/challenges-2.html')

#Copy this whole function to create a new challenge page.
@login_required(login_url='/login/')
def challenges3(request):
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
        
    return render(request, 'main/challenges-3.html')

#Copy this whole function to create a new challenge page.
@login_required(login_url='/login/')
def challenges4(request):
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
        
    return render(request, 'main/challenges-4.html')


# Leaderboard function. Queries the Userpoints db and out of the Usernames takes the points.Orders the users by Many to less. and will only show 10
@login_required(login_url='/login/')
def leaderboard(request):
    user_points = UserPoints.objects.values('user__username').annotate(total_points=Sum('points')).order_by('-total_points')[:10]
    return render(request, 'main/leaderboard.html', {'user_points': user_points})



