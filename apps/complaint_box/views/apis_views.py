from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers import ComplaintSerializer

class ComplaintCreateAPIView(APIView):
    """
    API لإنشاء شكوى جديدة
    """
    def post(self, request, *args, **kwargs):
        serializer = ComplaintSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "تم إرسال الشكوى بنجاح!"
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
