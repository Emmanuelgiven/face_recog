from django.shortcuts import render
from django.http import HttpResponse
import subprocess
import MySQLdb



def index(request):
    db = MySQLdb.connect(host="localhost", user="root", passwd="", db="facial")
    cursor = db.cursor()
    sql = "SELECT * FROM attend"
    cursor.execute(sql)
    rows = cursor.fetchall()
    db.close()
    return render(request, 'index.html', {'rows': rows})

def attend(request):
    return render(request, 'attend.html') 

def run_recognition(request):
    subprocess.run(['python', 'C:/xampp/htdocs/face_recog/recognition.py'])
    return HttpResponse('Done')