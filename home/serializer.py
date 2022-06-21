from rest_framework import serializers
from .models import Todo




class TodoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =Todo
        fields= '__all__'
        
    def validate(self, validated_data):
        if validated_data.get('todo_title'):
            todo_title = validated_data['todo_title']
            if not todo_title.isalpha():
                raise serializers.ValidationError('Title contains only english letters')
        return validated_data 
        
        