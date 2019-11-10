from django.shortcuts import render

from web.models import Note


def index(request):
    if request.method == "POST":
        note = request.POST.get("note")
        new_note = Note(note=note)
        new_note.save()  # Save the note to the database
    return render(
        request,
        'index.html',  # Automagically finds the file using the settings.py
        context={
            "title": "Django Server",
            "description": "A full blown Django server",
            "has_notes": True,
            "notes": [note.note for note in Note.objects.all()]
        }
    )
