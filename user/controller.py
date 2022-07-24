import urllib

from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.http import JsonResponse

from final.models import structureModel, LanguageModel, inquiryModel, useradminModel, TrainigTypedModel, \
    registrationModel


def home(request):
    d = LanguageModel.objects.all()
    u = structureModel.objects.all()
    v= TrainigTypedModel.objects.all()
    data = {
        'res': d,
        'ress': u,
        'resu':v

    }
    return render(request, 'user/home.html', data)


# ==================================login part start =====================
def login(request):
    return render(request,'user/login.html')

def logout(request):
    try:
        del request.session['fullname']
        del request.session['password']
    except KeyError:
        pass
    return render(request,'user/login.html')


def logininsert1(request):
    fullname = request.POST.get('fullname')
    password = request.POST.get('password')
    try:
        re = useradminModel.objects.get(fullname=fullname)
    except useradminModel.DoesNotExist:
        re = None
    if (re != None):
        try:
            rw = useradminModel.objects.get(fullname=fullname, password=password)
        except useradminModel.DoesNotExist:
            rw = None
        if (rw != None):
            request.session['lid'] = rw.id
            request.session['fullname'] = rw.fullname
            # request.session['email'] = rw.email
            return render(request, 'user/afterlogin.html')
        else:
            da = {
                'msg': 'WRONG PASSWORD!'
            }
            return render(request, 'user/login.html', da)
    else:
        da = {
            'msg': 'WRONG EMAILID!'
        }
        return render(request, 'user/login.html', da)


def student_inquiry(request):
    studentphoto = request.FILES['studentphoto']
    fs = FileSystemStorage()
    studentphoto = fs.save(studentphoto.name, studentphoto)
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

    r = inquiryModel()
    r.studentphoto= studentphoto
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
    return render(request, 'user/home.html')

# ===========================end=============================================

# ========certificate and receipt mate nu che aaa start ====================

# ana badha certificate ma get_certificatedata vadu function che ae pramane badhu set karvanu baki che...


def Offer_letter_Certificate(request):
    cur_user = request.session['fullname']
    d = registrationModel.objects.filter(fullname=cur_user)
    some_var = d

    for content in some_var:
        if (content.status == "closed"):
            if content.TrainigTyped.TrainigTyped == str("Offer_letter_Certificate"):
                data = {
                    'result': some_var
                }
                return render(request, 'admin/certificate/Offer_letter Certificate.html', data)
            else:
                return HttpResponse('Sorry!! Not For You')
        else:
            return HttpResponse('<h1>Please Completing Your Course</h1>')


def Experience_Certificate(request):
    cur_user = request.session['fullname']
    d = registrationModel.objects.filter(fullname=cur_user)
    some_var = d

    for content in some_var:
        if (content.status == "closed"):
            if content.TrainigTyped.TrainigTyped == str("Experience_Certificate"):
                data = {
                    'results': some_var
                }
                return render(request, 'admin/certificate/Experience Certificate.html', data)
            else:
                return HttpResponse('Sorry!! Not For You')
        else:
            return HttpResponse('<h1>Please Completing Your Course</h1>')


def Leave_for_Internship(request):
    cur_user = request.session['fullname']
    d = registrationModel.objects.filter(fullname=cur_user)
    some_var = d

    for content in some_var:
        if (content.status == "closed"):
            if content.TrainigTyped.TrainigTyped == str("Leave_for_Internship"):
                data = {
                    'result': some_var
                }
                return render(request, 'admin/certificate/Leave_for_Internship.html', data)
            else:
                return HttpResponse('Sorry!! Not For You')
        else:
            return HttpResponse('<h1>Please Completing Your Course</h1>')


def gne_certificate(request):
    cur_user = request.session['fullname']
    d = registrationModel.objects.filter(fullname=cur_user)
    some_var = d

    for content in some_var:
        if (content.status == "closed"):
            data = {
                'result': some_var
            }
            return render(request, 'admin/certificate/Internship Certificate.html', data)
        else:
            return HttpResponse('<h1>Please Completing Your Course</h1>')


def generae_certificatedata(request):
    cur_user = request.session['fullname']
    d = registrationModel.objects.filter(fullname=cur_user)
    some_var = d
    for content in some_var:
        if (content.status == "closed"):
            # print(content.typedname.typedname)
            if content.TrainigTyped.TrainigTyped == str("Intership trannig"):
                data = {
                    'result': some_var
                }
                return render(request, 'admin/certificate/Internship Certificate.html', data)
            else:
                return HttpResponse('Sorry!! Not For You')
        else:
            return HttpResponse('<h1>Please Completing Your Course</h1>')

def gen_recipt(request):
    cur_user = request.session['fullname']
    # print(cur_user)
    d = registrationModel.objects.filter(fullname=cur_user)
    some_var = d
    for content in some_var:
        # if (content.remaining_installment < content.installment):
        if (content.remaining_installment == 0):
            data = {
                'result': some_var
            }
            return render(request, 'admin/receipt.html', data)
        else:

            return HttpResponse('<h1>Please Completing Your Payment</h1>')
# ========certificate and receipt mate nu che aaa end ====================


# ==========temp lang na========--------------------------------
def CANDCPLUS(request):
    return render(request, 'user/lang/CANDC++.html')

def devlopment(request):
    return render(request, 'user/lang/devlopment.html')

def htmlandcss(request):
    return render(request, 'user/lang/htmlandcss.html')

def javalangdecription(request):
    return render(request, 'user/lang/javalangdecription.html')


def pythonlang(request):
    return render(request, 'user/lang/pythonlang.html')

def nodejs(request):
    return render(request, 'user/lang/nodejs.html')
# =========================end==================










# =========login kariya pachinu che aa user side ============================
def afterlogin(request):
    return render(request,'user/afterlogin.html')
# =========login kariya pachinu che aa user side end ============================