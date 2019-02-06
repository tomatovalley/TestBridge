<<<<<<< HEAD
from rest_framework import serializers
from Projects.models import Project

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        
    def get_url(self, obj):
        request = self.context.get("request")
=======
from rest_framework import serializers
from Projects.models import Project

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        
    def get_url(self, obj):
        request = self.context.get("request")
>>>>>>> 1e76af9444df3aa6779f6bd26b224af9d9dea43c
        return obj.get_api_url(request=request)