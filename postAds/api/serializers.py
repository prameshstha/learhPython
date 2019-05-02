from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField
from postAds.models import PostAd


class PostAdCreateSerializer(ModelSerializer):
    class Meta:
        model = PostAd
        fields = [
            'post_title',
            'post_image',
            'post_body',
            'post_image',
            'post_category',
            'post_created_at',
            'post_updated_at',

        ]


# for all the list view
class PostAdListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name="details",
        lookup_field='pk'
    )
    user = SerializerMethodField()

    class Meta:
        model = PostAd
        fields = [
            'url',
            'id',
            'post_user',
            'user',
            'post_title',
            'post_image',
            'post_created_at',
        ]

    def get_user(self, obj):
        return str(obj.post_user.username)


# for all the details view
# can be changed as required field and can be same
class PostAdDetailSerializer(ModelSerializer):
    user = SerializerMethodField()
    image = SerializerMethodField()
    markdown = SerializerMethodField()
    class Meta:
        model = PostAd
        fields = [
            'id',
            'user',
            'post_title',
            'post_image',
            'post_body',
            'markdown',
            'image',
            'post_category',
            'post_created_at',
            'post_updated_at',

        ]

    def get_user(self, obj):
        return str(obj.post_user.username)

    def get_image(self, obj):
        return str(obj.post_image.url)

    def get_markdown(self, obj):
        return str(obj.get_markdown)