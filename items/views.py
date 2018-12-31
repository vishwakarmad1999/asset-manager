from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic  import (
					TemplateView, 
					ListView, 
					DetailView, 
					CreateView,
					UpdateView,
					DeleteView,
					)
from .models import Asset
from .forms import AssetModelForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
import datetime
# import pandas as pd
# from math import isnan
from django.http import Http404

# Create your views here.

class ItemsListView(LoginRequiredMixin, ListView):
	def get(self, request, *args, **kwargs):
		template_name = 'templates/home.html'
		queryset = Asset.objects.filter(user = request.user)

		context = {
			"object_list": queryset,
			"flag": True
		}

		if request.GET and request.GET['q'].strip():
			q = str(request.GET['q'])

			try:
				search_result = 	queryset.filter(
												Q(date_of_purchase = datetime.datetime.strptime(q, "%d-%m-%Y")) |
												Q(warranty_expiry = datetime.datetime.strptime(q, "%d-%m-%Y"))
											)
			except:
				search_result = 	queryset.filter(
													Q(asset_id__iexact = q) |
												Q(email_id__icontains = q) |
												Q(plant__icontains = q) |
												Q(location__icontains = q) |
												Q(department__icontains = q) | 
												Q(username__icontains = q) |
												Q(hostname__icontains = q) |
												Q(model__icontains = q) |
												Q(configuration__icontains = q) |
												Q(amount__icontains = q) |
												Q(asset_code__icontains = q) |
												Q(category__iexact = q)
											)
			if len(search_result) == 0:
				context['flag'] = False
			else:
				context['search_result'] = search_result.distinct()

		return render(request, template_name, context)


class ItemView(DetailView):
	template_name = 'templates/item.html'
	queryset = Asset.objects.all()


class ItemCreateView(CreateView, LoginRequiredMixin):
	template_name = "templates/create.html"
	success_url = "/"
	form_class = AssetModelForm

	def form_valid(self, form):
		instance = form.save(commit = False)
		instance.user = self.request.user
		return super(ItemCreateView, self).form_valid(form)


class ItemUpdateView(LoginRequiredMixin, UpdateView):
	template_name = "templates/update.html"
	success_url = "/"
	form_class = AssetModelForm

	def get_queryset(self):
		queryset = Asset.objects.filter(user = self.request.user)
		return queryset


class ItemDeleteView(LoginRequiredMixin, DeleteView):
	template_name = 'templates/delete.html'
	model = Asset
	success_url = '/'

	def get_context_data(self, *args, **kwargs):
		context = super(ItemDeleteView, self).get_context_data(*args, **kwargs)
		obj = get_object_or_404(Asset, id__iexact = kwargs['object'].id, user = self.request.user)
		return context


def add_from_excel(request):
	raise Http404
	# template_name = 'templates/create.html'
	# df = pd.read_excel('templates/IT_Asset_SEZ.xlsx', skiprows = 2)
	
	# len_df = len(df)
	# # df.loc[171]['Amount'] = 130000

	# count = Asset.objects.count()

	# while count < 217:
	# 	obj = Asset()
	# 	obj.user 			= request.user

	# 	obj.category 		= df.loc[count]['Category']

	# 	obj.plant 			= df.loc[count]['Plant']

	# 	obj.location 		= df.loc[count]['LOCATION']

	# 	obj.department 		= df.loc[count]['Department']

	# 	try:
	# 		if isnan(df.loc[count]['User Name']):
	# 			obj.username= None
	# 	except:
	# 		obj.username 	= df.loc[count]['User Name']
		
	# 	try:
	# 		if isnan(df.loc[count]['Host Name']):
	# 			obj.username= None
	# 	except:
	# 		obj.hostname 	= df.loc[count]['Host Name']

	# 	try:
	# 		if isnan(df.loc[count]['EMail ID']):
	# 			obj.email_id= 'none@none.com'
	# 	except:
	# 		obj.email_id 	= df.loc[count]['EMail ID']

	# 	try:
	# 		if isnan(df.loc[count]['MODEL']):
	# 			obj.model 	= None
	# 	except:
	# 		obj.model 		= df.loc[count]['MODEL']

	# 	try:
	# 		if isnan(df.loc[count]['ASSET CODE ']):
	# 			obj.asset_code = None
	# 	except:
	# 		obj.asset_code 	= df.loc[count]['ASSET CODE ']
		
	# 	if type(df.loc[count]['Date of Purchase']) == datetime.datetime:
	# 		obj.date_of_purchase= df.loc[count]['Date of Purchase'].date()
	# 	if type(df.loc[count]['Warrenty expiry']) == datetime.datetime:
	# 		obj.warranty_expiry	= df.loc[count]['Warrenty expiry'].date()
		
	# 	try:
	# 		if isnan(df.loc[count]['Configuration']):
	# 			obj.configuration	= None
	# 	except:
	# 		obj.configuration	= df.loc[count]['Configuration']
		
	# 	if df.loc[count]['Amount'].__class__ == type(1):
	# 		obj.amount			= df.loc[count]['Amount']

	# 	try:
	# 		if isnan(df.loc[count]['OS']):
	# 			obj.operating_system= None
	# 	except:
	# 		obj.operating_system= df.loc[count]['OS']

	# 	try:
	# 		if isnan(df.loc[count]['Asset ID']):
	# 			obj.asset_id 	= None
	# 	except:
	# 		obj.asset_id 		= df.loc[count]['Asset ID']

	# 	obj.save()

	# 	count += 1

	# print(count)

	# return render(request, template_name, {})