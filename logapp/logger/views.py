#import the libraries

from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage, default_storage
import os, shutil
import mimetypes
from django.template.defaultfilters import upper
from .log_merger import merge
from .support_bundle import zip_logs
from .ServiceStatusCheck import getServiceStatus
import os
import logging

#base path where the files gets stored
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
output_file_path = "media/output.txt"
os.makedirs("logs/msg/", exist_ok=True)
logging.basicConfig(filename='logs/msg/view_log.txt', format='%(asctime)s -[%(pathname)s - %(lineno)d] - %(levelname)-8s %(message)s', filemode= 'a')
logs = logging.getLogger()
logs.setLevel(logging.INFO)

def index(request):
    #if the method is post
    context ={}
    if request.method == "POST":
        if os.path.exists('media'):
            #delete the media folder if exists
            shutil.rmtree("media")
        #create new media folder
        os.makedirs("media")
        #iterate through the files
        fs = FileSystemStorage()
        with open(output_file_path, 'w') as fp:
            pass
        for file in request.FILES.getlist('files'):
            fs.save(file.name, file)
            merge(os.path.join('media', file.name))
            #merge(pathA, pathB)
        context['url'] = fs.url("output.txt")
        context["notification"] = "SucessFully merged Log Files <br> No.of Log Files Uploaded:{}".format(len(request.FILES.getlist('files')))
    #return the index.html page
    return render(request, 'index.html', context)

#function to print the logs of the log file
def view_log(request):
	os.makedirs("media/view/", exist_ok=True)
	context = {}
	if request.method == 'POST':
		logs.info("view the log file")
		#get the log file from the request
		file = request.FILES['log_file']
		fs = FileSystemStorage()
		if os.path.exists("./media/view/view.txt"):
			os.remove("./media/view/view.txt")
		fs.save("view/view.txt", file)
		context["log"] = ''
		context["InfoCount"] = 0
		context["WarningCount"] = 0
		for chunk in file:
			content = chunk.decode("utf-8")
			context["log"] += content
			if("INFO" in content):
				 context["InfoCount"] +=1
			elif("WARNING" in content):
				 context["WarningCount"] +=1
				 
		context["InfoCount"] = str(context["InfoCount"])
		context["WarningCount"] = str(context["WarningCount"])
		return render(request, 'index.html', context=context)
	#return the index.html page
	return render(request, 'index.html')

def filter(request):
	logs.info("filter is shown")
	context = {}
	if request.method =='GET':
		filter_word = request.GET.get('filter_word')
		filter_word = upper(filter_word)
		context["log"] = ''
		content = ""
		context["InfoCount"] = 0
		context["WarningCount"] = 0
		with open("./media/view/view.txt") as f:
			for line in f:
				if(filter_word in line):
					context["log"] += line
					if("INFO" in line):
						context["InfoCount"] +=1
					elif("WARNING" in line):
						context["WarningCount"] +=1
		context["InfoCount"] = str(context["InfoCount"])
		context["WarningCount"] = str(context["WarningCount"])
		#return the index.html page
		return render(request, 'index.html', context=context)
	#return the index.html page
	return render(request, 'index.html')

def search(request):
    context = {}
    if request.method =='GET':
        search_word = request.GET.get('search_word')
        context["log"] = ''
        content = ""
        context["InfoCount"] = 0
        context["WarningCount"] = 0
        with open("./media/view/view.txt") as f:
            for line in f:
                if("INFO" in line):
                    context["InfoCount"] +=1
                elif("WARNING" in line):
                    context["WarningCount"] +=1
                if(search_word in line):
                    context["log"] += "<mark>" + line +"</mark>"
                else:
                    context["log"] += line

        context["InfoCount"] = str(context["InfoCount"])
        context["WarningCount"] = str(context["WarningCount"])
        #return the index.html page
        return render(request, 'index.html', context=context)
    #return the index.html page
    return render(request, 'index.html')

def view_support_bundle(request):
    context = {}
    context["log"] = ""
    context["notification"]= ""
    support_bundle_list = os.listdir("./support bundle")
    if(len(support_bundle_list) != 0):
        for item in support_bundle_list[::-1]:
            context["log"] += item
            context["log"] += " <br>"
    else:
        context["notification"] += "No support Bundle available"
    return render(request, 'index.html', context=context)

def generate_support_bundle(request):
    context = {}
    zip_logs()
    context["notification"] = "Generated New Support Bundle"
    return render(request, 'index.html', context=context)

def download_file(request):
	logs.info("Downloading the current file")
	# fill these variables with real values
	fl_path = 'media/output.txt'
	filename = 'output.txt'
	fl = open(fl_path, 'r')
	mime_type, _ = mimetypes.guess_type(fl_path)
	response = HttpResponse(fl, content_type=mime_type)
	response['Content-Disposition'] = "attachment; filename=%s" % filename
	return response

def check_service_status(request):
    context = {}
    os.system('net start FMService')
    context['status'] = getServiceStatus('FMService')
    return render(request, 'index.html', context=context)