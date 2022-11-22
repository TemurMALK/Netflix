from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from rest_framework.generics import *
from .models import *
from .serializers import *

# class KinolarAPIView(APIView):
#     permission_classes = [IsAuthenticated, ]
#     def get(self, request):
#         kinolar = Kino.objects.all()
#         serializer = KinoSerializer(kinolar, many=True)
#         return Response(serializer.data)
#     def post(self, request):
#         kino = request.data
#         serializer = KinoSerializer(data=kino)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"success":"True", "data":serializer.data})
#         return Response("success","False")
#
# class AktyorqowAPIView(APIView):
#     permission_classes = [IsAuthenticated, ]
#     def post(self, request):
#         albom = request.data
#         serializer = AktyorSerializer(data=albom)
#         if serializer.is_valid():
#             serializer.save()
#             natija = {"xabar": "Saqlandi!",
#                       "qoshilgan malumot": serializer.data}
#             return Response(natija)
#         return Response({"xabar": "Jins kiritishda xatolik bor!"})
#
# class AktyorAPIView(APIView):
#     permission_classes = [IsAuthenticated, ]
#     def get(self, request, pk):
#         aktyor = Aktyor.objects.get(id=pk)
#         serializer = AktyorSerializer(aktyor)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         aktyor = Aktyor.objects.get(id=pk)
#         serializer = AktyorSerializer(aktyor, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             natija = {"xabar":"Saqlandi!",
#                       "qoshilgan malumot": serializer.data}
#             return Response(natija, status = status.HTTP_201_CREATED)
#         return Response({"xabar":"Ma'lumotda xatolik bor!", "detail":serializer.errors}).objects
#
#     def delete(self, reuqest, pk):
#         aktyor = Aktyor.objects.get(id=pk)
#         aktyor.delete()
#         return Response({"xabar":"Ma'lumot o'chdi!"})

#
# class CommentlarAPIView(APIView):
#     permission_classes = [IsAuthenticated, ]
#     def get(self, request):
#         commentlar = Comment.objects.all()
#         serializer = CommentSerializer(commentlar)
#         return Response(serializer.data)
#
# class CommentAPIView(APIView):
#     permission_classes = [IsAuthenticated, ]
#     def post(self, request):
#         comment = request.data
#         serializer = CommentSerializer(data=comment)
#         if serializer.is_valid():
#             serializer.save()
#             natija = {"Comment": "Saqlandi!",
#                       "qoshilgan comment": serializer.data}
#             return Response(natija)
#         return Response({"Error": "Comment kiritishda xatolik bor!"})




class KinoViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Kino.objects.all()
    serializer_class =KinoSerializer

    @action(methods=['GET'], detail=True)
    def commentlar(self, request, pk):
        comment = Comment.objects.filter(kino__id=pk)
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)

class AktyorViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Aktyor.objects.all()
    serializer_class =AktyorSerializer

class CommentViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class =CommentSerializer