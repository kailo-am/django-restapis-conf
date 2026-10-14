from django.shortcuts import render
from django.http import JsonResponse
from students.models import Student
from . serializers import StudentSerializer , EmployeeSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from employees.models import Employee
from rest_framework import mixins , generics,viewsets
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend



# def studentsView(request):
#     students = Student.objects.all()
# #manually serializing the query set
#     students_list = list(students.values())
#     print(students_list)
#     return JsonResponse(students_list , safe=False)

@api_view(['GET', 'POST'])
def studentsView(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students , many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) # for returning the serialized data in JSON format 
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def StudentDetailView(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# APIView for Employees

"""
This class-based view handles API requests related to employees.
class Employees(APIView):
    def get(self, request):
        # Handle GET request for employees list
        # You can implement the logic to retrieve and return the list of employees here
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # Handle POST request for creating a new employee
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeDetailView(APIView):
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return None
        
    def get(self, request, pk):
        # Handle GET request for a specific employee based on their primary key (pk)
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        # Handle PUT request for updating a specific employee based on their primary key (pk)
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # Handle DELETE request for deleting a specific employee based on their primary key (pk)
        employee = self.get_object(pk)
        if employee is not None: # which means employee is not None and exists in the database,not None means it is not empty
            employee.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'error': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)


"""        


# Mixins 
"""
class Employees(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):# generics.GenericAPIView is a base class for creating API views in 
                                            #Django REST Framework. It provides common functionality for handling HTTP requests and responses, such as request
                                            #  parsing, authentication, and response rendering.
                                            #mixins.ListModelMixin provides the functionality to handle GET requests for listing objects, while mixins.
                                            # CreateModelMixin provides the functionality to handle POST requests for creating new objects.
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request, *args, **kwargs):    # Handle GET request for employees list,*args and **kwargs are used to pass
                                                # any additional arguments or keyword arguments to the method. which means 
                                                # it can accept any number of positional and keyword arguments like example: if we 
                                                # want to pass any additional parameters in the URL, we can access them using *args and **kwargs.
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class EmployeeDetailView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer # serializer_class is used to specify the serializer that will be used to serialize and deserialize the data for this view. you dont 
    #need to pass getobject and request.data in the put method because the serializer_class will automatically handle the serialization and deserialization of the data based on the specified serializer.

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request,pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)

"""


#generics

# class Employees(generics.ListCreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer



"""class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'pk'  # Specify the lookup field for retrieving, updating, and deleting a specific employee based on their primary key (pk)
"""


#Viewsets
"""
class EmployeesViewSet(viewsets.ViewSet):
    def list(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            employee = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Response({'error': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
"""

#Model viewsets
class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filterset_fields = ['name', 'department']  # Specify the fields you want to filter on. You can add more fields as needed.
    filter_backends = [SearchFilter,DjangoFilterBackend]
    search_fields = ['name']