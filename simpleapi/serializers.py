from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import update_session_auth_hash

UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(style={'input_type' : 'password'}, write_only=True)

    def create(self, validated_data):

        user = UserModel.objects.create_user( 
            username=validated_data['username'],
            password=validated_data['password'],
        )
        return user
    def update(self, instance, validated_data):
            instance.username = validated_data.get('username', instance.username)

            instance.save()

            password = validated_data.get('password', None)
            #confirm_password = validated_data.get('confirm_password', None)
            instance.set_password(password)
            instance.save()

            update_session_auth_hash(self.context.get('request'), instance)

            return instance   
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password')