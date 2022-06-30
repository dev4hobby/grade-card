User = get_user_model()

class UserCreateSerializer(serializer.Serializer):
    email = serializer.EmailField(required=True)
    username = serializer.CharField(required=True)
    password = serializer.CharField(required=True)

    print(email)
    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user