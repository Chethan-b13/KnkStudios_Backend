from drf_yasg.utils import serializers
from .models import Profile,Style

class SignupSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    password2 = serializers.CharField()
    name = serializers.CharField()


class makeAdminSerializer(serializers.Serializer):
    email = serializers.EmailField()


class StyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Style
        fields = '__all__'
class ProfileSerializer(serializers.ModelSerializer):
    team = StyleSerializer(many=True)
    class Meta:
        model = Profile
        fields = '__all__'

