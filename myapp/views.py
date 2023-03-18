
# views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UploadedFile
import pandas as pd

def upload_file(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        UploadedFile.objects.create(file=uploaded_file)
        return redirect('file_list')
    return render(request, 'upload.html')

def file_list(request):
    files = UploadedFile.objects.all()
    return render(request, 'file_list.html', {'files': files})

def download_file(request, file_id):
    file = UploadedFile.objects.get(id=file_id)
    response = HttpResponse(file.file, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{file.file.name}"'
    return response

def open_file(request, file_id):
    file = UploadedFile.objects.get(id=file_id)
    df = pd.read_csv(file.file)  # or pd.read_excel(file.file)
    table = df.to_html()
    return render(request, 'table.html', {'table': table})
