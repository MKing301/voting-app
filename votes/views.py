from django.shortcuts import render, get_object_or_404, redirect
from .models import Poll, Choice, Vote
from django.contrib.auth.decorators import login_required


@login_required
def poll_list(request):
    polls = Poll.objects.filter(is_active=True)
    return render(request, 'votes/poll_list.html', {'polls': polls})


@login_required
def poll_detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    user_vote = Vote.objects.filter(user=request.user, choice__poll=poll).first()

    if request.method == 'POST':
        if user_vote:
            # Optional: show a message that the user has already voted
            return redirect('poll_results', poll_id=poll.id)

        choice_id = request.POST.get('choice')
        choice = get_object_or_404(Choice, pk=choice_id, poll=poll)

        Vote.objects.create(user=request.user, choice=choice)
        return redirect('poll_results', poll_id=poll.id)

    return render(request, 'votes/poll_detail.html', {
        'poll': poll,
        'user_vote': user_vote,
    })


@login_required
def poll_results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'votes/poll_results.html', {'poll': poll})
