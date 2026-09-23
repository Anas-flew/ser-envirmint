
# if loop :
env = "prod"

# For loop :
inver =[
	{"name":"web-01","ip":"192.168.20.1","status":"up" },
	{"name":"web-02","ip":"192.168.20.2","status":"down" },

]

print(inver[0]["name"])

# print if loop :
if env == "prod" :
	print ("be careful")
	print(["name"])
else : 
	print("safe")


# print for loop :
for i in inver :
	print(i["name"], "--->",i["ip"])

