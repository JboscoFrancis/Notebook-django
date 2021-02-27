from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .forms import NoteForm
from . models import Note

# Create your views here.
def index(request):
    note = Note.objects.all().order_by('-date_created')

    #create note form
    form = NoteForm()
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('index')
        else:
            messages.info(request, f'sorry something went wrong')
    context ={'note': note, 'form':form}
    return render(request, 'note/index.html', context)

def detail(request, pk):
    note = Note.objects.get(id=pk)

    #edit note form
    form = NoteForm(instance=note)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid:
            form.save()
            return redirect('detail',pk)
    context = {'note':note, 'form': form}
    return render(request, 'note/detail.html', context)

def notedel(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return redirect('index')

@csrf_exempt    #exempt cerf token
def complete(request):
    data = json.loads(request.body)
    noteid = data['noteId']
    action = data['action']
    print(action)
    note = Note.objects.get(id=noteid)
    if action == 'False':
        note.complete=True
        note.save()
    else:
        note.complete=False
        note.save()
    return JsonResponse('data sent', safe=False)