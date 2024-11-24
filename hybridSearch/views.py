from rest_framework import viewsets
from rest_framework import filters
from .models import MagazineInfo, MagazineContent
from .serializers import MagazineInfoSerializer, MagazineContentSerializer

# ViewSet for MagazineInfo
class MagazineInfoViewSet(viewsets.ModelViewSet):
    queryset = MagazineInfo.objects.all()
    serializer_class = MagazineInfoSerializer
    filter_backends = (filters.SearchFilter,)  
    search_fields = ['title','category','id']   

# ViewSet for MagazineContent
class MagazineContentViewSet(viewsets.ModelViewSet):
    queryset = MagazineContent.objects.all()
    serializer_class = MagazineContentSerializer
