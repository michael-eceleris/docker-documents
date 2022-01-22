import pdfkit as pdf
from jinja2 import FileSystemLoader, Environment, Template

def generatePdfFromJinja(name):
    loader = FileSystemLoader(searchpath="./")
    env = Environment(loader=loader)
    template_file = name + ".html"
    t = env.get_template(template_file)
    format_html = t.render(
        sucursal="26", 
        ramo="21", 
        poliza="C-9159", 
        day="27", 
        month="10", 
        year="2022", 
        individual_certified_number = "SA-00000000000",
        client="jorge enrique ramírez gómez", 
        nit="1016053187", 
        address="Cl 99 No.14– 09",
        phone="3107792390",
        city="bogotá",
        email="jr_981@hotmail.com",
        brand="motorola",
        model="one fusion 128gb",
        imei="353596117148320",
        insured_value="288.500",
        bonus_value="8.500",
        iva="850",
        value_total="9.000",
        day_present="18",
        month_present="octubre",
        year_present="2021",
        typeEvent="hurto calificado",
        numberEvent="123"
    )
    
    options = {
        'margin-top': '0.71in',
        'margin-right': '0.15in',
        'margin-bottom': '0.10in',
        'margin-left': '0.15in',
    } 
  
    pdf.from_string(format_html, name + '.pdf', options=options);

generatePdfFromJinja("certificado_todo_riesgo")

#options formato traspaso
""" options = {
        'page-size': 'Letter'
    } """

#options orden de compra 
""" options = {
        'margin-top': '0.4in',
        'margin-right': '0.3in',
        'margin-bottom': '0.40in',
        'margin-left': '0.3in',
    } """


#options para la orden de ingreso
""" options = {
        'margin-top': '0.22in',
        'margin-right': '0.40in',
        'margin-bottom': '0.40in',
        'margin-left': '0.40in',
    } """

#options para la carta de rechazo
"""  options = {
        'margin-top': '1.65in',
        'margin-right': '0.44in',
        'margin-bottom': '1.65in',
        'margin-left': '0.4in',
        'header-html': 'header.html',
        'footer-html': 'footer.html'
    }  """
#options certificados de seguro total y fractura pantalla
""" options = {
        'margin-top': '0.71in',
        'margin-right': '0.15in',
        'margin-bottom': '0.10in',
        'margin-left': '0.15in',
    } """

#options para orden reparacion
"""  options = {
        'margin-top': '0.25in',
        'margin-right': '0.28in',
        'margin-bottom': '0.3in',
        'margin-left': '0.30in',
    }  """