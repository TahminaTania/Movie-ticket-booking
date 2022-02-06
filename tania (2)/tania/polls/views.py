from django.shortcuts import redirect, render
# from django.http import HttpResponse
# from django.urls import exceptions
from .models import zara, participant
from .forms import reg

# Create your views here.


def hello(request):

    polls = zara.objects.all()
    # [
    #     {'title':'Man of steel',
    #     'location':'New York',
    #     'details': 'This movie released on 2001',
    #     'slug': 'A_first_one'},
    #     {'title':'The witcher',
    #     'location':'Paris',
    #     'details': 'This movie released on 2021',
    #     'slug':'Second_one' },
    #     {'title':'Garlat of rivia',
    #     'location':'Grece',
    #     'details': 'This movie released on 2022',
    #     'slug':'Third_one'}
    # ]

    # return HttpResponse("Hello world! this is zara.")
    return render(request, 'hello.html', {
        # 'show_pol': True,
        'polls': polls
    }
    )


def details(request, polls_slug):
    selected = {
        'title': polls_slug,
        'details': 'This movie released on 2009',
    }
    try:
        selected = zara.objects.get(slug=polls_slug)
        if request.method == 'GET':
            registration = reg()

        else:
            registration = reg(request.POST)
            if registration.is_valid():
                user_email = registration.cleaned_data['email']
                participate, _ = participant.objects.get_or_create(
                    email=user_email)
                selected.persons.add(participate)  # this line is not working
                # getting arguments from polls_slug
                return redirect('confirm-reg', polls_slug=polls_slug)
        return render(request, 'details.html', {
            'polls_found': True,
            'polls': selected,
            'form': registration
        })

    except Exception as exc:
        return render(request, 'registration.html', {
            'polls_found': False

        })


def confirmReg(request, polls_slug):
    polls = zara.objects.get(slug=polls_slug)
    return render(request, 'registration.html', {
        'R_email': polls.organizer_email

    })
