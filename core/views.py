import os
from django import http
from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from PIL import Image
from zipfile import ZipFile

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def convert(request):
    if request.method == 'POST':
        files = request.FILES.getlist('file')
        with ZipFile('convert.zip', 'w') as zipObj:
            for f in files:
                
                im = Image.open(f)
                fn , ext = os.path.splitext(f.name)
               
                extjpg ='.jpg'
                fill_color= (255,255,255)

                if im.mode in ('RGBA', 'LA'):
                    background = Image.new(im.mode[:-1], im.size, fill_color)
                    background.paste(im , im.split()[-1])
                    im = background
                im_output= im.convert('RGB')
                im_output.save("Foto/{}{}".format(fn,extjpg), quality=95)
               
                zipObj.write("Foto/{}{}".format(fn,extjpg))
                os.remove("Foto/{}{}".format(fn,extjpg))
            zip_file = open('convert.zip', 'rb')
            return FileResponse(zip_file)
                
        
        
                    