from django.shortcuts import render
from .models import Expense
from .serializers import ExpenseSerializer
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def getExpenses(self):
    expenses = Expense.objects.all()
    serializer = ExpenseSerializer(expenses, many=True)
    return Response(serializer.data,status= status.HTTP_200_OK)
@api_view(['POST'])
def createExpense(request):
    print("Received data:", request.data)  # Print received data for debugging
    serializer = ExpenseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()   
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response({"message": "bad Data format", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
@api_view(['DELETE'])
def deleteExpense(request,pk):
    try:
        expense = Expense.objects.get(pk=pk)
    except Expense.DoesNotExist:
        return Response({"message": "Expense not found"}, status=status.HTTP_404_NOT_FOUND)
    expense.delete()
    return Response ({"message":"data deleted sucessfully"},status=status.HTTP_200_OK)

@api_view(['GET'])
def filterCategory(request,category):
    expenses = Expense.objects.filter(category=category)
    serializer = ExpenseSerializer(expenses, many=True)
    return Response(serializer.data,status= status.HTTP_200_OK)
