import datetime
from django.db import models
from django.utils import timezone

#--------------------- admin login model start--------------------
class LoginModel(models.Model):
    photos= models.CharField('photos', max_length=200)
    email = models.EmailField('email',unique=True)
    password = models.CharField('pass',max_length=30)
    fullname = models.CharField('fullname',max_length=30)

# class User_registration(models.Model):
#     name = models.CharField('name', max_length=30)
#     email = models.CharField('email', max_length=30)
#     phone_no = models.CharField('phone_no', max_length=15)
#     password = models.CharField('password', max_length=15)
#     age = models.CharField('age', max_length=5)
#     gender = models.CharField('gender', max_length=7)
#     total_price = models.BigIntegerField('total_price', null=True, default=0)

#--------------------- admin login model End--------------------------------

# =============================== acm model =====================

class roleModel(models.Model):
    role = models.CharField('role',max_length=20, unique=True)
    roleimage = models.CharField('roleimage',max_length=200, )

class privilegeModelACM(models.Model):
    privname = models.CharField('privilegename', max_length=30)
    fontcode = models.CharField('fontcode', max_length=30)

class privComponentModelACM(models.Model):
    privId = models.ForeignKey(privilegeModelACM, on_delete=models.CASCADE)
    pCompName = models.CharField('privCompName', max_length=100)
    pCompLink = models.CharField('privCompLink', max_length=100)

class stateModel(models.Model):
    statecode = models.CharField('statecode', max_length=30)
    statename = models.CharField('statename', max_length=30)


class cityModel(models.Model):
    stateId = models.ForeignKey(stateModel, on_delete=models.CASCADE)
    cityname = models.CharField('cityname', max_length=30)


class EmployeeModelACM(models.Model):
    empid = models.CharField('empid', max_length=30, unique=True)
    fullname = models.CharField('fullname', max_length=50)
    password = models.CharField('password', max_length=30, unique=True)
    role_id = models.ForeignKey(roleModel, on_delete=models.CASCADE)
    # company_id = models.ForeignKey(CompanyModelACM, on_delete=models.CASCADE)
    bloodgroup = models.CharField('bloodgroup', max_length=30)
    gender = models.CharField('gender', max_length=30)
    mstatus = models.CharField('mstatus', max_length=30)
    mobnum = models.BigIntegerField('mobnum', unique=True)
    nativenum = models.BigIntegerField('nativenum', unique=True)
    email = models.CharField('email', max_length=30, unique=True)
    dob = models.CharField('dob', max_length=30)
    paddress = models.CharField('paddress', max_length=30)
    taddress = models.CharField('taddress', max_length=30)
    state_id = models.ForeignKey(stateModel, on_delete=models.CASCADE)
    city_id = models.ForeignKey(cityModel, on_delete=models.CASCADE)
    # area_id = models.ForeignKey(areaModel, on_delete=models.CASCADE)
    zipcode = models.BigIntegerField('zipcode')
    bsalary = models.BigIntegerField('basicsalary')
    tax = models.CharField('tax', max_length=30)
    taxpercentage = models.IntegerField('taxpercentage', null=True)
    fsalary = models.BigIntegerField('finalsalary')
    workdays = models.CharField('workdays', max_length=200)
    asignleave = models.IntegerField('asignleave')
    cutleave = models.IntegerField('cutleave')
    cuthalfleave = models.IntegerField('cuthalfleave')
    comingtime = models.CharField('comingtime', max_length=50)
    leavingtime = models.CharField('leavingtime', max_length=50)
    fathername = models.CharField('fathername', max_length=200)
    mothername = models.CharField('mothername', max_length=200)
    fcontact = models.BigIntegerField('fcontact', unique=True)
    mcontact = models.BigIntegerField('mcontact', unique=True)
    adharcard = models.CharField('adharcard', max_length=200)
    pancard = models.CharField('pancard', max_length=200)
    photo = models.CharField('photo', max_length=200)
    bankname = models.CharField('bankname', max_length=30)
    branchname = models.CharField('branchname', max_length=30)
    accnum = models.BigIntegerField('accnum', unique=True)
    acctype = models.CharField('acctype', max_length=30)
    pannumber = models.BigIntegerField('pannumber', unique=True)
    chqnumber = models.BigIntegerField('chqnumber', unique=True)
    codeifsc = models.BigIntegerField('codeifsc', unique=True)
    codemicr = models.BigIntegerField('codemicr', unique=True)


class PrivToRoleModelACM(models.Model):
    roleId = models.ForeignKey(roleModel, on_delete=models.CASCADE)
    privId = models.TextField('role_privilage')


class PrivToUserModelACM(models.Model):
    roleId = models.ForeignKey(roleModel, on_delete=models.CASCADE)
    empId = models.ForeignKey(EmployeeModelACM, on_delete=models.CASCADE)
    privId = models.TextField('role_user_privilage')
# ========================= acm end ===========================

# ====================== language model ====================
class LanguageModel(models.Model):
    lang = models.CharField('lang', max_length=25)
    langimg=models.CharField('langimg', max_length=200)
    desc = models.TextField('desc', max_length=200)
    dur = models.CharField('dur', max_length=25)
    # trainigntype= models.CharField('trainigntype',max_length=25)
# ======================== lang end===================================


# =============TrainigTyped model====================---------------
class TrainigTypedModel(models.Model):
    TrainigTyped =models.CharField('TrainigTyped', max_length=50)
# =========================================end=====================


# ==============================structre==============================
class structureModel(models.Model):
    structurename = models.CharField('structurename', max_length=20,unique=True)
# ================================structre  end =====================

# ============================fees start =================================
class feeModel(models.Model):
    structurename = models.ForeignKey(structureModel,on_delete=models.CASCADE)
    lang = models.ForeignKey(LanguageModel,on_delete=models.CASCADE)
    price = models.IntegerField('price')
# ========================fee end========================================

# =======================batch model=========================
class batchModel(models.Model):
    lang = models.ForeignKey(LanguageModel, on_delete=models.CASCADE)
    batch =models.CharField('batch',max_length=20)
    time1 = models.TimeField('time1')
    time2 = models.TimeField('time2')
    day = models.CharField('day',max_length=100)
# ======================batch end===========================


# -------------------- user side model --------------------------------------------
class inquiryModel(models.Model):
    studentphoto =models.CharField('studentphoto',max_length=200)
    fullname =models.CharField('fullname',max_length=25, blank =False)
    pnum = models.CharField('pnum',max_length=12,unique=True)
    structurename = models.ForeignKey(structureModel, on_delete=models.CASCADE)
    dob=models.DateField('dob')
    email = models.EmailField('email',unique=True)
    reffname = models.CharField('reffname',max_length=20)
    reffcontact = models.CharField('reffcontact',max_length=12)
    inqdate=models.DateField('inqdate',default=timezone.now(), null=True)
    University = models.CharField('University',max_length=50)
    Institute = models.CharField('Institute', max_length=50)
    Semester = models.CharField('Semester', max_length=50)
    Stream = models.CharField('Stream', max_length=50)
    lang = models.ForeignKey(LanguageModel, on_delete=models.CASCADE)
    TrainigTyped = models.ForeignKey(TrainigTypedModel, on_delete=models.CASCADE)
    status = models.CharField('status', max_length=20)



class useradminModel(models.Model):
    # email = models.EmailField('email',blank=False)
    password = models.CharField('passowrd',max_length=30,blank=False)
    fullname = models.CharField('fullname',max_length=20,)
# -------------------------------------------- user model end --------------------------------------------







# =================== regisration model ===============================

class registrationModel(models.Model):
    fullname = models.CharField('fullname',max_length=20)
    pnum = models.CharField('pnum',max_length=12)
    email = models.EmailField('email')
    reffname = models.CharField('reffname',max_length=20)
    reffcontact = models.CharField('reffcontact',max_length=12)
    date1=models.DateField('date1',default=timezone.now(),null=True)
    University = models.CharField('University',max_length=50)
    Institute = models.CharField('Institute', max_length=50)
    Semester = models.CharField('Semester', max_length=50)
    Stream = models.CharField('Stream', max_length=50)
    structurename = models.ForeignKey(structureModel,on_delete=models.CASCADE)
    TrainigTyped = models.ForeignKey(TrainigTypedModel, on_delete=models.CASCADE)
    lang = models.ForeignKey(LanguageModel,on_delete=models.CASCADE)
    price=models.ForeignKey(feeModel,on_delete=models.CASCADE)
    batch = models.ForeignKey(batchModel,on_delete=models.CASCADE,null=True)
    installment=models.IntegerField('installment')
    remaining_installment=models.IntegerField('installment')
    status = models.CharField('status', max_length=20)
    stud_id = models.CharField('stud_id', max_length=11,default=23)
    ass = models.CharField('ass', max_length=500,null=True)
# ===================== regi end =====================

#
# ======================admin inquiryModel start=======================================
class admin_inquiryModel(models.Model):
    studentphotos = models.CharField('studentphotos', max_length=200)
    fullname = models.CharField('fullname', max_length=25, blank=False)
    pnum = models.CharField('pnum', max_length=12, )
    structurename = models.ForeignKey(structureModel, on_delete=models.CASCADE)
    dob = models.DateField('dob')
    email = models.EmailField('email', )
    reffname = models.CharField('reffname', max_length=20)
    reffcontact = models.CharField('reffcontact', max_length=12)
    inqdate = models.DateField('inqdate', default=timezone.now(), null=True)
    University = models.CharField('University', max_length=50)
    Institute = models.CharField('Institute', max_length=50)
    Semester = models.CharField('Semester', max_length=50)
    Stream = models.CharField('Stream', max_length=50)
    lang = models.ForeignKey(LanguageModel, on_delete=models.CASCADE)
    TrainigTyped = models.ForeignKey(TrainigTypedModel, on_delete=models.CASCADE)
    status = models.CharField('status', max_length=20)
# ======================admin inquiryModel end=======================================





