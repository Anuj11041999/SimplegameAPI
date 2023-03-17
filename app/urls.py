from django.urls import path, include
from .views import CreateView,GameView
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')


urlpatterns = [
    path('swagger',schema_view),
    path('all', CreateView.as_view()),
    path('game/<int:pk>/', GameView.as_view()),
    
    
]
