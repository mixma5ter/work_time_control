from rest_framework import generics

from .models import Employee
from .serializers import EmployeeSerializer


class EmployeeListView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetailView(generics.RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'card_number'
    # permission_classes = [permissions.IsAuthenticated]
