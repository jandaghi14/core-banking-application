from tkinter import Label, Entry, Button,Frame
import random
import string
from PIL import Image, ImageDraw, ImageFont, ImageTk


class CaptchaComponent(Frame):
    def __init__(self,parent):
        super().__init__(parent)
        
        self.characters = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"
        self.captcha_text= self.generate_captcha_text()
        self.grid_columnconfigure(0,weight=1)
        
        self.image_lable= Label(self)
        self.image_lable.grid(row=0,column=0,padx=5)

        self.captcha_entry = Entry(self,width=20)
        self.captcha_entry.grid(row=0,column=1,padx=5)

        self.refresh_button= Button(self, text='Refresh', command=self.refresh_captcha)
        self.refresh_button.grid(row=0,column=2)
        
        self.display_captcha()
        
    def generate_captcha_text(self):
        return ''.join(random.choice(self.characters) for _ in range(6))

    
    def create_captcha_image(self):
        width=150
        height=50
        # ===========
        bg_color = (random.randint(200, 255), random.randint(200,255),random.randint(200,255))
        image = Image.new('RGB', (width,height),bg_color)
        # ===========
        
        draw= ImageDraw.Draw(image)

        try:
            font= ImageFont.truetype('arial.ttf', 40)
        except:
            font= ImageFont.load_default()
            
        #  Calculate Text Position (CENTER IT)
        text= self.captcha_text
        bbox= draw.textbbox((0,0), text, font=font,font_size=5)
        text_width = bbox[2] - bbox[0]
        text_height= bbox[3] - bbox[1]
        
        
        
        x = (width - text_width) //2
        y=(height - text_height) //2-10
        
        
        text_color = (random.randint(0, 100), random.randint(0, 100), random.randint(0, 100))
        draw.text((x, y), text, fill=text_color, font=font)
        
        # Add some noise lines for security
        for _ in range(5):
            line_color = (random.randint(100, 200), random.randint(100, 200), random.randint(100, 200))
            x1 = random.randint(0, width)
            y1 = random.randint(0, height)
            x2 = random.randint(0, width)
            y2 = random.randint(0, height)
            draw.line([(x1, y1), (x2, y2)], fill=line_color, width=2)
        
        return image

    def display_captcha(self):
        pil_image= self.create_captcha_image()
        self.photo_image= ImageTk.PhotoImage(pil_image)
        self.image_lable.config(image=self.photo_image)
    
    def refresh_captcha(self):
        self.captcha_text= self.generate_captcha_text()
        self.captcha_entry.delete(0,'end')
        self.display_captcha()
        print(f"New CAPTCHA: {self.captcha_text}")

    def validate(self):
        user_input= self.captcha_entry.get().upper()
        return user_input == self.captcha_text
    
    def get_user_input(self):
        return self.captcha_entry.get()
    
    def clear_input(self):
        self.captcha_entry.delete(0,'end')









