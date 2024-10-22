# Create your views here.

from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
# from .utils import detect_deepfake

def homepage(request):
    return render(request, 'detection/homepage.html')

# def upload_video(request):
#     if request.method == 'POST' and request.FILES['video']:
#         video = request.FILES['video']
#         fs = FileSystemStorage()
#         filename = fs.save(video.name, video)
#         uploaded_file_url = fs.url(filename)
        
#         # Gọi hàm phát hiện deepfake
#         result = detect_deepfake(uploaded_file_url)
        
#         return render(request, 'detection/result.html', {'result': result})
    
#     return render(request, 'detection/upload.html')
