from django.shortcuts import render, redirect
from .models import DebitCard, InstituteOwner, Institute
from .forms import DebitCardForm, InstituteOwnerForm, InstituteForm
from django.http import HttpResponse

# Create your views here.
def only_upper(s):
    return "".join(c for c in s if c.isupper())


def addInstitutes(request):
    if request.method == "POST":
        DebitCardData = DebitCardForm(request.POST)
        InstituteData = InstituteForm(request.POST)
        InstituteOwnerData = InstituteOwnerForm(request.POST)
        if DebitCardData.is_valid():
            CardKey = DebitCardData.save()
            if InstituteData.is_valid():
                Institute_Name = InstituteData['Name'].value()
                Institute_State = InstituteData.save(commit=False)
                Institute_State.URL = only_upper(Institute_Name)
                ID = DebitCard.objects.get(Card_ID=CardKey.pk)
                Institute_State.Card_ID = ID
                Institute_State.save()
                if InstituteOwnerData.is_valid():
                    InstituteOwner_State = InstituteOwnerData.save(commit=False)
                    ID = Institute.objects.get(Institute_ID=Institute_State.pk)
                    InstituteOwner_State.Institute_ID = ID
                    InstituteOwner_State.save()
                    return redirect("/notifications")
    else:
        DebitCardData = DebitCardForm()
        InstituteData = InstituteForm()
        InstituteOwnerData = InstituteOwnerForm()
    return render(request, "addinstitutes.html", {
        'DebitCardData': DebitCardData,
        'InstituteData': InstituteData,
        'InstituteOwnerData': InstituteOwnerData,
    })


def notifications(request):
    Institutes = Institute.objects.filter(Token=0)
    return render(request, "notifications.html", { 'Institutes': Institutes})


def approveRequest(request , pk1):
    acceptInstitute = Institute.objects.get(pk=pk1)
    acceptInstitute.Token = 1
    acceptInstitute.save([['Token']])
    return redirect("/notifications")



