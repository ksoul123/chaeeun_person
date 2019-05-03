from django.shortcuts import render,get_object_or_404, redirect
from .models import Person
from django.utils import timezone
from .forms import PersonForm
# Create your views here.

def home(request):
    persons = Person.objects
    return render(request, 'blog/home.html',{'persons':persons} )

def detail(request, post_id):
    post_detail = get_object_or_404(Person, pk = post_id)
    return render(request, 'blog/detail.html',{'person':post_detail})

def person_new(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            person = form.save(commit=False)
            person.published_date = timezone.datetime.now()
            person.save()
            return redirect('home')
    else:
        form=PersonForm()
    return render(request, 'blog/person_new.html',{'form':form})

def post_edit(request,post_id):
    post = get_object_or_404(Person,pk=post_id)
    if request.method == "POST":
        form = PersonForm(request.POST,instance=post)
        if form.is_valid():
            person = form.save(commit = False)
            person.published_date = timezone.datetime.now()
            person.save()
            return redirect('detail', post_id=post.pk)
    else:
        form = PersonForm(instance=post)
    return render(request,'blog/post_edit.html',{'form':form})

def post_delete(request,post_id):
    post = get_object_or_404(Person, pk=post_id)
    post.delete()
    return redirect('home')