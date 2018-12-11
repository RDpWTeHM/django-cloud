from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect
import os
import sys

import json


class BasicIndex(object):
    title = "httpserver-cloud | basic"
    h1 = "Upload File"


def index(request):
    basicindex = BasicIndex()

    HOME = os.environ.get("HOME", None)
    last_dir = HOME

    files = os.listdir(last_dir)
    dirs = [file for file in files if os.path.isdir(os.path.join(last_dir, file))]

    # don't display hidden folder
    dirs = [dir for dir in dirs if not dir.startswith(".")]
    return render(request, "basic/index.html",
                  {"basicindex": basicindex,
                   'HOME': HOME,
                   'dirs': dirs,
                   })


def select_dir(request):
    if request.method == "POST":
        last_path = request.POST["last_path"]
        selected_folder = request.POST["folder"]

        last_path = os.path.join(last_path, selected_folder)
        files = os.listdir(last_path)
        dirs = [file for file in files if os.path.isdir(os.path.join(last_path, file))]
        # if __debug__:
        #     print(dirs, file=sys.stderr)
        return HttpResponse(json.dumps({'sub_dirs': dirs}))
    else:
        redirect("/basic/")


def upload(request):
    if request.method == "POST":
        upload_file = request.FILES.get('upload_file', None)
        if not upload_file:
            return redirect("/basic/")  # home page should with error

        _path = request.POST["cloud_path"]
        # save_file_path = open(os.path.join("E:\\tmp", upload_file.name), 'wb+')
        save_file_path = open(os.path.join(_path, upload_file.name), 'wb+')

        for chunk in upload_file.chunks():
            save_file_path.write(chunk)
        save_file_path.close()
        return HttpResponse("<h1>Upload finished!</h1>")

    else:
        return redirect("/basic/")
