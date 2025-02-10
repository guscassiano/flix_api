from rest_framework.serializers import ModelSerializer
from actors.models import ActorModel


class ActorSerializers(ModelSerializer):

    class Meta:
        model = ActorModel
        fields = '__all__'
