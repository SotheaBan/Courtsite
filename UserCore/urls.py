from django.urls import path
from .views import CustomTokenObtainPairView, TokenRefreshView,ProtectedView

urlpatterns = [
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('protected_resource/', ProtectedView.as_view(), name='protected-resource'),
]