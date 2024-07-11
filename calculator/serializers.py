# calculator/serializers.py

from rest_framework import serializers # type: ignore

class OperationSerializer(serializers.Serializer):
    operation = serializers.CharField(error_messages={"required":"check th spelling"})
    num1 = serializers.FloatField(error_messages={"invalid":"num1 must be a integer"})
    num2 = serializers.FloatField()
    

    def validate_operation(self, value):
        if value not in ['add', 'subtract', 'multiply','div']:
            raise serializers.ValidationError("Invalid operation. Choose from 'add', 'subtract', 'multiply'.")
        
        else:
            return value
        

class PalindromeSerializer(serializers.Serializer):
    number=serializers.IntegerField()

    def validate_number(self,value):
        if value==0:
            raise serializers.ValidationError("number should not be equal to zero")
        # elif value>0 or value<10:
        #     raise serializers.ValidationError(" provide the number which is greater than and equal to 10 ")

        
        else:
            return value
        
class PatternSerializer(serializers.Serializer):
    input=serializers.IntegerField()
    type=serializers.CharField()


    def validate_type(self,value):
        if value not in ['normal','iso']:
            raise serializers.ValidationError("provide a vaild type")
        
        else:
            return value


    def validate_number(self,value):
        if value==0:
            raise serializers.ValidationError("number should not be equal to zero")
        
        else:
            return value



