from django.shortcuts import render
from django.http import HttpResponse
import pytube
from pytube import YouTube  
import os
# Create your views here.

def index(request):
    return render(request,'index.html')

def download(request):
    if request.method =='POST':
        url = request.POST['url']
        print('url:',url)
        obj = YouTube(url)
        thumbnail_url = obj.thumbnail_url
        title = obj.title
        desc = obj.description
        view = obj.views
        rating = obj.rating
        res = render(request,'index.html',{"title":title,"thumbnail":thumbnail_url,"url":url})
        return res
    else:
        res = render(request,'index.html')
        return res


def startdownloding(request):
	homedir = os.path.expanduser("~")
	dirs = homedir+'/Downloads'
	if request.method == 'POST':
		formatRadio = request.POST['formatRadio']
		if formatRadio != "audio":
			qualityRadio = request.POST['qualityRadio']
		video_url_d = request.POST['video_url_d']
		print(video_url_d)
		# print(qualityRadio)
		yt = YouTube(video_url_d)
		# print(yt)
		# print("Downloading start ....")
		if formatRadio == "audio":
			yt.streams.filter(type=formatRadio).last().download(dirs)
		else:
			yt.streams.filter(type = formatRadio,resolution=qualityRadio).first().download(dirs)
		# print("Downloding completed")
	res = render(request,'index.html',{"msg":"downloading completed"})
	return res
