import qrcode
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.pagesizes import A4

qr = qrcode.QRCode(
    version=2, # 1 to 40: controls the size of the QR Code; 1 is smallest
    error_correction=qrcode.constants.ERROR_CORRECT_Q,
    box_size=10, # how many pixels each “box” of the QR code is
    border=4, # how many boxes thick the border should be (the default is 4, which is the minimum according to the specs)
)

# Create a pdf object
pdf = canvas.Canvas("sample.pdf")
pdf.setPageSize(size=A4)
# Title
pdfmetrics.registerFont(TTFont('abc', 'Calibri.ttf'))
pdf.setFont('abc', 18)
pdf.drawCentredString(210*mm / 2, (297 - 15)*mm, "Dericole Feathers")

x_start = int(round(20*mm))
x_end = int(round((210 - 24)*mm))
x_interval = int(round(21*mm))
x_offset = 2
y_start = int(round((297 - 10)*mm))
y_end = int(round(15*mm))
y_interval = int(round(24*mm))
y_offset = -y_end - 28*mm

qr_width = 20*mm

# Draw QRs
pdf.setFont('abc', 10)
indx = 1
for y in range(y_end, y_start - y_interval, y_interval):
    for x in range(x_start, x_end, x_interval):
        txt = "O26D{0}".format(indx)
        qr.clear()
        qr.add_data(txt)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        pdf.drawInlineImage(image=img, x=x+x_offset, y=y+y_offset, width=qr_width, preserveAspectRatio=True)
        pdf.drawString(x+7, y+12, txt)
        indx += 1

# Draw grid
xlist = []
for x in range(x_start, x_end+x_interval, x_interval):
    xlist.append(x)
ylist = []
for y in range(y_end, y_start, y_interval):
    ylist.append(y)
pdf.grid(xlist, ylist)

pdf.save()