from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token


class CreateAdminUserAPIView(APIView):
    def post(self, request, *args, **kwargs):
        # Foydalanuvchi ma'lumotlari
        username = request.data.get('username')
        password = request.data.get('password')

        # Foydalanuvchi mavjudligini tekshirish
        if User.objects.filter(username=username).exists():
            return Response({'message': 'Bunday nomdagi username allaqachon band'}, status=status.HTTP_400_BAD_REQUEST)

        # Foydalanuvchi yaratish
        user = User.objects.create_user(username=username, password=password, is_staff=True)

        # Agar muvaffaqiyatli bo'lsa, 201 Created statusni qaytarish
        return Response({'message': 'Foydalanuvchi muvaffaqiyatli yaratildi.'}, status=status.HTTP_201_CREATED)

class AdminLoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:
            login(request, user)

            # Tokenni olish
            token, created = Token.objects.get_or_create(user=user)

            return Response({'message': 'Admin user successfully logged in', 'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid credentials or not an admin user'},
                            status=status.HTTP_401_UNAUTHORIZED)
class MahsulotApiView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        mahsulotlar = Mahsulot.objects.filter(user=request.user)
        serializer = MahsulotSerializer(mahsulotlar, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MahsulotSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            mahsulot = serializer.save(user=request.user)  # Foydalanuvchi ma'lumotlarini qo'shish
            return Response(MahsulotSerializer(mahsulot).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MahsulotOzgartirishApiView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        mahsulot = Mahsulot.objects.filter(pk=pk, user=request.user).first()

        if mahsulot:
            serializer = MahsulotSerializer(mahsulot)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Mahsulot topilmadi"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            mahsulot = Mahsulot.objects.get(pk=pk, user=request.user)
            serializer = MahsulotSerializer(mahsulot, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Mahsulot.DoesNotExist:
            return Response({"message": "Ma'lumot topilmadi"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            mahsulot = Mahsulot.objects.get(pk=pk, user=request.user)
            mahsulot.delete()
            return Response({"message": "Successfully deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Mahsulot.DoesNotExist:
            return Response({"message": "Error, ma'lumot topilmadi yoki o'chirish mumkin emas"},
                            status=status.HTTP_404_NOT_FOUND)

class Qarzdorlik_sotuvchiApiView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        mahsulotlar = Qarzdorlik_sotuvchi.objects.filter(user=request.user)
        serializer = Qarzdorlik_sotuvchiSerializer(mahsulotlar, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Qarzdorlik_sotuvchiSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(user=request.user)  # Foydalanuvchi ma'lumotlarini qo'shish
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Qarzdorlik_sotuvchiOzgartirishApiView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        qarz_s = Qarzdorlik_sotuvchi.objects.filter(pk=pk, user=request.user).first()

        if qarz_s:
            serializer = Qarzdorlik_sotuvchiSerializer(qarz_s)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Mahsulot topilmadi"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            mahsulot = Qarzdorlik_sotuvchi.objects.get(pk=pk, user=request.user)
            serializer = Qarzdorlik_sotuvchiSerializer(mahsulot, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Qarzdorlik_sotuvchi.DoesNotExist:
            return Response({"message": "Ma'lumot topilmadi"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            mahsulot = Qarzdorlik_sotuvchi.objects.get(pk=pk, user=request.user)
            mahsulot.delete()
            return Response({"message": "Successfully deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Qarzdorlik_sotuvchi.DoesNotExist:
            return Response({"message": "Error"}, status=status.HTTP_404_NOT_FOUND)


class Qarzdorlik_mijozApiView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        mahsulotlar = Qarzdorlik_mijoz.objects.filter(user=request.user)
        serializer = Qarzdorlik_mijozSerializer(mahsulotlar, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Qarzdorlik_mijozSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(user=request.user)  # Foydalanuvchi ma'lumotlarini qo'shish
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Qarzdorlik_mijozOzgartirishApiView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    def get(self, request, pk):
        qarz_m = Qarzdorlik_mijoz.objects.filter(pk=pk, user=request.user).first()

        if qarz_m:
            serializer = Qarzdorlik_mijozSerializer(qarz_m)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Mahsulot topilmadi"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            mahsulot = Qarzdorlik_mijoz.objects.get(pk=pk, user=request.user)
            serializer = Qarzdorlik_mijozSerializer(mahsulot, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Qarzdorlik_mijoz.DoesNotExist:
            return Response({"message": "Ma'lumot topilmadi"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            mahsulot = Qarzdorlik_mijoz.objects.get(pk=pk, user=request.user)
            mahsulot.delete()
            return Response({"message": "Successfully deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Qarzdorlik_mijoz.DoesNotExist:
            return Response({"message": "Error"}, status=status.HTTP_404_NOT_FOUND)

class KirimApiView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        mahsulotlar = Kirim.objects.filter(user=request.user)
        serializer = KirimSerializer(mahsulotlar, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = KirimSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(user=request.user)  # Foydalanuvchi ma'lumotlarini qo'shish
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class KirimOzgartirishApiView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        kirim = Kirim.objects.filter(pk=pk, user=request.user).first()

        if kirim:
            serializer = KirimSerializer(kirim)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Mahsulot topilmadi"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            mahsulot = Kirim.objects.get(pk=pk, user=request.user)
            serializer = KirimSerializer(mahsulot, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Kirim.DoesNotExist:
            return Response({"message": "Ma'lumot topilmadi"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            mahsulot = Kirim.objects.get(pk=pk, user=request.user)
            mahsulot.delete()
            return Response({"message": "Successfully deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Kirim.DoesNotExist:
            return Response({"message": "Error"}, status=status.HTTP_404_NOT_FOUND)

