from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
# Create your views here.
from .forms import SongForm
from django.core.files.storage import FileSystemStorage
from .models import Song
from . import conversao
from pathlib import Path


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


def _song_json(song):
    return {"id": song.id, "titulo": song.titulo}


def list(request):
    songs = Song.objects.all()
    list_songs = [_song_json(s) for s in songs]
    
    return JsonResponse(list_songs, safe=False)   

def converte(request, id):
    song = Song.objects.get(pk=id)
    padrao = conversao.get_padrao_vibracao(song.arquivo.file)
    return JsonResponse({"padrao": padrao, })


def download(request, id):
    song = Song.objects.get(pk=id)
    file_path = Path(song.arquivo.file.name)
    with open(file_path, 'rb') as reader:
        response = HttpResponse(reader.read(),
                                content_type="audio/wav")
        response['Content-Disposition'] = 'inline; filename=' + file_path.name
        return response
    raise Http404