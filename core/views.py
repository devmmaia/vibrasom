from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from .forms import SongForm
from django.core.files.storage import FileSystemStorage
from .models import Song

def upload(request):
    if request.method == 'POST' and request.FILES['musica']:
        myfile = request.FILES['musica']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'core/upload.html', {
            'uploaded': uploaded_file_url
        })
    form = SongForm()
    return render(request, 'core/upload.html', locals())


def list(request):
    songs = Song.objects.all()
    list_songs = list(map(lambda s: {"id": s.id, "titulo":  s.titulo}, songs))
    map()
    
    return JsonResponse({"songs": list_songs,})
