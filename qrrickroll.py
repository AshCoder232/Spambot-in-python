import webbrowser
import time
import random
import qrcode
def rickroller(i):
    while i < 5:

        sites = random.choice([
            'www.youtube.com/watch?v=AyOqGRjVtls',
            'youtube.com/watch?v=dQw4w9WgXcQ',
            'www.youtube.com/watch?v=w33zPsYhiCA'
        ])
        visit = "http://{}".format(sites)
        webbrowser.open(visit)
        seconds = random.randrange(5, 10)
        time.sleep(seconds)
        i+=1
i=1        
data = rickroller(i)
img = qrcode.make(visit)

qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color='red', back_color='white')
img.save('myQRcode1.png')




