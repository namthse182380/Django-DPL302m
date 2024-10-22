from django.urls import path
from .views import homepage

urlpatterns = [
    path('', homepage, name='homepage'),  # Đường dẫn cho homepage
    # path('upload/', upload_video, name='upload_video'),  # Đường dẫn cho trang tải lên video
]
