from rest_framework import serializers
from .models import Room,Scholar, Parent

class RoomSerializer(serializers.HyperlinkedModelSerializer):

    scholar = serializers.HyperlinkedRelatedField(
        view_name= 'scholar_detail',
        many= True,
        read_only= True
    )


    class Meta: 
        model= Room
        fields= ('id','room_number','teacher_Name','scholar_Name','photo_url','scholar')

class ScholarSerializer(serializers.HyperlinkedModelSerializer):

    parent = serializers.HyperlinkedRelatedField(
        view_name= 'parent_detail',
        many= True,
        read_only= True
    )
    class Meta: 
        model =Scholar
        fields= ('scholar_name', 'photo_url', 'parent_Name', 'date_Of_Birth', 'teacher_Name', 'grade_Level','room_Number','pickup_Method','parent_Number','parent')

class ParentSerializer(serializers.HyperlinkedModelSerializer):

    scholar = serializers.HyperlinkedRelatedField(
        view_name ='scholar_detail',
        many= True,
        read_only = True
    )


    class Meta: 
        model =Parent
        fields= ('first_name','last_name', 'relation_To_Scholar', 'scholar', 'phone_number')



    