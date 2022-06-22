from rest_framework import serializers
from jdm.models import Brand, Body, Transmission, DriveType, Car, Comment, Post


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
   

class BodySerializer(serializers.ModelSerializer):
    class Meta:
        model = Body
        fields = '__all__'
             

class TransmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transmission
        fields = '__all__'


class DriveTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriveType
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'