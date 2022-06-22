from rest_framework import viewsets, permissions
from jdm.models import Brand, Body, Transmission, DriveType, Car, Comment, Post
from .serializers import BrandSerializer, BodySerializer, TransmissionSerializer, DriveTypeSerializer, CarSerializer, CommentSerializer, PostSerializer


class BrandViewSet(viewsets.ModelViewSet):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()
    permission_classes = [permissions.IsAdminUser]


class BodyViewSet(viewsets.ModelViewSet):
    serializer_class = BodySerializer
    queryset = Body.objects.all()
    permission_classes = [permissions.IsAdminUser]


class TransmissionViewSet(viewsets.ModelViewSet):
    serializer_class = TransmissionSerializer
    queryset = Transmission.objects.all()
    permission_classes = [permissions.IsAdminUser]


class DriveTypeViewSet(viewsets.ModelViewSet):
    serializer_class = DriveTypeSerializer
    queryset = DriveType.objects.all()
    permission_classes = [permissions.IsAdminUser]


class CarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    permission_classes = [permissions.IsAdminUser]


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [permissions.IsAdminUser]


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [permissions.IsAdminUser]