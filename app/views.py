from django.shortcuts import render
from .serializer import GameSerializer
from rest_framework.generics import GenericAPIView
from .models import Game
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .permissions import IsReviewUserOrReadOnly
# Create your views here.

class CreateView(GenericAPIView):
    serializer_class = GameSerializer
    def get(self, request):
        platform = Game.objects.all()
        serializer = GameSerializer(
            platform, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = GameSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class GameView(GenericAPIView):
    serializer_class = GameSerializer
    
    def get(self, request, pk):
        try:
            game = Game.objects.get(pk=pk)
        except Game.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = GameSerializer(
            game, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        game = Game.objects.get(pk=pk)
        serializer = GameSerializer(game, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        game = Game.objects.get(pk=pk)
        game.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
        
    
    
