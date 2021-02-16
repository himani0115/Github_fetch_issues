from django.shortcuts import render
import requests
import json
import pandas as pd
# Create your views here.


def home(request):
    return render(request, 'home.html')

def github_issues(request):
    if request.method == "POST":
        endpoint= request.POST['endpoint']
        token = request.POST['auth_token']
        owner = request.POST['username']
        repo = request.POST['repo_name']
        file_name = request.POST['file_name']
  
    query_url = f"https://api.github.com/repos/{owner}/{repo}/" + endpoint
    params = {
        "state": "open",
    }
    headers = {'Authorization': f'{token}'}

    responce = requests.get(query_url, headers=headers, params=params)
    data = responce.json()
    df = pd.DataFrame.from_dict(data)
    if file_name:
        df.to_csv(file_name+'.csv')
    context = {
        'data': data,
    }
    return render(request, 'github_issues.html', context)
