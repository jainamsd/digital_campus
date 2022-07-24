from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from final import view
from django.conf import settings

urlpatterns = [
    path('', include('user.urls')),
    path('admin/',view.login),
    path('logout/',view.logout),
    path('home/',view.home),
    path('dashboard/',view.dashboard),
    path('logininsert/',view.logininsert),
    path('crete_new_user/',view.crete_new_user),
    path('newuserwithoutface/',view.newuserwithoutface),
    # path('newuserface/', view.newuserface),
    path('create_dataset/',view.Create_dataset),
    path('detect/',view.Detect),

    # path('user_registration/',view.user_registration),




    # ==========acm thi  login kari home kholavu hoy tyyare==============
    path('acmhome/',view.acmhome),
    path('insetacmdata/',view.insetacmdata),

    # ==========acm login end=============


    # ========== acm url ========--------------
    path('acmrole/', view.acmrole),
    path('addacmrole/', view.addacmrole),
    path('acmroledelete/', view.acmroledelete),
    path('PrivilegeACM/', view.PrivilegeACM),
    path('addPrivilegeACM/', view.addPrivilegeACM),
    path('privelegedelet/', view.privelegedelet),
    path('PrivComponentACM/', view.PrivComponentACM),
    path('addPrivComponentACM/', view.addPrivComponentACM),
    path('emp/', view.employee),
    path('addEmpACM/', view.addEmpACM),
    path('PrivToRoleACM/', view.PrivToRoleACM),
    path('AddprivToroleACM/', view.AddprivToroleACM),
    path('PrivToUserACM/', view.PrivToUserACM),
    path('AddprivTouserACM/', view.AddprivTouserACM),
    path('getpriv/', view.getpriv),
    path('getuser/', view.getuser),
    path('getprivileges/', view.getprivileges),
    # ======================= acm url end ===============================

    # ---------------- state and city start ---------------------------
    path('state/', view.state),
    path('addState/', view.addState),
    path('city/', view.city),
    path('addCity/', view.addCity),
    path('statedel/', view.statedel),
    path('citydel/', view.citydel),
    # ---------------- state and city End ----------------------------

    # =======================language==============
    path('language/', view.language),
    path('languegeinsert/', view.languegeinsert),
    path('deletelang/', view.deletelang),
    # ================end lang =====================

    # ================= structure=================
    path('sructure/', view.sructure),
    path('structureinsert/', view.structureinsert),
    path('sturcturedelete/', view.sturcturedelete),
    # ================structure end ==============

    # ===============fees-========================
    path('fees/', view.fees),
    path('feesinsert/', view.feesinsert),
    path('feesdelete/', view.feesdelete),
    # ====================fees end================

    # ===============batch start =================
    path('addbatch/', view.addbatch),
    path('batchinsert/', view.batchinsert),
    path('batchdel/', view.batchdel),
    path('cancleb/', view.cancleb),
    # ===============end batch====================
    # ===============training typed==============
    path('TrainigTyped/', view.TrainigTyped),
    path('TrainigTypedinsert/', view.TrainigTypedinsert),
    path('Trainigydelete/', view.Trainigydelete),
    # ===============training typed==============

    # ===========================Assignments for student==================
    path('Assignments/',view.Assignments),
    path('Assignmentsinsert/',view.Assignmentsinsert),
    path('sendsmsgood/',view.sendsmsgood),
    # ===============================Assignments end ======================


    # ================ inquiry module start ===========================
    path('Pendinginquiry/', view.Pendinginquiry),
    path('pendelete/', view.pendelete),
    path('coninq/', view.confirminquiry),
    path('Confirminquiry/', view.confirm),
    path('caninq/', view.canreg),
    path('cancel/', view.cancel),
    path('confirmdelete/', view.confirmdelete),
    path('cancledelete/', view.cancledelete),

    # ================= registration inqury wizard start ====================

    path('inquiry_registation_form/', view.inquiry_registation_form),
    path('insertregistrations/', view.insertregistrations),
    path('registerconfirm/', view.registerconfirm),
    path('cid/',view.cid),
    path('pid/',view.pid),
    path('did/', view.did),
    # # ================= registration inqury wizard end ====================

    # ========================== Students Registered ==========================
    path('regidelete/', view.regidelete),
    path('Students_Registered/', view.Students_Registered),
    path('sendmessagefor_registered/', view.sendmessagefor_registered),
    path('clos/', view.clos),
    path('confirminquirytoregistion/', view.confirminquirytoregistion),
    path('cr_user/', view.cr_user),
    path('Completecourse/', view.Completecourse),
    path('clostoreq/', view.clostoreq),
    path('receipt/', view.receipt),
    path('rec_getdata/', view.rec_getdata),
    path('regidelete1/', view.regidelete1),

    # =============================Students Registered end ====================
    #   allocation of batch--------------------------
    path('allocate_batch_student/',view.allocate_batch_student),
    path('allcoatebatchinsert/',view.allcoatebatchinsert),
    # ============== end allocation batch ===============
    #=================== inq end ===============================================================

    # ======================RaimaingFees----------------------------------------
    path('RaimaingFees/', view.RaimaingFees),
    path('decree/', view.decree),
    path('sendmessagefor_registered12345/', view.sendmessagefor_registered12345),
    # path('rfeedelete/', view.rfeedelete),

    #=========================== RaimaingFees================================


    #====================all admin sid mate certifiactes =================
    path('Experience_Certificate1/', view.Experience_Certificate1),
    path('Internship_Certificate1/', view.Internship_Certificate1),
    path('Leave_for_Internship1/', view.Leave_for_Internship1),
    path('Offer_letter_Certificate1/', view.Offer_letter_Certificate1),
    #=============================certi end----------------------------

    #=================lockscreen==========================================
    path('lockscreen/',view.lockscreen),
    path('lockscreeninsert/',view.lockscreeninsert),
    #=================lockscreen end======================================

    #----------send mail-----------------
    path('sendmail/',view.sendmail),
    # ----------send mail-----------------


    #================admin side inq------------
    path('admin_inquiry/',view.admin_inquiry),
    path('admin_inq_insert/',view.admin_inq_insert),
    path('admin_pending/',view.admin_pending),
    path('admin_confirm/',view.admin_confirm),
    path('pendelete1/',view.pendelete1),
    path('coninq1/', view.confirminquiry1),
    path('confirminquirytoregistion1/', view.confirminquirytoregistion1),
    path('confirmdelete1/', view.confirmdelete1),
    path('registerconfirm1/', view.registerconfirm1),
    #================admin side inq------------





]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
