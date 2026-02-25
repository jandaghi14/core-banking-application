from Common.DTO.reponse import Response
from Common.Repositories.iemployee_repository import IEmployeeRepository
import hashlib
import random
import smtplib
from email.mime.text import MIMEText
import requests
from sms_ir import SmsIr

from dotenv import load_dotenv
import os
load_dotenv()


class EmployeeBusiness:
    def __init__(self, employee_repository: IEmployeeRepository):
        self.employee_repository = employee_repository

    def login(self, username, password):
        if len(username) < 3 or len(password) < 6:
            return Response(False, "Invalid data for username or password.", None)

        hash_password = hashlib.md5(password.encode()).hexdigest()
        employee = self.employee_repository.get_employee_by_username_password(username, hash_password)

        if not employee:
            return Response(False, "Invalid username or password.", None)

        if employee.status.name == 'Active':
            return Response(True, None, employee)
        elif employee.status.name == 'Pending':
            return Response(False, "your account is pending status.", None)
        elif employee.status.name == 'Deactive':
            return Response(False, "your account is deactive.", None)
    
    def register(self, firstname, lastname, username,password, email, phone):
        employee = self.employee_repository.get_employee_by_username(username)
        if employee:
            return Response(False,f'Username {employee.username} exists in database!', employee)
        
        if len(username) < 3 or len(password) < 6:
            return Response(False, "Invalid data for username or password.", None)
        
        hash_password = hashlib.md5(password.encode()).hexdigest()
        employee = self.employee_repository.insert_new_employee(firstname, lastname, username,hash_password,email, phone)
        if employee:
            return Response(True, f'Employee with username {username} added to database.',None)    
    
    def update_employee(self, employee_id, firstname, lastname ,username, email, phone, status_id, role_id  ):
        if len(username) < 3:
            return Response(False, "Invalid Username Length.", None)
        self.employee_repository.update_employee(employee_id, firstname, lastname ,username, email, phone, status_id, role_id )
        return Response(True,'Update Successfully', None)
    
    def verify_old_password(self, employee, old_password):
        hashed_old_password = hashlib.md5(old_password.encode()).hexdigest()
        if employee.password == hashed_old_password:
            return Response(True,'Old pass is verified', employee)
        return Response(False, 'Old password is incorrect', None)
    
    def generate_verify_char(self):
        verify_char = 'ABCDEFGHJKMNOPQRSTUVWXYZ'
        code = ''.join(random.choice(verify_char) for _ in range(6))
        return code
    
    
    def send_reset_code_email(self, employee):
        sender = os.getenv('EMAIL_SENDER')
        password = os.getenv("EMAIL_PASSWORD")
        to_email = employee.email
        code = self.generate_verify_char()

        msg = MIMEText(f'Your reset code is: {code}')
        msg['Subject']= 'Password Reset Code'
        msg['From'] = sender
        msg['To'] = to_email
        
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender, password)
            server.sendmail(sender,to_email, msg.as_string())
        
        return Response(True,'Code sent', code)
        
    def send_reset_code_sms(self, employee):
        API_KEY = os.getenv('API_KEY_SMS_IR_PRODUCTION')
        phone_number = employee.phone
        code = self.generate_verify_char()
        
        url = "https://api.sms.ir/v1/send/verify"

        headers = {
            "Content-Type": "application/json",
            "Accept": "text/plain",
            "x-api-key": API_KEY
        }

        payload = {
                "mobile": phone_number,       # recipient's mobile
                "templateId": 459162,         # your SMS template ID
                "parameters": [
                    {"name": "Code", "value": code},  # dynamic parameter(s) in your template
                    # you can add more parameters if your template has more placeholders
                    # {"name": "OtherParam", "value": "ValueHere"}
                ]
            }
        
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            result = response.json()
            print("Status:", result.get("status"))
            print("Message:", result.get("message"))
            print("Message ID:", result.get("data", {}).get("messageId"))
            print("Cost:", result.get("data", {}).get("cost"))
        else:
            print("Failed to send SMS. Status code:", response.status_code)
            print("Response:", response.text)
        
        
        
        
        
        
        
        # sms_ir = SmsIr(
        #             API_KEY,
        #             phone_number
        #             )
        # print(sms_ir.send_sms(phone_number,'message',phone_number))
        
        
        # return Response(True,'Code sent', code)
    
    
    
    def reset_password(self, employee, new_password):
        hashed = hashlib.md5(new_password.encode()).hexdigest()
        self.employee_repository.update_password(employee.id, hashed)
        return Response(True, 'Password is changed successfully', None)