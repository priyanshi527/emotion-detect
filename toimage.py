import base64
#from firebase import Firebase

#file = open('hello2.bin', 'rb')
#byte = file.read()
#string = byte[22:]

  
decodeit = open('hello_future.jpeg', 'wb')
decodeit.write(base64.b64decode((byte)))
decodeit.close()