import os

def build_url(host,port):
	return f"https://{host}:{port}/healt" 

print(build_url("localhost",8000))



port = os.environ.get("PORT","8000")
print("port is",port,type(port))
