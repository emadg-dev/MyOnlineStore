from django.urls import path 
from .views import SignUpView
# ,PasswordUpdateConfirmView, PasswordUpdateView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    # path('changepassword/', PasswordUpdateView.as_view(), name='changepassword'),
    # path('changepassword/confirmed/', PasswordUpdateConfirmView.as_view(), name='passwordupdateconfirm'),

]