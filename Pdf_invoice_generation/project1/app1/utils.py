
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


def render_to_pdf(template_src, context_dict={}):
    template =get_template(template_src)
    html= template.render(context_dict)
    response=HttpResponse(content_type ='application/pdf')
    #response['Content-Disposition'] =f"attachment; filename='{pdf_name}'"
    pdf_status =pisa.CreatePDF(html, dest=response)


    if pdf_status.err:
        return HttpResponse('some errors were encountered <pre>' +html +'</pre>')

    return response

def render_to_pdf1(template_src , context_dict={id}):
    template=get_template(template_src)
    html=template.render(context_dict)
    response=HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] =f"attachment; filename='{pdf_name}'"
    pdf_status =pisa.CreatePDF(html, dest=response)


    if pdf_status.err:
        return HttpResponse('some errors were encountered <pre>' +html +'</pre>')

    return response        