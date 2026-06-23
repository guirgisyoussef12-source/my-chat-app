from django.contrib.auth import get_user_model
from rest_framework import serializers
User = get_user_model
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username","email"]
        read_only_fields = fields
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,min_length=8,tirm_whitespace=False)
    class Meta:
        model = User
        fields = ["username","email","password"]
    def validate_email(self,value):
        email = value.strip().lower()
        if User.objects.filter(email__iexact=email).exists():
            raise serializers.ValidationError("this email is already used")
        return email
    def validate_username(self,value):
        username = value.strip()
        if user.objects.filter(username__iexact=username).exists():
            raise serializers.ValidationError("this username is already used")
        return username
    def create(self,validate_date):
        return User.objects.create_user(
            username = validate_date["username"],
            email = validate_date["email"],
            password = validate_date["password"],
        )
