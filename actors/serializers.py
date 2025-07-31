from rest_framework.serializers import ModelSerializer, CharField
from actors.models import ActorModel, Nationality


class ActorSerializers(ModelSerializer):
    nationality = CharField(source='nationality.name', read_only=True)

    class Meta:
        model = ActorModel
        fields = ['id', 'name', 'birthday', 'nationality']


class NationalitySerializer(ModelSerializer):

    class Meta:
        model = Nationality
        fields = ['id', 'name']