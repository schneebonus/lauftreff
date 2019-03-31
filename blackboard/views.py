from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import RunningSession
from django.contrib.auth.decorators import login_required

'''
Index View of the blackboard.
'''


def index(request):
    sessions = RunningSession.objects.all()
    context = {'sessions': sessions, 'bb_active': True}
    return render(request, 'blackboard/index.html', context)


'''
View to define new RunningSessions
'''


@login_required
def new_session(request):
    context = {}
    return render(request, 'blackboard/new_session_form.html', context)


'''
View to create a new RunningSessions
Required POST parameters are:
- title
- description
- location
'''


@login_required
def save_session(request):
    title = request.POST.get("title", "")
    description = request.POST.get("description", "")
    location = request.POST.get("location", "")
    current_user = request.user

    if title is not "" and description is not "" and location is not "":
        session = RunningSession(
            title=title, description=description, location=location, author=current_user)
        session.save()
        return redirect('blackboard:index')
    else:
        context = {'title': title,
                   'description': description, 'location': location}
        return render(request, 'blackboard/new_session_form.html', context)


'''
View to confirm and delete RunningSessions
'''


@login_required
def delete_session(request):
    id = request.GET.get('id', None)
    confirmation = request.GET.get('confirmation', None)
    session = None
    if id == None:
        # no id... user should not be here!
        # redirect to blackboard
        return redirect('blackboard:index')
    else:
        session = RunningSession.objects.filter(id=id)
        if len(session) == 0:
            # given id does not exist
            # redirect to blackboard
            return redirect('blackboard:index')
        else:
            session = session[0]    # thats ugly!
    if not request.user.is_authenticated:
        # user is not authentificated and should not be here!
        # should not be possible because of @login_required
        # redirect to blackboard!
        return redirect('blackboard:index')
    elif request.user == session.author:
        # current user is owner of this session
        if confirmation is not None and confirmation == "True":
            # delete and redirect to blackboard
            session.delete()
            return redirect('blackboard:index')
        else:
            # user is allowed to delete this session but should confirm the action
            context = {'session': session}
            return render(request, 'blackboard/delete_confirmation.html', context)
    else:
        # user is authentificated but not the author of the session.
        # redirect
        return redirect('blackboard:index')

    # in case we reached this line of code none of the previous condition applied.
    # thats a problem!
    # to prevent damage, redirect to blackboard.
    return redirect('blackboard:index')
