import smtplib
import ssl
from email.message import EmailMessage


sender_email = "enter the sender gmail here"
receiver_email = "enter reciver email"
password = input("Enter a app-password: ")

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

html = """
<html>
    <body style="display: flex; justify-content:center; algin-items:center;">
    
        <div style="width:80%; height: 80%; margin:20px; ">
            <h2 style="color:red;">Hello Amir Hussein</h2>
            
            <p style="margin-top:10px; color: orange;":>this message was sent to you because of your great improvements in programming field of python :)))))</p>
            <img style="margin: 20px 0; width:300px; height: 300px; border-radius: 50%; border-color: blue;" src="https://www.letrasboom.com/thumbs/artistas/img_1644601961.jpg" />
            
            <h2 style="margin-bottom: 20px ;">for your <b style="color:blue;">Reward</b> listen to this music below :) </h2>
            <p style="margin-bottom: 20px ;">Song by Ashkan Kagan, Atour, and Hiphopologist</p>
            <a style="margin-bottom: 20px ; color: padding: 50px 20px; border-radius: 15px; " href="https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjeu5mZ88T7AhWolYsKHd5CAr0QyCl6BAgfEAM&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DyiLXNmPcEzw&usg=AOvVaw3BUN7OykPYp7rm7CHgo5AH">Listen To Nabz</a>
        </div>
        
    </body>
</html>
"""

message.add_alternative(html, subtype="html")

context = ssl.create_default_context()

print("Sending Email!")

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Success")