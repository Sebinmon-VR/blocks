from reportlab.pdfgen import canvas

c = canvas.Canvas("samples/sample.pdf")
c.drawString(100, 750, "Hello, this is a sample PDF file.")
c.drawString(100, 730, "It only has a few lines of text.")
c.save()
print("PDF created")
