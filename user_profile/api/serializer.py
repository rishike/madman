from rest_framework import serializers
from user_profile.models import Profile
from user_profile.models import Address
from accounts.api.serializer import UserDisplaySerializer


class AddressDisplaySerializer(serializers.ModelSerializer):
	class Meta:
		model = Address
		fields = [
			'street_address',
			'city',
			'state',
			'pincode',
			'country',		
		]

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
	# user = UserDisplaySerializer()
	permanent_address = AddressDisplaySerializer()
	friends = serializers.SerializerMethodField()

	class Meta:
		model = Profile
		fields = [
		'name',
		'email',
		'phone_number',
		'gender',
		'profile_pic',
		'dob',
		'permanent_address',
		'friends',
		]

	def get_friends(self, obj):
		return obj.friends.all().count()


