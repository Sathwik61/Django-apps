from django.shortcuts import render
from .models import Books
from django.http import HttpResponse
import csv
from django.template.loader import get_template
from xhtml2pdf import pisa


def home(r):
    books=Books.objects.all()
    return render(r,'index.html',{'books':books})

def booktocsv(r):
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment; filename="abc.csv"'
    writer=csv.writer(response)
    writer.writerow(['Name','Author','Publication'])
    booklist=Books.objects.all().values_list('name','author','publication')
    for book in booklist:
        writer.writerow(book)
    return response

def booktopdf(r):
    books=Books.objects.all()
    template_path='list.html'
    context={'books':books}
    response=HttpResponse(content_type="application/pdf")
    response['Content-Disposition']='attachment; filename="abc.pdf"'
    template=get_template(template_path)
    html=template.render(context)
    pisa_status=pisa.CreatePDF(html,dest=response)
    if pisa_status.err:
        return HttpResponse('<p>There is some error </p>')
    return response

