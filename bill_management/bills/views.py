from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Bill, Payment, Customer
from .serializers import BillSerializer, PaymentSerializer
from .serializers import UserRegistrationSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny


class BillListCreateView(generics.ListCreateAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    permission_classes = [IsAuthenticated]

class PaymentListCreateView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

class BillListView(generics.ListCreateAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer


class BillerAnalysisView(generics.GenericAPIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        # Example logic for analysis
        total_bills = Bill.objects.filter(customer__user=request.user).count()
        total_payments = Payment.objects.filter(bill__customer__user=request.user).count()
        return Response({"total_bills": total_bills, "total_payments": total_payments}, status=status.HTTP_200_OK)

class UserRegistrationView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)