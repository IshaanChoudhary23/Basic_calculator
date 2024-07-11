
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import OperationSerializer,PalindromeSerializer,PatternSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle



class CalculatorView(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    def post(self, request):
        serializer = OperationSerializer(data=request.data)
        if serializer.is_valid():
            operation = serializer.validated_data['operation']
            operand1 = serializer.validated_data['num1']
            operand2 = serializer.validated_data['num2']

            if operation == 'add':
                result = operand1 + operand2
            elif operation == 'subtract':
                result = operand1 - operand2
            elif operation == 'multiply':
                result = operand1 * operand2
            elif operation == 'div':
                result = operand1/operand2    

            data={
                'provided_operation':operation,
                'provided_number_1':operand1,
                'provided_number_2':operand2,

                'After the calculation output is ': result
                }
            return Response(data, status=status.HTTP_200_OK)
        

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class CheckPalindromeView(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    def post(self, request):
        serializer = PalindromeSerializer(data=request.data)
        
        if serializer.is_valid():
            number = serializer.validated_data['number']
            original_number = number 
            reversed_num = 0
            
            while number != 0:
                digit = number % 10
                reversed_num = reversed_num * 10 + digit
                number //= 10

            if original_number == reversed_num:
                return Response({'result': 'provided number is palindrome'}, status=status.HTTP_200_OK)
            else:
                return Response({'result': 'provided number is not palindrome'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class PatternView(APIView):
    def post(self,request):
        serializer =PatternSerializer(data=request.data)
        if serializer.is_valid():
            n=serializer.validated_data['input']
            type=serializer.validated_data['type']
            data={}
            if type=='normal':
                for i in range(1,n+1):
                    data[i]="*"*i
                return Response(data,status=status.HTTP_200_OK)
            elif type=='iso':
                for i in range(1, n + 1):
                    spaces = ' ' * (n - i)
                    stars = '*' * (2 * i - 1)
                    data[i] = spaces + stars
                return Response(data,status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
