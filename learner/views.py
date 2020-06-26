from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def youtube(request):
    return HttpResponse('''<a href="https://www.youtube.com/">Youtube </a><br>
                            <a href="https://www.sarkariresult.com/"> SarkariResult</a><br>
                            <a href="https://www.amazon.in/"> Amazon </a><br>
                            <a href="https://www.flipkart.com/"> Flipkart </a><br>
                            <a href="https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox"> Gmail </a><br>
                            <input type="button" value="Go back!" onclick="history.back()"><br>
                            <a href='/'>back</a>
                            ''' )

def Analyze(request):
    text = request.POST.get('text', 'default')
    removepunc = request.POST.get('RemovePunch','off')
    newlineremover = request.POST.get('NewLineRemover','off')
    fullcap = request.POST.get('FullCap','off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in text:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyze_text': analyzed}
        text = analyzed

    if fullcap == 'on':
        analyzed = ' '
        for char in text:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Full Cap', 'analyze_text': analyzed}
        text = analyzed

    if newlineremover =='on':
        analyzed = " "
        for char in text:
            if char != '\n' and char !='\r':
                analyzed = analyzed + char
        params = {'purpose': 'New Line Remover', 'analyze_text': analyzed}

    if(removepunc !='on' and fullcap !='on' and newlineremover !='on'):
        return HttpResponse("error")

    return render(request, 'analyze.html', params)


