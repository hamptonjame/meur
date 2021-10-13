import serial
import time
import cherrypy
import os

class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        header = """
        <html>
	<body>
		<form method="get" action="forward">
			<button type="submit">Forward</button>
		</form>
		<form method="get" action="left">
			<button type="submit">Left</button>
		</form>
		<form method="get" action="right">
			<button type="submit">Right</button>
		</form>
		<form method="get" action="backward">
			<button type="submit">Backward</button>
		</form>
	</body>
</html>"""
        return header
    
    @cherrypy.expose
    def left(self):
        ser.write(b"left\n")
        raise cherrypy.HTTPRedirect("/index")
    
    @cherrypy.expose
    def right(self):
        ser.write(b"right\n")
        raise cherrypy.HTTPRedirect("/index")
    
    @cherrypy.expose
    def backward(self):
        ser.write(b"backward\n")
        raise cherrypy.HTTPRedirect("/index")
    
    @cherrypy.expose
    def forward(self):
        ser.write(b"forward\n")
        raise cherrypy.HTTPRedirect("/index")
        
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0',9600, timeout=1)
    ser.flush()
    time.sleep(3)

    cherrypy.quickstart(StringGenerator());