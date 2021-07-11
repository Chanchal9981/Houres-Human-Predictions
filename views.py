from django.shortcuts import render,redirect
from.models import *



#jetbrains://pycharm/navigate/reference?project=untitled21&path=myproject/MEDIA
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import os
from PIL import Image
from django.core.files.storage import FileSystemStorage
import numpy as np
model=load_model("horse_human_prediction1.h5")
def pred_horse_human(horse_or_human):
    test_img=load_img(horse_or_human,target_size=(150,150))
    test_img=img_to_array(test_img)/255
    test_img=np.expand_dims(test_img,axis=0)
    result=model.predict(test_img).round(3)
    print(result)
    pred=np.argmax(result)
    if pred==0:
        return "Horses"
    else:
        return "Human"





from django.core.files.storage import FileSystemStorage
def home(request):
    if request.method=="POST":
        fileobj=request.FILES["image"]
        fs=FileSystemStorage()
        filepathname=fs.save(fileobj.name,fileobj)
        filepathname=fs.url(filepathname)
        testimg='.'+filepathname
        preds = pred_horse_human(horse_or_human=testimg)
        return render(request,'home.html',{"pred":preds,"user_img":filepathname})
    return render(request,'home.html')




