from rest_framework import serializers
# from apijson.models import NewApiJsonData, NewJsonData


class CoordsJsonSerializer(serializers.Serializer):

    accuracy = serializers.FloatField()
    altitude = serializers.FloatField()
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    heading = serializers.FloatField()
    speed = serializers.FloatField()
    altitudeAccuracy = serializers.FloatField()
    class Meta:
        # model = NewJsonData
        fields = ['accuracy', 'altitude', 'latitude', 'longitude',
                  'heading', 'speed', 'altitudeAccuracy']


class NewJsonSerializer(serializers.Serializer):
    
    _id = serializers.CharField()
    coords = CoordsJsonSerializer(many=False)
    mocked = serializers.BooleanField()
    timestamp = serializers.FloatField()
    _v = serializers.IntegerField()
    createdAt = serializers.CharField()
    updatedAt = serializers.CharField()

    class Meta:
        # model = NewApiJsonData
        fields = ['_id', 'coords', 'mocked',
                  'timestamp', '_v', 'createdAt', 'updatedAt']

    def create(self, validated_data):
        # print(validated_data)
        # mod_data = validated_data.pop('coords')
        # asset_model = NewJsonData.objects.create(**mod_data)
        # dataitem = NewApiJsonData.objects.create(
        #     coords=asset_model, **validated_data)
        return validated_data


# class UserSerializer(serializers.ModelSerializer):
#     # authentication
#     username=serializers.CharField()
#     password=serializers.CharField()
#     class Meta:
#         model = User
#         fields=['username','password']
