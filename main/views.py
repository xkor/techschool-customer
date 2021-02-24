from rest_framework import (
    views, response, permissions, authentication
)
from .serializers import CustomerSerializer


class CustomerCreateView(views.APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def post(self, request):
        context = {'user': request.user}
        serializer = CustomerSerializer(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data)
