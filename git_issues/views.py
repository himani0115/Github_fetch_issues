from django.shortcuts import render
import requests
import json
# Create your views here.

def home(request):
    return render(request, 'home.html')

def github_issues(request):
    if request.method == "POST":
        token= request.POST['auth_token']
        owner = request.POST['username']
        repo=request.POST['repo_name']
    query_url = f"https://api.github.com/repos/{owner}/{repo}/issues"
    params = {
        "state": "open",
        }
    headers = {'Authorization': f'{token}'}

    responce = requests.get(query_url, headers=headers, params=params)
    data= responce.json()
    context = {
        'data': data,
    }
    return render(request,'github_issues.html',context)