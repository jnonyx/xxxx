#!C:\Users\jnony\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.9\python.exe
import cgi, os

print('content-type:text/html\r\n\r\n')

form = cgi.FieldStorage()
pn = str(form.getvalue("pname"))
des = str(form.getvalue("des"))
fle = form['filename']

fn = os.path.basename(fle.filename)
open("C:/html/" +fn, "wb").write(fle.file.read())
     
print('<html>')
print('<body>')
print('<h1>Product Name\n(%s)</h1>'%pn)
print('<img src=tem/%s>'%fn)
print('<h2>%s</h2>'%des)
print('</center></body></html>')
    
