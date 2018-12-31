from django.shortcuts import render, redirect
from .models import AuthenticateUser
from random import randint
from django.core.mail import send_mail
from django import forms
from django.contrib.auth import get_user_model


def verify_user(request):
	if request.method == "GET":
		User = get_user_model().objects.all()
		User = User.filter(username = request.user.username).first()

		if User.authenticateuser.otp == -1:
			num = randint(100000, 200000)
			AuthenticateUser.objects.filter(user = User).update(otp = num)

			send_mail(
			    'OTP',
			    'Dear ' + request.user.username + '\nOTP: ' + str(num),
			    'appdjango99@gmail.com',
			    [request.user.email],
			    fail_silently=False,
			)
	else:
		User = get_user_model().objects.all()
		User = User.filter(username = request.user.username).first()
		
		otp = int(request.POST['otp'])
		user_otp = User.authenticateuser.otp

		if otp == user_otp:
			AuthenticateUser.objects.filter(user = User).update(is_verified = True)
			return redirect('/')
		else:
			raise forms.ValidationError("You entered a wrong OTP")

	return render(request, "templates/login_verify.html", {})