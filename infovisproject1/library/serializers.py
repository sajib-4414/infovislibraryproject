from rest_framework import serializers

from library.models import Subjects


class SubjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = ['subject_text', 'hit_count']

    def to_representation(self, instance):
        # instance is the model object. create the custom json format by accessing instance attributes normaly and return it

        identifiers = dict()
        identifiers['Name'] = instance.subject_text
        identifiers['hits'] = instance.hit_count

        representation = {
            'identifiers': identifiers,
            'Name': instance.subject_text,
            'hits': instance.hit_count,
        }
        return representation