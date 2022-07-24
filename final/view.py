import string
import urllib
from datetime import datetime,date
import random
import urllib.request
from urllib import request
import monthdelta as monthdelta
from django.contrib.sessions.models import Session
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse, HttpResponse
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
import cv2
import numpy as np
import logging
import matplotlib.pyplot as plt
# from . import cascade as casc
from PIL import Image
from time import time
from sklearn.decomposition import PCA
from final.models import LoginModel, roleModel, EmployeeModelACM, PrivToUserModelACM, PrivToRoleModelACM, \
    privilegeModelACM, privComponentModelACM, cityModel, stateModel, LanguageModel, structureModel, feeModel, \
    batchModel, inquiryModel, useradminModel, registrationModel, TrainigTypedModel, admin_inquiryModel
# -------------digitalcampus no mail id and password----------
#     id=digitalcampus49@gmail.com
#     pass=digital@710
# ------------======================================----------

# -------------mail mate------------------

# send_mail('Welcome To Jabra-Jabri',
#           'Joyu BHaila Email thi kariyu che aama jate msg banai ne mokaliyo che Django through taro password nathi khabar atyare',
#           'digitalcampus49@gmail.com',
#           ['nishilmakwana123@gmail.com', 'nishilmacwan19@gmail.com'],
#           fail_silently=False)

# =========end mail -------======================================
from final.settings import EMAIL_HOST_USER


def sendsms(mobile,msg):
	user = "silver" # Your authentication key.
	key = "e07bfa50dfXX" # Your authentication key.
	mobile = "+1"+str(mobile) # Multiple mobiles numbers separated by comma.

	message = msg # Your message to send.

	senderid = "SILVER" # Sender ID,While using route4 sender id should be 6 characters long.

	accusage = "1" # Define route

	# Prepare you post parameters

	values = {

				'user' : user,

				'password' : key,

				'mobiles' : mobile,

				'sms' : message,

				'senderid' : senderid,

				'accusage' : accusage

				}
	url = "http://mysms.webpointinfotech.org/sendsms.jsp?" # API URL

	data = urllib.parse.urlencode(values)
	data = data.encode('ascii') # data should be bytes
	req = urllib.request.Request(url, data)
	with urllib.request.urlopen(req) as response:
		the_page = response.read()
		print(the_page)






# ===================index Start ============================
def home(request):
    return render(request,'admin/home.html')

def dashboard(request):
    batch = batchModel.objects.all()
    reg = registrationModel.objects.all()
    total = inquiryModel.objects.all().count()
    c = inquiryModel.objects.filter(status="pending").count()
    t = inquiryModel.objects.filter(status='confirm').count()
    y = inquiryModel.objects.filter(status='cancelled').count()
    complete = registrationModel.objects.filter(status='closed').count()
    data = {
        'inquiry': c,
        'ddd': t,
        'yyy': y,
        'fff': total,
        'reg': reg,
        'batch': batch,
        'complete': complete
    }
    return render(request,'admin/dashboard.html',data)

def sendsms(mobile,msg):
	user = "silver" # Your authentication key.
	key = "e07bfa50dfXX" # Your authentication key.
	mobile = "+91"+str(mobile) # Multiple mobiles numbers separated by comma.

	message = msg # Your message to send.

	senderid = "SILVER" # Sender ID,While using route4 sender id should be 6 characters long.

	accusage = "1" # Define route

	# Prepare you post parameters

	values = {

				'user' : user,

				'password' : key,

				'mobiles' : mobile,

				'sms' : message,

				'senderid' : senderid,

				'accusage' : accusage

				}

	url = "http://mysms.webpointinfotech.org/sendsms.jsp?" # API URL

	data = urllib.parse.urlencode(values)
	data = data.encode('ascii') # data should be bytes
	req = urllib.request.Request(url, data)
	with urllib.request.urlopen(req) as response:
		the_page = response.read()
		print(the_page)


# ===================index End ============================

# ===============acm thi login -------------------------

def insetacmdata(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            login = EmployeeModelACM.objects.get(fullname=email, password=password)
        except EmployeeModelACM.DoesNotExist:
            login = None
        if login == None:
            return render(request, 'admin/login.html')
        else:
            request.session['username'] = login.fullname
            request.session['role'] = login.role_id.role
            request.session['userphoto'] = login.photo
            # sendsms(+login.mobnum, "Hello " + login.fullname + " Welcome To Digital Campus!!")
            total = inquiryModel.objects.all().count()
            inq = inquiryModel.objects.all()
            inqdict = {
                'inqlist': inq,
                'res': total
            }
            emp = EmployeeModelACM.objects.get(id=login.id)
            io = PrivToUserModelACM.objects.get(empId=emp)
            privilage = io.privId
            listpri = privilage.split(',')

            liuser = []
            for i in range(len(listpri)):
                templist = []
                empm = privilegeModelACM.objects.get(id=listpri[i])
                ioo = privComponentModelACM.objects.get(privId=empm)
                templist.append(ioo.privId.privname)
                templist.append(ioo.privId.fontcode)
                kkk = ioo.pCompName.split(',')
                ppp = ioo.pCompLink.split(',')
                iii = []
                uuu = []
                for o in range(len(kkk)):
                    iii.append(kkk[o])
                    uuu.append(ppp[o])

                templist.append(iii)
                templist.append(uuu)
                liuser.append(templist)
            request.session['userlist'] = liuser

            return render(request, 'admin/acmhome.html',inqdict)
    else:
        return render(request, 'admin/login.html')

def acmhome(request):
    return request(request,'admin/acmhome.html')


# ======================acm login end --------------------

# ========================face Data============================
def Create_dataset(user_id):
    userId = user_id
    print(cv2.__version__)
    # Detect face
    # Creating a cascade image classifier
    faceDetect = cv2.CascadeClassifier('ml\haarcascade_frontalface_default.xml')
    # camture images from the webcam and process and detect the face
    # takes video capture id, for webcam most of the time its 0.
    cam = cv2.VideoCapture(0)

    # Our identifier
    # We will put the id here and we will store the id with a face, so that later we can identify whose face it is
    id = userId
    # Our dataset naming counter
    sampleNum = 0
    # Capturing the faces one by one and detect the faces and showing it on the window
    while (True):
        # Capturing the image
        # cam.read will return the status variable and the captured colored image
        ret, img = cam.read()
        # the returned img is a colored image but for the classifier to work we need a greyscale image
        # to convert
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # To store the faces
        # This will detect all the images in the current frame, and it will return the coordinates of the faces
        # Takes in image and some other parameter for accurate result
        faces = faceDetect.detectMultiScale(gray, 1.3, 5)
        # In above 'faces' variable there can be multiple faces so we have to get each and every face and draw a rectangle around it.
        for (x, y, w, h) in faces:
            # Whenever the program captures the face, we will write that is a folder
            # Before capturing the face, we need to tell the script whose face it is
            # For that we will need an identifier, here we call it id
            # So now we captured a face, we need to write it in a file
            sampleNum = sampleNum + 1
            # Saving the image dataset, but only the face part, cropping the rest
            cv2.imwrite('./ml/dataset/user.' + str(id) + '.' + str(sampleNum) + '.jpg', gray[y:y + h, x:x + w])
            # @params the initial point of the rectangle will be x,y and
            # @params end point will be x+width and y+height
            # @params along with color of the rectangle
            # @params thickness of the rectangle
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # Before continuing to the next loop, I want to give it a little pause
            # waitKey of 100 millisecond
            cv2.waitKey(250)

        # Showing the image in another window
        # Creates a window with window name "Face" and with the image img
        cv2.imshow("Face", img)
        # Before closing it we need to give a wait command, otherwise the open cv wont work
        # @params with the millisecond of delay 1
        cv2.waitKey(1)
        # To get out of the loop
        if (sampleNum > 35):
            break
    # releasing the cam
    cam.release()
    # destroying all the windows
    cv2.destroyAllWindows()

    return redirect('/')


def Trainers(request):
    '''
        In trainer.py we have to get all the samples from the dataset folder,
        for the trainer to recognize which id number is for which face.

        for that we need to extract all the relative path
        i.e. dataset/user.1.1.jpg, dataset/user.1.2.jpg, dataset/user.1.3.jpg
        for this python has a library called os
    '''
    import os
    from PIL import Image

    # Creating a recognizer to train
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    # recognizer = cv2.face_LBPHFaceRecognizer.create()

    # Path of the samples
    path = 'ml\dataset'

    # To get all the images, we need corresponing id
    def getImagesWithID(path):
        # create a list for the path for all the images that is available in the folder
        # from the path(dataset folder) this is listing all the directories and it is fetching the directories from each and every pictures
        # And putting them in 'f' and join method is appending the f(file name) to the path with the '/'
        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]  # concatinate the path with the image name
        # print imagePaths

        # Now, we loop all the images and store that userid and the face with different image list
        faces = []
        Ids = []
        for imagePath in imagePaths:
            # First we have to open the image then we have to convert it into numpy array
            faceImg = Image.open(imagePath).convert('L')  # convert it to grayscale
            # converting the PIL image to numpy array
            # @params takes image and convertion format
            faceNp = np.array(faceImg, 'uint8')
            # Now we need to get the user id, which we can get from the name of the picture
            # for this we have to slit the path() i.e dataset/user.1.7.jpg with path splitter and then get the second part only i.e. user.1.7.jpg
            # Then we split the second part with . splitter
            # Initially in string format so hance have to convert into int format
            ID = int(os.path.split(imagePath)[-1].split('.')[
                         1])  # -1 so that it will count from backwards and slipt the second index of the '.' Hence id

            # Images
            faces.append(faceNp)
            # Label
            Ids.append(ID)
            # print ID
            cv2.imshow("training", faceNp)
            cv2.waitKey(10)
        return np.array(Ids), np.array(faces)

    # Fetching ids and faces
    ids, faces = getImagesWithID(path)

    # Training the recognizer
    # For that we need face samples and corresponding labels
    recognizer.train(faces, ids)

    # Save the recogzier state so that we can access it later
    recognizer.save('./ml/recognizer/trainingData.yml')
    cv2.destroyAllWindows()

    return redirect('/')


def Detect(request):
    Trainers(request)
    faceDetect = cv2.CascadeClassifier('./ml/haarcascade_frontalface_default.xml')

    cam = cv2.VideoCapture(0)
    # creating recognizer
    rec = cv2.face.LBPHFaceRecognizer_create()
    # loading the training data
    rec.read('./ml/recognizer/trainingData.yml')
    getId = 0
    font = cv2.FONT_HERSHEY_SIMPLEX
    userId = 0
    while (True):
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceDetect.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

            getId, conf = rec.predict(gray[y:y + h, x:x + w])  # This will predict the id of the face

            # print conf;
            if conf < 35:
                userId = getId
                cv2.putText(img, "Detected", (x, y + h), font, 2, (0, 255, 0), 2)

            else:
                cv2.putText(img, "Unknown", (x, y + h), font, 2, (0, 0, 255), 2)

            # Printing that number below the face
            # @Prams cam image, id, location,font style, color, stroke

        cv2.imshow("Face", img)
        if (cv2.waitKey(1) == ord('q')):
            break
        elif (userId != 0):
            cv2.waitKey(1000)
            cam.release()
            cv2.destroyAllWindows()

            request.session['user_id'] = userId
            user = LoginModel.objects.get(id=userId)
            request.session['email'] = user.email
            request.session['password'] = user.password
            # products = list(Basic_product_form.objects.all())
            # update_status_discount()
            # cart_all = list(Add_to_cart.objects.all().filter(user_id=request.session['user_id']))
            # sale_products = list(Basic_product_form.objects.all().filter(special_price_id__sale_status=1))

            # product = {
            #     "products": products,
            #     "sale_products": sale_products,
            #     # "cart_all": cart_all,
            #     # "total": total_amount(request.session['user_id']),
            #     # "items": Count(request.session['user_id'])
            # }

            return render(request, 'admin/home.html')
    cam.release()
    cv2.destroyAllWindows()
    return redirect('/')


# =================face ==========================

# ===========================login start================================================
def login(request):
    return render(request,'admin/login.html')

def lockscreen(request):
    return render(request, 'admin/lockscreen.html')

def logininsert(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    try:
        re = LoginModel.objects.get(email=email)
    except LoginModel.DoesNotExist:
        re = None
    if (re != None):
        try:
            rw = LoginModel.objects.get(email=email, password=password)
        except LoginModel.DoesNotExist:
            rw = None
        if (rw != None):

            # sendsms(+ rw.pnum, "Hello " + rw.fullname + " Welcome To Digital Campus!!")
            request.session['lid'] = rw.id
            request.session['fullname'] = rw.fullname
            request.session['photos'] = rw.photos
            request.session['email'] = rw.email
            # send_mail('django testing email',
            #           'this is  email for in testing',
            #           'gohila71098@gmail.com',
            #           ['gohila71098@gmail.com'],
            #           fail_silently=False)


            batch = batchModel.objects.all()
            reg = registrationModel.objects.all()
            inq = inquiryModel.objects.all()
            total = inquiryModel.objects.all().count()
            c = inquiryModel.objects.filter(status="pending").count()
            pending = inquiryModel.objects.filter(status="pending")
            t = inquiryModel.objects.filter(status='confirm').count()
            y = inquiryModel.objects.filter(status='cancelled').count()

            complete = registrationModel.objects.filter(status='closed').count()
            data = {
                'pen':pending,
                'inquiry': c,
                'ddd': t,
                'yyy': y,
                'fff': total,
                'reg': reg,
                'batch': batch,
                'complete': complete,
                'inqlist': inq,
            }

            return render(request, 'admin/dashboard.html',data)
        else:
            da = {
                'msg': 'WRONG PASSWORD!'
            }
            return render(request, 'admin/login.html', da)
    else:
        da = {
            'msg': 'WRONG EMAILID!'
        }
        return render(request, 'admin/login.html', da)

def logout(request):
    Session.objects.all().delete()
    return render(request, 'admin/login.html')

def lockscreeninsert(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    try:
        re = LoginModel.objects.get(email=email)
    except LoginModel.DoesNotExist:
        re = None
    if (re != None):
        try:
            rw = LoginModel.objects.get(email=email, password=password)
        except LoginModel.DoesNotExist:
            rw = None
        if (rw != None):

            request.session['lid'] = rw.id
            request.session['fullname'] = rw.fullname
            request.session['email'] = rw.email
            request.session['password'] = rw.password
            request.session['photos'] = rw.photos
            # sendsms(+ rw.pnum, "Hello " + rw.fullname + " Welcome To Digital Campus!!")

            batch = batchModel.objects.all()
            reg = registrationModel.objects.all()
            inq = inquiryModel.objects.all()
            total = inquiryModel.objects.all().count()
            c = inquiryModel.objects.filter(status="pending").count()
            pending = inquiryModel.objects.filter(status="pending")
            t = inquiryModel.objects.filter(status='confirm').count()
            y = inquiryModel.objects.filter(status='cancelled').count()

            complete = registrationModel.objects.filter(status='closed').count()
            data = {
                'pen':pending,
                'inquiry': c,
                'ddd': t,
                'yyy': y,
                'fff': total,
                'reg': reg,
                'batch': batch,
                'complete': complete,
                'inqlist': inq,
            }

            return render(request, 'admin/dashboard.html',data)
        else:
            da = {
                'msg': 'WRONG PASSWORD!'
            }
            return render(request,'admin/lockscreen.html')
    else:
        da = {
            'msg': 'WRONG EMAILID!'
        }
        return render(request,'admin/lockscreen.html')



def crete_new_user(request):
    return render(request,'admin/Create_new_user.html')

def newuserwithoutface(request):
    photos = request.FILES['photos']
    fs = FileSystemStorage()
    photos = fs.save(photos.name, photos)
    fullname = request.POST.get('fullname')
    email = request.POST.get('email')
    password = request.POST.get('password')
    confirmpassword = request.POST.get('confirmpassword')
    r = LoginModel()
    r.photos = photos
    r.fullname = fullname
    r.email = email
    r.confirmpassword = confirmpassword
    r.password = password
    r.save()
    Create_dataset(r.id)
    da = {
        'msg': 'successfully created account!'
    }
    return render(request, 'admin/login.html', da)

# =============================================================================================================

# def user_registration(request):
#     if request.method == 'POST':
#         obj = User_registration()
#         obj.name = request.POST.get('name')
#         obj.email = request.POST.get('email')
#         obj.phone_no = request.POST.get('phone_no')
#         # a = request.POST.get('phone_no')
#         obj.password = request.POST.get('password1')
#         obj.age = request.POST.get('age')
#         obj.gender = request.POST.get('gender')
#         obj.save()
#         Create_dataset(obj.id)
#         return render(request, 'admin/newuserface.html')
#
#
# def newuserface(request):
#     return render(request, 'admin/newuserface.html')
#
# ==========================login end==============================================

# =============================== ACM START =====================================

def acmrole(request):
    data = roleModel.objects.all()
    da = {
        'result': data,
    }
    return render(request, 'admin/acm/ACM_Role.html', da)

def addacmrole(request):
    if request.method == 'POST':
        rname = request.POST.get('role')
        roleimag = request.FILES['roleimage']
        fs = FileSystemStorage()
        roleimage = fs.save(roleimag.name, roleimag)
        rmodel = roleModel()
        rmodel.role = rname
        rmodel.roleimage=roleimage
        rmodel.save()
    return redirect('/acmrole/')

def acmroledelete(request):
    r = request.GET.get('id')
    obj = roleModel.objects.get(id=r)
    obj.delete()
    return redirect('/acmrole/')

def PrivilegeACM(request):
    privilege = privilegeModelACM.objects.all()
    privdict = {
        'results': privilege,
    }
    return render(request, 'admin/acm/PrivilegeACM.html', privdict)

def addPrivilegeACM(request):
    if request.method == 'POST':
        pname = request.POST.get('privname')
        fcode = request.POST.get('fontcode')
        pmodel = privilegeModelACM()
        pmodel.privname = pname
        pmodel.fontcode = fcode
        pmodel.save()
    return redirect('/PrivilegeACM/')

def privelegedelet(request):
    r = request.GET.get('id')
    obj = privilegeModelACM.objects.get(id=r)
    obj.delete()
    return redirect('/PrivilegeACM/')

def PrivComponentACM(request):
    pdata = privilegeModelACM.objects.all()
    pdict = {
        'plist': pdata,

    }
    return render(request, 'admin/acm/PrivComponentACM.html', pdict)


def addPrivComponentACM(request):
    if request.method == 'POST':
        post = privComponentModelACM()
        pid = request.POST.get('privid')
        pmodel = privilegeModelACM()
        pmodel.id = pid
        post.privId = pmodel

        cname = request.POST.getlist('privCompName[]')
        post.pCompName = ",".join(cname)

        clink = request.POST.getlist('privCompLink[]')
        post.pCompLink = ",".join(clink)

        post.save()
    return render(request, 'admin/acm/PrivComponentACM.html')

def state(request):
    state = stateModel.objects.all()
    data = {
        'result': state
    }
    return render(request, 'admin/acm/state.html', data)


def addState(request):
    if request.method == 'POST':
        scode = request.POST.get('statecode')
        sname = request.POST.get('statename')
        smodel = stateModel()
        smodel.statecode = scode
        smodel.statename = sname
        smodel.save()
    return redirect('/state/')

def statedel(request):
    r = request.GET.get('Id')
    obj = stateModel.objects.get(id=r)
    obj.delete()
    return redirect('/state/')


def city(request):
    sdata = stateModel.objects.all()
    city = cityModel.objects.all()
    sdict = {
        'slist': sdata,
        'res': city
    }
    return render(request, 'admin/acm/city.html', sdict)


def addCity(request):
    if request.method == 'POST':
        stid = request.POST.get('sid')
        cname = request.POST.get('cityname')
        cmodel = cityModel()
        smodel = stateModel()
        cmodel.cityname = cname
        smodel.id = stid
        cmodel.stateId = smodel
        cmodel.save()
    return redirect('/city/')

def citydel(request):
    r = request.GET.get('Id')
    obj = cityModel.objects.get(id=r)
    obj.delete()
    return redirect('/city/')

def employee(request):
    state = stateModel.objects.all()
    city = cityModel.objects.all()

    role = roleModel.objects.all()
    # company = CompanyModelACM.objects.all()
    employeedict = {
        'role': role,
        # 'company': company,
        'state': state,
        'city': city,

    }
    return render(request, 'admin/acm/empAcm.html', employeedict)



def addEmpACM(request):
    if request.method == 'POST':
        empid = request.POST.get('empid')  # text
        fullname = request.POST.get('fullname')  # text
        password = request.POST.get('password')  # text
        roleid = request.POST.get('roleid')  # int   roleid 121
        # companyid = request.POST.get('companyid')  # text
        bloodgroup = request.POST.get('bloodgroup')  # text
        gender = request.POST.get('gender')  # text
        mstatus = request.POST.get('mstatus')  # text
        mobnum = request.POST.get('mobnum')  # bigint
        nativenum = request.POST.get('nativenum')  # bigint
        email = request.POST.get('email')  # text
        dob = request.POST.get('dob')  # text datetime
        paddress = request.POST.get('paddress')  # textarea
        taddress = request.POST.get('taddress')  # textarea
        stateid = request.POST.get('stateid')  # int stateid 121
        cityid = request.POST.get('cityid')  # int cityid 121
        # areaid = request.POST.get('areaid')  # int areaid 121
        zipcode = request.POST.get('zipcode')  # int
        bsalary = request.POST.get('bsalary')  # bigint
        tax = request.POST.get('tax')  # text
        taxpercentage = request.POST.get('taxpercentage')  # text
        fsalary = request.POST.get('fsalary')  # bigin
        asignleave = request.POST.get('asignleave')  # int
        cutleave = request.POST.get('cutleave')  # int
        cuthalfleave = request.POST.get('cuthalfleave')  # int
        comingtime = request.POST.get('comingtime')  # text datetime
        leavingtime = request.POST.get('leavingtime')  # text datetime
        fathername = request.POST.get('fathername')  # text
        mothername = request.POST.get('mothername')  # text
        fcontact = request.POST.get('fcontact')  # bigint
        mcontact = request.POST.get('mcontact')  # bigint

        adhar = request.FILES['adharcard']
        fs = FileSystemStorage()
        adharcard = fs.save(adhar.name, adhar)

        pan = request.FILES['pancard']  # bigint img
        fs = FileSystemStorage()
        pancard = fs.save(pan.name, pan)

        photo = request.FILES['photo']  # bigint img
        fs = FileSystemStorage()
        photo = fs.save(photo.name, photo)

        bankname = request.POST.get('bankname')  # text
        branchname = request.POST.get('branchname')  # text
        accnum = request.POST.get('accnum')  # bigint
        acctype = request.POST.get('acctype')  # text
        pannumber = request.POST.get('pannumber')  # bigint notpic
        chqnumber = request.POST.get('chqnumber')  # bigint notpic
        codeifsc = request.POST.get('codeifsc')  # bigint
        codemicr = request.POST.get('codemicr')  # bigint
        emp = EmployeeModelACM()
        role = roleModel()
        # company = CompanyModelACM()
        state = stateModel()
        city = cityModel()
        # area = areaModel()

        # Add Role ID to Employee
        role.id = roleid
        emp.role_id = role
        # Add Company ID to Employee

        # company.id = companyid
        # emp.company_id = company

        # Add State ID to Employee

        state.id = stateid
        emp.state_id = state

        # Add City ID to Employee

        city.id = cityid
        emp.city_id = city

        # Add area ID to Employee

        # area.id = areaid
        # emp.area_id = area

        # Add split Workdays into employee

        workdays = request.POST.getlist('workdays[]')
        emp.workdays = ",".join(workdays)

        emp.empid = empid
        emp.fullname = fullname
        emp.password = password
        emp.bloodgroup = bloodgroup
        emp.gender = gender
        emp.mstatus = mstatus
        emp.mobnum = mobnum
        emp.nativenum = nativenum
        emp.email = email
        emp.dob = dob
        emp.paddress = paddress
        emp.taddress = taddress
        emp.zipcode = zipcode
        emp.bsalary = bsalary
        emp.tax = tax
        emp.taxpercentage = taxpercentage
        emp.fsalary = fsalary
        emp.asignleave = asignleave
        emp.cutleave = cutleave
        emp.cuthalfleave = cuthalfleave
        emp.comingtime = comingtime
        emp.leavingtime = leavingtime
        emp.fathername = fathername
        emp.mothername = mothername
        emp.fcontact = fcontact
        emp.mcontact = mcontact
        emp.adharcard = adharcard
        emp.pancard = pancard
        emp.photo = photo
        emp.bankname = bankname
        emp.branchname = branchname
        emp.accnum = accnum
        emp.acctype = acctype
        emp.pannumber = pannumber
        emp.chqnumber = chqnumber
        emp.codeifsc = codeifsc
        emp.codemicr = codemicr
        emp.save()
    return redirect('/emp/')


def addPrivComponentACM(request):

    if request.method == 'POST':
        post = privComponentModelACM()

        pid = request.POST.get('privid')
        pmodel = privilegeModelACM()
        pmodel.id = pid
        post.privId = pmodel

        cname = request.POST.getlist('privCompName[]')
        post.pCompName = ",".join(cname)

        clink = request.POST.getlist('privCompLink[]')
        post.pCompLink = ",".join(clink)

        post.save()
    return render(request, 'admin/acm/PrivComponentACM.html')


def PrivToRoleACM(request):
    role = roleModel.objects.all()
    privilege = privilegeModelACM.objects.all()
    PrivToRole = {
        'role': role,
        'privilege': privilege
    }
    return render(request, 'admin/acm/PrivToRoleACM.html', PrivToRole)


def AddprivToroleACM(request):
    if request.method == 'POST':
        rid = request.POST.get('roleid')
        privileges = request.POST.getlist('privileges[]')
        pTOr = PrivToRoleModelACM()
        rmodel = roleModel()
        pmodel = privilegeModelACM()
        # Store Role ID
        rid = request.POST.get('roleid')
        rmodel.id = rid
        pTOr.roleId = rmodel
        # Store multiple Privileges ID
        pid = request.POST.getlist('privileges[]')
        pTOr.privId = ",".join(pid)
        # Save PrivilegeToRole Model
        pTOr.save()
    return redirect('/PrivToRoleACM/')


def PrivToUserACM(request):
    emp = EmployeeModelACM.objects.all()
    role = roleModel.objects.all()
    privilege = privilegeModelACM.objects.all()
    PrivToUser = {
        'role': role,
        'privilege': privilege,
        'emp': emp,
    }
    return render(request, 'admin/acm/PrivToUserACM.html', PrivToUser)


def AddprivTouserACM(request):
    if request.method == 'POST':
        rid = request.POST.get('roleid')
        uid = request.POST.get('userid')
        role = roleModel()
        emp = EmployeeModelACM()
        privUser = PrivToUserModelACM()
        # Store Role ID
        role.id = rid
        privUser.roleId = role
        # Store Employee ID
        emp.id = uid
        privUser.empId = emp
        # Store multiple Privileges ID
        pid = request.POST.getlist('privileges[]')
        privUser.privId = ",".join(pid)
        # Save PrivilegeToRole Model
        privUser.save()
    return redirect('/PrivToUserACM/')

def getpriv(request):
    id = request.POST.get('pid')
    rol = roleModel.objects.get(id=id)
    pr = PrivToRoleModelACM.objects.get(roleId=rol)
    ui = pr.privId.split(',')
    pDict = {
        'Plist': ui,
    }
    return JsonResponse(pDict)


def getuser(request):
    id = request.POST.get('uid')
    rol = roleModel.objects.get(id=id)
    aa = list(EmployeeModelACM.objects.filter(role_id=rol).values())
    da = {
        "list": aa,
    }
    return JsonResponse(da)


def getprivileges(request):
    id = request.POST.get('uid')
    em = EmployeeModelACM.objects.get(id=id)
    pr = PrivToUserModelACM.objects.get(empId=em)
    pid = pr.privId.split(',')
    pdict = {
        'plist': pid,
    }
    return JsonResponse(pdict)

# ================== acm end ==================================


#    ---------------------------------inquiry start ============================
def Pendinginquiry(request):
    data = inquiryModel.objects.filter(status="pending")
    da = {
        'result': data,
    }
    return render(request,'admin/Pendinginquiry.html',da)

def pendelete(request):
    r = request.GET.get('id')
    obj = inquiryModel.objects.get(id=r)
    obj.delete()
    return redirect('/Pendinginquiry/')

def confirm(request):
    a = inquiryModel.objects.filter(status='confirm')
    ab = structureModel.objects.all()
    bb= LanguageModel.objects.all()
    cc=feeModel.objects.all()
    data = {
        'results': a,
        'stru':ab,
        'lang':bb,
        'fee':cc
    }
    return render(request, 'admin/Confirminquiry.html', data)


def confirminquiry(request):
    r = request.GET.get('id')
    obj = inquiryModel.objects.get(id=r)
    obj.status = 'confirm'
    obj.save()
    return redirect('/Confirminquiry/')

def canreg(request):
    r = request.GET.get('id')
    obj = inquiryModel.objects.get(id=r)
    obj.status = 'cancelled'
    obj.save()
    return redirect('/cancel/co')


def cancel(request):
    a = inquiryModel.objects.filter(status='cancelled')
    w = {
        'results': a
    }
    return render(request, 'admin/cancel.html', w)

def confirmdelete(request):
    r = request.GET.get('id')
    obj = inquiryModel.objects.get(id=r)
    obj.delete()
    return redirect('/Confirminquiry/')

def cancledelete(request):
    r = request.GET.get('id')
    obj = inquiryModel.objects.get(id=r)
    obj.delete()
    return redirect('/cancel/')

# -------- registration form of inquiry start ------------------------------
def inquiry_registation_form(request):
    return render(request, 'admin/inquiry_registation_form.html')

def insertregistrations(request):
    # inqid = request.POST.get('inqid')
    stud_id = request.POST.get('stud_id')
    fullname = request.POST.get('fullname')
    pnum = request.POST.get('pnum')
    email = request.POST.get('email')
    reffname = request.POST.get('reffname')
    reffcontact = request.POST.get('reffcontact')
    date1 = request.POST.get('date1')
    # time1 = request.POST.get('time1')
    University = request.POST.get('University')
    Institute = request.POST.get('Institute')
    Semester = request.POST.get('Semester')
    Stream = request.POST.get('Stream')
    structurename = request.POST.get('structurename')
    TrainigTyped = request.POST.get('TrainigTyped')
    lang = request.POST.get('lang')
    price = request.POST.get('price')
    installment = request.POST.get('installment')
    remaining_installment = request.POST.get('installment')

    r = registrationModel()
    # i = inquiryModel()
    # i.id = inqid
    # r.inq_id = i

    r.fullname = fullname
    r.pnum = pnum
    r.email = email
    r.reffname = reffname
    r.reffcontact = reffcontact
    r.date1 = date1
    # r.time1 = time1
    r.University = University
    r.Institute = Institute
    r.Semester = Semester
    r.Stream = Stream
    r.structurename = structureModel.objects.get(id=structurename)
    r.TrainigTyped = TrainigTypedModel.objects.get(TrainigTyped=TrainigTyped)
    r.lang = LanguageModel.objects.get(id=lang)
    r.price = feeModel.objects.get(id=price)
    r.installment = installment
    r.remaining_installment = remaining_installment
    r.status = 'Registered'
    r.stud_id = random_string_generator()
    # r.inqid = inquiryModel.objects.get(id=inqid)
    r.save()
    return redirect('/Students_Registered/')

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def registerconfirm(request):
    r = request.GET.get('id')
    obj = inquiryModel.objects.filter(id=r)
    ab = structureModel.objects.all()
    da = {
        'result': obj,
        'res': ab,
    }
    return render(request,'admin/inquiry_registation_form.html',da)

def cid(request):
    try:
        id = request.POST.get('id')
        a = structureModel.objects.get(id=id)
        b = list(feeModel.objects.filter(structurename=a.id).values())
        data = {
            'data': b,
            'result': 'true'
        }
    except BaseException:
        data = {
            'result': 'false'
        }
    return JsonResponse(data)


def pid(request):
    try:
        id = request.POST.get('id')
        a = LanguageModel.objects.get(id=id)
        b = list(feeModel.objects.filter(lang=a).values())
        data = {
            'data': b,
            'result': 'true'
        }
    except BaseException:
        data = {
            'result': 'false'
        }
    return JsonResponse(data)


def did(request):
    id = request.POST.get('id')
    b = list(LanguageModel.objects.filter(id=id).values())
    data = {
        'data': b
    }

    return JsonResponse(data)
# -------- registration form of inquiry end ------------------------------

# ===================================# Students_Registered =============================
def Students_Registered(request):
    r = registrationModel.objects.filter(status='Registered')
    id = request.GET.get('id')
    obj = batchModel.objects.filter(id=id)
    lang=LanguageModel.objects.all()

    data = {
        'rr': obj,
        'result': r,
        'lang1':lang,

    }
    return render(request,'admin/Students_Registered.html',data)



# create user user side mate che
def cr_user(request):
    r = request.GET.get('id')
    d = registrationModel.objects.get(id=r)
    s = useradminModel()
    s.fullname = d.fullname
    s.password = d.stud_id
    s.save()
    return redirect('/Students_Registered/')
# =========-====== recipt mate che=========================
def rec_getdata(request):
    r = request.GET.get('id')
    obj = registrationModel.objects.filter(id=r)
    data = {
        'result': obj
    }
    return render(request, 'admin/receipt.html', data)
# recipt mate che==============================

# registration table mathe delete karva
def regidelete(request):
    r = request.GET.get('id')
    obj = registrationModel.objects.get(id=r)
    obj.delete()
    return redirect('/Students_Registered/')
# ==================================================
def regidelete1(request):
    r = request.GET.get('id')
    obj = registrationModel.objects.get(id=r)
    obj.delete()
    return redirect('/Completecourse/')




def sendmessagefor_registered(request):
    r = request.GET.get('id')
    d = registrationModel.objects.get(id=r)
    sendsms('' +d.pnum,'Hello I am From Digital Campus.Your Inquiry Is Registered!!\nYour Userid: ' + d.fullname + 'Password:' + d.stud_id)
    return redirect("/Students_Registered/")

def Completecourse(request):
    a = registrationModel.objects.filter(status='closed')
    data = {
        'results': a
    }
    return render(request,'admin/Completecourse.html',data)

def clostoreq(request):
    r = request.GET.get('id')
    obj = registrationModel.objects.get(id=r)
    obj.status = 'Registered'
    obj.save()
    return redirect('/Completecourse/')

# ---------------closed mate che------------------
def clos(request):
    r = request.GET.get('id')
    obj = registrationModel.objects.get(id=r)
    obj.status = 'closed'
    obj.save()
    return redirect('/Completecourse/')
# ------------------------------------------end===========
# -----------receipt mate-----------------
def receipt(requst):
    return render(request,'admin/receipt.html')

# -----------receipt mate end-----------------


# ==================================== # Students_Registered end ========================




# -------------------------------------------inquiry end -------------------------------------------------------------------------------


# ========================== language start ====================
def language(request):
    r = LanguageModel.objects.all()
    data = {
        'result': r
    }
    return render(request,'admin/language.html',data)

def deletelang(request):
    r = request.GET.get('id')
    obj = LanguageModel.objects.get(id=r)
    obj.delete()
    return redirect('/language/')

def languegeinsert(request):
    # id = request.POST.get('id')  # update id
    lang = request.POST.get('lang')
    langimg = request.FILES['langimg']
    fs = FileSystemStorage()
    langimg = fs.save(langimg.name, langimg)
    desc = request.POST.get('desc')
    dur = request.POST.get('dur')
    trainigntype = request.POST.get('trainigntype')
    r = LanguageModel()
    r.lang = lang
    r.langimg=langimg
    r.desc = desc
    r.dur = dur
    r.trainigntype=trainigntype
    # r.id = id
    r.save()
    return redirect('/language/')

# ===========================lang end ======================


# ======================structure start======================
def sructure(request):
    data = structureModel.objects.all()
    da = {
        'result': data,
    }
    return render(request,'admin/sructure.html',da)

def structureinsert(request):
    strID = request.POST.get("id")
    structurename = request.POST.get("structurename")
    if (strID != "0"):
        r = structureModel.objects.get(id=strID)
    else:
        r = structureModel()
    r.structurename = structurename
    r.save()
    return redirect('/sructure/')

def sturcturedelete(request):
    r = request.GET.get('id')
    obj = structureModel.objects.get(id=r)
    obj.delete()
    return redirect('/sructure/')
# =====================structure end==============================

# ==========================fees start==============================
def fees(request):
    r = feeModel.objects.all()
    data = LanguageModel.objects.all()
    dab = structureModel.objects.all()
    da = {
        'result': data,
        're': dab,
        'akash': r
    }
    return render(request,'admin/fees.html',da)

def feesinsert(request):
    hid = request.POST.get('hid')
    structurename = request.POST.get('structurename')
    lang = request.POST.get('lang')
    price = request.POST.get('price')
    r = feeModel()
    s = LanguageModel.objects.get(id=lang)
    b = structureModel.objects.get(id=structurename)
    r.structurename = b
    r.lang = s
    r.price = price
    r.id = hid
    r.save()
    return redirect('/fees/')

def feesdelete(request):
    r = request.GET.get('id')
    obj =feeModel.objects.get(id=r)
    obj.delete()
    return redirect('/fees/')

# ===========================fees end=============================

# ======================== addbatch start ========================
def addbatch(request):
    c = LanguageModel.objects.all()
    d = batchModel.objects.all()
    data = {
        'results': c,
        'res': d
    }
    return render(request,'admin/Add batch.html',data)



def batchinsert(request):
    lang = request.POST.get('lang')
    batch = request.POST.get('batch')
    time1 = request.POST.get('time1')
    time2 = request.POST.get('time2')
    day = ','.join(request.POST.getlist('day'))
    r = batchModel()
    s = LanguageModel.objects.get(lang=lang)
    r.lang = s
    r.batch = batch
    r.time1 = time1
    r.time2 = time2
    r.day = day
    r.save()
    return redirect('/addbatch/')

def batchdel(request):
    r = request.GET.get('id')
    obj =batchModel.objects.get(id=r)
    obj.delete()
    return redirect('/addbatch/')


# aa message mate che ke aje batch cancle thai che aem
def cancleb(request):
    r = request.GET.get('id')
    d = registrationModel.objects.filter(batch=r)
    some_var = d
    for content in some_var:
        sendsms("" + content.pnum, "Today batch is cancle for some reasons !")
    return redirect("/addbanch/")

def confirminquirytoregistion(request):
    r = request.GET.get('id')
    obj = inquiryModel.objects.get(id=r)
    obj.status = 'registered'
    obj.save()
    return redirect('/Confirminquiry/')


def allocate_batch_student(request):
    c = batchModel.objects.all()
    d = registrationModel.objects.filter(batch=None)
    data = {
        'results': c,
        'res': d

    }
    return render(request,'admin/allocate_batch_student.html',data)

def allcoatebatchinsert(request):
    some_var = request.POST.getlist('check[]')
    batch = request.POST.get('batch')
    for i in range(len(some_var)):
        s = registrationModel.objects.get(id=some_var[i])
        d = batchModel()
        b = batchModel.objects.get(batch=batch)
        print(b)
        s.batch = b
        s.save()

    return redirect('/allocate_batch_student/')

# ========================= endbatch =============================

# ==========================training typeadd =====================

def TrainigTyped(request):
    dat = TrainigTypedModel.objects.all()
    data={
        'resu':dat
    }
    return render(request,'admin/TrainigTyped.html',data)

def TrainigTypedinsert(request):
    TrainigTyped = request.POST.get('TrainigTyped')
    r = TrainigTypedModel()
    r.TrainigTyped = TrainigTyped
    r.save()
    return redirect('/TrainigTyped/')

def Trainigydelete(request):
    r = request.GET.get('id')
    obj = TrainigTypedModel.objects.get(id=r)
    obj.delete()
    return redirect('/TrainigTyped/')
# ==========================training typeadd end =====================



# ============================= RaimaingFees start ===================
def RaimaingFees (request):
    r = registrationModel.objects.filter(status='Registered')
    data = {

        'result': r,

    }
    return render(request,'admin/RaimaingFees.html',data)

def decree(request):
    r = request.GET.get('id')
    obj = registrationModel.objects.get(id=r)
    # monthdalta aek function che month get karva mate ok  or day mate timedelta ae method che datetime ni ok....
    obj.remaining_installment = int(obj.remaining_installment) - 1
    s = obj.remaining_installment
    d = {
        'data': s
    }
    obj.save()
    sendsms('' + obj.pnum, 'Your Next PaymentDate is : ' + str(datetime.today() + monthdelta.monthdelta(1)))
    return redirect('/Students_Registered/', d)

def sendmessagefor_registered12345(request):
    r = request.GET.get('id')
    d = registrationModel.objects.get(id=r)
    # monthdalta aek function che month get karva mate ok  or day mate timedelta ae method che datetime ni ok....
    sendsms('' + d.pnum, 'Your Next PaymentDate is : ' + str(datetime.today() + monthdelta.monthdelta(1)))
    return redirect("/Students_Registered/")

# def rfeedelete(request):
#     r = request.GET.get('id')
#     obj = registrationModel.objects.get(id=r)
#     obj.delete()
#     return redirect('/RaimaingFees/')
# ==========================RaimaingFees end =========================

# ================================Assignments for student start====================
def Assignments(request):
    d = registrationModel.objects.all()
    data = {
        'results': d
    }
    return render(request,'admin/Assignments.html',data)

def Assignmentsinsert(request):
    some_var = request.POST.getlist('check[]')
    ass = request.POST.get('ass')
    for i in range(len(some_var)):
        s = registrationModel.objects.get(id=some_var[i])
        s.ass = ass
        s.save()
    return redirect('/Assignments/')

def sendsmsgood(request):
    r = request.GET.get('id')
    d = registrationModel.objects.get(id=r)
    sendsms('' + d.pnum, 'Hello I am From Digital Campus.Your Assignment Link Is Here\n' 'Your Assignment:' + d.ass)
    return redirect("/assignmentforadmin/")

# ===============================Assignments for end=================================================================


# =============================all certificate ======================================================================
def Experience_Certificate1(request):
    r = request.GET.get('cid')
    c = registrationModel.objects.filter(id=r)
    data = {
        'results': c
    }
    return render(request, 'admin/certificate/Experience Certificate.html', data)



def Internship_Certificate1(request):
    r = request.GET.get('cid')
    obj = registrationModel.objects.filter(id=r)
    data = {
        'result': obj
    }
    return render(request, 'admin/certificate/Internship Certificate.html', data)

def Leave_for_Internship1(request):
    r = request.GET.get('cid')
    c = registrationModel.objects.filter(id=r)
    data = {
        'result': c
    }
    return render(request, 'admin/certificate/Leave_for_Internship.html', data)

def Offer_letter_Certificate1(request):
    r = request.GET.get('cid')
    c = registrationModel.objects.filter(id=r)
    data = {
        'result': c
    }
    return render(request, 'admin/certificate/Offer_letter Certificate.html', data)
# =============================all certificate end ===============================================


# =================recipt ma send mail mate che--------------------
def sendmail(request):
    message=request.POST.get('message','')
    subject=request.POST.get('subject','')
    mail_id = request.POST.get('email','')
    email=EmailMessage(subject,message,EMAIL_HOST_USER,[mail_id])
    email.content_subtype='html'
    file = request.FILES['file']
    email.attach(file.name,file.read(),file.content_type)
    email.send()
    return HttpResponse('send succesfully!!!')

# ======================mail end-------------------------------------




# =====================admin side inqu mate--------------------------
def admin_inquiry(request):
    d = LanguageModel.objects.all()
    u = structureModel.objects.all()
    v = TrainigTypedModel.objects.all()
    data = {
        'res': d,
        'ress': u,
        'resu': v

    }
    return render(request,'admin/inq/admin_inquiry.html',data)

def admin_inq_insert(request):
    studentphotos = request.FILES['studentphotos']
    fs = FileSystemStorage()
    studentphotos = fs.save(studentphotos.name, studentphotos)
    fullname = request.POST.get('fullname')
    pnum = request.POST.get('pnum')
    dob = request.POST.get('dob')
    email = request.POST.get('email')
    reffname = request.POST.get('reffname')
    reffcontact = request.POST.get('reffcontact')
    inqdate = request.POST.get('inqdate')
    University = request.POST.get('University')
    Institute = request.POST.get('Institute')
    Semester = request.POST.get('Semester')
    Stream = request.POST.get('Stream')
    lang = request.POST.get('lang')
    structurename = request.POST.get('structurename')
    TrainigTyped = request.POST.get('TrainigTyped')

    status = request.POST.get('status')

    r = admin_inquiryModel()
    r.studentphotos = studentphotos
    r.fullname = fullname
    r.pnum = pnum
    r.dob = dob
    r.email = email
    r.reffname = reffname
    r.reffcontact = reffcontact
    r.inqdate1 = inqdate
    r.University = University
    r.Institute = Institute
    r.Semester = Semester
    r.Stream = Stream
    r.lang = LanguageModel.objects.get(id=lang)
    r.structurename = structureModel.objects.get(id=structurename)
    r.TrainigTyped = TrainigTypedModel.objects.get(id=TrainigTyped)
    r.status = 'pending'
    r.save()
    return render(request, 'admin/inq/admin_inquiry.html')

def admin_pending(request):
    data = admin_inquiryModel.objects.filter(status="pending")
    da = {
        'results': data,
    }
    return render(request,'admin/inq/admin_pending.html',da)

def pendelete1(request):
    r = request.GET.get('id')
    obj = inquiryModel.objects.get(id=r)
    obj.delete()
    return redirect('/admin_pending/')

def confirminquiry1(request):
    r = request.GET.get('id')
    obj = admin_inquiryModel.objects.get(id=r)
    obj.status = 'confirm'
    obj.save()
    return redirect('/admin_confirm/')

def admin_confirm(request):
    a = admin_inquiryModel.objects.filter(status='confirm')
    ab = structureModel.objects.all()
    bb = LanguageModel.objects.all()
    cc = feeModel.objects.all()
    data = {
        'results': a,
        'stru': ab,
        'lang': bb,
        'fee': cc
    }
    return render(request,'admin/inq/admin_confirm.html',data)


def confirminquirytoregistion1(request):
    r = request.GET.get('id')
    obj = admin_inquiryModel.objects.get(id=r)
    obj.status = 'registered'
    obj.save()
    return redirect('/admin_confirm/')

def confirmdelete1(request):
    r = request.GET.get('id')
    obj = admin_inquiryModel.objects.get(id=r)
    obj.delete()
    return redirect('/admin_confirm/')

def registerconfirm1(request):
    r = request.GET.get('id')
    obj = admin_inquiryModel.objects.filter(id=r)
    ab = structureModel.objects.all()
    da = {
        'result': obj,
        'res': ab,
    }
    return render(request,'admin/inquiry_registation_form.html',da)



# =====================admin side inqu mate--------------------------


