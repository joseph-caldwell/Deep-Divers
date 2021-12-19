from .models import Article
from .serializers import ArticleSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework import mixins
 
 
 
class ArticleViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin):
        serializer_class = ArticleSerializer
        queryset = Article.objects.all()



 
    # def list(self, request):
    #     articles = Article.objects.all()
    #     serializer = ArticleSerializer(articles, many=True)
    #     return Response(serializer.data)
 
 
    # def create(self, request):
    #     serializer = ArticleSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
 
    # def retrieve(self, request, pk=None):
    #     queryset = Article.objects.all()
    #     article = get_object_or_404(queryset, pk=pk)
    #     serializer = ArticleSerializer(article)
    #     return Response(serializer.data)

    # def update(self, request, pk=None):
    #     article = Article.objects.get( pk=pk)
    #     serializer = ArticleSerializer(article, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)