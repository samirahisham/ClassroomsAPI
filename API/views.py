from rest_framework.generics import (ListAPIView ,CreateAPIView,RetrieveUpdateAPIView,RetrieveAPIView,DestroyAPIView)
from classes.models import Classroom
from .serializers import (ListSerializer,DetailSerializer,
CreateSerializer)

# Create your views here.

class ListView(ListAPIView):
    serializer_class =ListSerializer
    queryset = Classroom.objects.all()

class DetailView(RetrieveAPIView):
    queryset = Classroom.objects.all()
    serializer_class =DetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id' 

class UpdateView(RetrieveUpdateAPIView):
    serializer_class =DetailSerializer
    queryset = Classroom.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id' 

class DeleteView(DestroyAPIView):
    queryset = Classroom.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id' 



class CreateView(CreateAPIView):
	serializer_class=CreateSerializer
	def perform_create(self, serializer):
		serializer.save(teacher=self.request.user )