from django.urls import path
from .views import BillListCreateView, PaymentListCreateView, BillerAnalysisView, BillListView

urlpatterns = [
    path('bills/', BillListCreateView.as_view(), name='bill-list-create'),
    path('bills/<int:pk>/payments/', PaymentListCreateView.as_view(), name='payment-list-create'),
    path('bills/reports/biller-analysis/', BillerAnalysisView.as_view(), name='biller-analysis'),
    path('bills/', BillListView.as_view(), name='bill-list'),
    
   ]
