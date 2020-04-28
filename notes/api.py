from rest_framework import serializers, viewsets
from .models import PersonalNotes, Notes

class PersonalNotesSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        user = self.context['request'].user
        notes = PersonalNotes.objects.create(user=user, **validated_data)
        return notes

    def get_queryset(self):
        user = self.request.user

        if user.is_anonymous:
            return PersonalNotes.objects.none()
        else:
            return PersonalNotes.objects.filter(user=user)

    class Meta:
        model = PersonalNotes
        fields = ('title', 'content')


class PersonalNotesViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalNotesSerializer
    queryset = Notes.objects.none()
#    queryset = PersonalNotes.objects.all()