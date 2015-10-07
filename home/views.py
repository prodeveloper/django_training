from django.shortcuts import render
from .forms import StudentForm
from .forms import FeedbackForm
from django.core.mail import send_mail
# Create your views here.


def index(request):
    form = StudentForm(request.POST or None)

    context = {
        "hello_message": "Register new student",
        "form": form
    }

    if form.is_valid():
        instance = form.save(commit=False)
        full_name = form.cleaned_data.get('full_name')
        if full_name == "Jacob":
            full_name = "Developer"
        instance.full_name = full_name
        instance.save()

        context = {
            "hello_message": "Student Saved"
            }

    return render(request, 'index.html', context)


def feedback(request):
    form = FeedbackForm(request.POST or None)
    if form.is_valid():
        from_email = form.cleaned_data.get('email')
        full_name = form.cleaned_data.get('full_name')
        message = form.cleaned_data.get('message')
        prepared_message = "You have feedback from {} saying '{}'".format(full_name, message)
        send_mail('New feedback given', prepared_message, from_email,
            ['jacob@chenchatech.com'], fail_silently=False)
    context = {
        "form": form
    }
    return render(request, 'feedback.html', context)
