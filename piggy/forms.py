from django import forms
from .models import Room, Scholar, Parent

class RoomForm(forms.ModelForm):

    class Meta:
        model = Room
        # fields = ('room.room_number', 'room.teacher_Name', 'room.scholar_Name', 'room.photo_url')
        fields = (
                'room_number',
                'teacher_Name',
           
                'photo_url'
                )

class ScholarForm(forms.ModelForm):

    class Meta:
        model = Scholar
        fields = ('scholar_name', 'photo_url', 'parent_Name', 'date_Of_Birth', 'teacher_Name', 'grade_Level','room_Number','pickup_Method')

class ParentForm(forms.ModelForm):

    class Meta:
        model = Parent
        fields = ('first_name','last_name', 'relation_To_Scholar', 'scholar', 'phone_number')