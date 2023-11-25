import aiml
kernel = aiml.Kernel()
kernel.learn("C:\\Users\\L05-26\\Desktop\\ai\\basic_chat.aiml")
kernel.learn("C:\\Users\\L05-26\\Desktop\\ai\\std-startup.xml")
kernel.respond("LOAD")
while True:
    print(kernel.respond(input("Enter your message>>")))
             
