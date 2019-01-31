from rest_framework import serializers
from Projects.models import Project

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        
    def get_url(self, obj):
        request = self.context.get("request")
        return obj.get_api_url(request=request)