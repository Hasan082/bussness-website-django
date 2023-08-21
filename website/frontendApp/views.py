from django.shortcuts import render
from adminPanel.models import aboutus


def index(request):
    about_us = aboutus.objects.last()
    title = about_us.about_title

    words = title.split()
    last_word_result = words[-1] if words else ""

    first_part = ' '.join(words[:-1]) 

    context = {
        "first_part": first_part,
        "last_word_result": last_word_result,
        "about_us": about_us,
    }

    return render(request, 'frontend/index.html', context)

def about(request):
    about_us = aboutus.objects.last()
    title = about_us.about_title

    words = title.split()
    last_word_result = words[-1] if words else ""

    first_part = ' '.join(words[:-1]) 

    context = {
        "first_part": first_part,
        "last_word_result": last_word_result,
        "about_us": about_us,
    }
    return render(request, 'frontend/about.html', context)
