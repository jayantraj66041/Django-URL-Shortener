from rest_framework.serializers import ModelSerializer
from api.models import UrlManage


class UrlManageSerializer(ModelSerializer):
    class Meta:
        model = UrlManage
        fields = ['url', 'short_url']