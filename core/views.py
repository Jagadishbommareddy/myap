# from django.shortcuts import render

# from django.contrib.auth import authenticate
from django.contrib.auth.views import LoginView, LogoutView
from .forms import *
# from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from core.forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse
from .serializers import *
from .models import *
import json
from rest_framework.response import Response
from rest_framework.pagination import (LimitOffsetPagination,PageNumberPagination)
from rest_framework.pagination import PageNumberPagination
from django.views.decorators.csrf import csrf_exempt
from .pagination import *
import openpyxl
class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 5

#@login_required
def home(request):
    return render(request, 'home.html')
#
#
# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = SignUpForm()
#     return render(request, 'signup.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            print("form is valid")
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            # #return redirect('')
            return render(request, 'signupcomp.html', {'form': form})
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

# def getdata(request):
#     usr = User.objects.all()
#     # for us in usr:
#     #     print (us.first_name)
#     # for data in usr:
#     #     print (data.first_name)
#     x = [data.first_name for data in usr]
#     print (x[0])
# def pagination(request):
#     use = UserObj.objects.all()
#     print (use)
#     #usr = UserObjSerializer(use, many=True).data
#     paginator = Paginator(use, 2)
#     #print (paginator)
#     usr = UserObjSerializer(instance={'paginator': paginator},many=True)
#     #page = request.POST.get('page')
#     # posts = paginator.get_page(page)
#     # print (posts)
#     return Response({'response':usr,'status':"success"})

def get_offse(request):
    PAGE_LIMIT = 20
    if request.method == 'GET':
        offset = request.GET.get('offset')
        print (offset)
        print (type(offset))
        #offset = 10
        limit = int(offset)+PAGE_LIMIT
        print (limit)
    return offset,limit
@csrf_exempt

# ## pagination is working
# def pagination(request):
#     #data = json.loads(request.body)
#     #pag = SystemConfig.objects.get(parameter="pagination").value
#     #print (pag)
#     ls = request.GET.get('page')
#     print (ls)
#     print (type(ls))
#     if request.GET.get('page') != "" and request.GET.get('page') != None:
#         ls = request.GET.get('page')
#         use = UserObj.objects.all()[:int(ls)]
#     else:
#         use = UserObj.objects.all()
#     #lis = []
#     #listingobj = {}
#     usr = UserObjSerializer(use, many=True)
#     #lis.append(listingobj)
#     #offset, limit = get_offse(usr.data)
#     #pagination_class = LargeResultsSetPagination
#     return JsonResponse({'response': usr.data, 'status': "success"})


#### write custome data
def pagination(request):

    ls = request.GET.get('page')
    user = UserObj.objects.all()[:int(ls)]
    list = []
    for us in user:
        lis = {}
        lis['id']= us.id
        lis['text_data'] = us.text_data
        list.append(lis)
    return JsonResponse({'response': list, 'status': "success"})
    # if request.GET.get('page') != "" and request.GET.get('page') != None:
    #     ls = request.GET.get('page')
    #     use = UserObj.objects.all()[:int(ls)]
    # else:
    #     use = UserObj.objects.all()
    # usr = UserObjSerializer(use, many=True)
    # return JsonResponse({'response': usr.data, 'status': "success"})

@csrf_exempt
def upload_excel(request):
    excel_file = request.FILES["excel_file"]
    print (excel_file)
    # you may put validations here to check extension or file size

    wb = openpyxl.load_workbook(excel_file)
    print (wb)

    # getting a particular sheet by name out of many sheets
    # worksheet = wb["Sheet1"]
    # print(worksheet)

    excel_data = list()
    print (excel_data)
    # iterating over the rows and
    # getting value from each cell in row
    # for row in worksheet.iter_rows():
    #     row_data = list()
    #     for cell in row:
    #         row_data.append(str(cell.value))
    #     excel_data.append(row_data)
    return JsonResponse({'Status':'Sucess'})
import uuid
@csrf_exempt
def upload_pdf(request):
    user_file = request.FILES
    #name = request.POST.get("name")
    #file = request.FILES['file'] ### single file upload
    for f in user_file.getlist('file'):  #### multiple file uploading
        new_name = str(uuid.uuid4().hex)
        b = str(f).split(".")
        ext = b[len(b) - 1]
        new_name = new_name + "." + ext
        #path = "/home/karthick/Desktop" + new_name
        new_media = PdfUpload.objects.create(name=new_name, original_name=str(f),file=f)
        new_media.save()
    return JsonResponse({'Status': 'Sucess'})