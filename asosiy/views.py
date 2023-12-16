from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializer import *


class MahsulotApiView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        mahsulot = Mahsulot.objects.all()
        serializer = MahsulotSerializer(mahsulot, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MahsulotSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            data = request.data
            id = data.get('id')
            mahsulot = Mahsulot.objects.get(pk=id)
            mahsulot.delete()
            return Response({"message": "Successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Mahsulot.DoesNotExist:
            return Response({"message": "Error"}, status=status.HTTP_404_NOT_FOUND)

class MahsulotOzgartirishApiView(APIView):
    def get(self, request, pk):
        mahsulot = Mahsulot.objects.filter(pk=pk).first()

        if mahsulot:
            serializer = MahsulotSerializer(mahsulot)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Mahsulot topilmadi"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            mahsulot = Mahsulot.objects.get(pk=pk)
            serializer = MahsulotSerializer(mahsulot, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Mahsulot.DoesNotExist:
            return Response({"message": "Ma'lumot topilmadi"}, status=status.HTTP_404_NOT_FOUND)


class Qarzdorlik_sotuvchiApiView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        qarzdorlik_s = Qarzdorlik_sotuvchi.objects.all()
        serializer = Qarzdorlik_sotuvchiSerializer(qarzdorlik_s, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Qarzdorlik_sotuvchiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            data = request.data
            id = data.get('id')
            mahsulot = Qarzdorlik_sotuvchi.objects.get(pk=id)
            mahsulot.delete()
            return Response({"message": "Successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Qarzdorlik_sotuvchi.DoesNotExist:
            return Response({"message": "Error"}, status=status.HTTP_404_NOT_FOUND)

class Qarzdorlik_sotuvchiOzgartirishApiView(APIView):
    def get(self, request, pk):
        qarz_s = Qarzdorlik_sotuvchi.objects.filter(pk=pk).first()

        if qarz_s:
            serializer = Qarzdorlik_sotuvchiSerializer(qarz_s)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Mahsulot topilmadi"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            mahsulot = Qarzdorlik_sotuvchi.objects.get(pk=pk)
            serializer = Qarzdorlik_sotuvchiSerializer(mahsulot, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Qarzdorlik_sotuvchi.DoesNotExist:
            return Response({"message": "Ma'lumot topilmadi"}, status=status.HTTP_404_NOT_FOUND)

class Qarzdorlik_mijozApiView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        mahsulot = Qarzdorlik_mijoz.objects.all()
        serializer = Qarzdorlik_mijozSerializer(mahsulot, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Qarzdorlik_mijozSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            data = request.data
            id = data.get('id')
            mahsulot = Qarzdorlik_mijoz.objects.get(pk=id)
            mahsulot.delete()
            return Response({"message": "Successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Qarzdorlik_mijoz.DoesNotExist:
            return Response({"message": "Error"}, status=status.HTTP_404_NOT_FOUND)

class Qarzdorlik_mijozOzgartirishApiView(APIView):
    def get(self, request, pk):
        qarz_m = Qarzdorlik_mijoz.objects.filter(pk=pk).first()

        if qarz_m:
            serializer = Qarzdorlik_mijozSerializer(qarz_m)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Mahsulot topilmadi"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            mahsulot = Qarzdorlik_mijoz.objects.get(pk=pk)
            serializer = Qarzdorlik_mijozSerializer(mahsulot, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Qarzdorlik_mijoz.DoesNotExist:
            return Response({"message": "Ma'lumot topilmadi"}, status=status.HTTP_404_NOT_FOUND)

class KirmApiView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        mahsulot = Kirim.objects.all()
        serializer = KirimSerializer(mahsulot, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = KirimSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            data = request.data
            id = data.get('id')
            mahsulot = KirimSerializer.objects.get(pk=id)
            mahsulot.delete()
            return Response({"message": "Successfully"}, status=status.HTTP_204_NO_CONTENT)
        except KirimSerializer.DoesNotExist:
            return Response({"message": "Error"}, status=status.HTTP_404_NOT_FOUND)

class KirimOzgartirishApiView(APIView):
    def get(self, request, pk):
        kirim = Kirim.objects.filter(pk=pk).first()

        if kirim:
            serializer = KirimSerializer(kirim)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Mahsulot topilmadi"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            mahsulot = Kirim.objects.get(pk=pk)
            serializer = KirimSerializer(mahsulot, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Kirim.DoesNotExist:
            return Response({"message": "Ma'lumot topilmadi"}, status=status.HTTP_404_NOT_FOUND)
# Create your views here.
