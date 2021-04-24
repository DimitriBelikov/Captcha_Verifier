from PIL import Image, ImageFont, ImageDraw
import numpy as np
from random import randint
from generate_text import generate_captcha_text
from os import getcwd, remove
from os.path import exists

class Captcha:
	def create_blank_image(self,image_text_length, text_size):
		img_array = np.zeros(shape=(text_size*2, image_text_length*48+60, 3), dtype=np.uint8)
		
		orig_image = Image.fromarray(img_array+255)
		
		return orig_image

	def random_noise(self, blank_image):
		width, height = blank_image.size
		random_points = []
		for i in range(200):
			random_points.append((randint(5,width), randint(5,height)))
		
		return random_points

	def draw_text_image(self, blank_image, image_text, image_text_size):
		width, height = blank_image.size
		draw_obj = ImageDraw.Draw(blank_image)
		
		font = ImageFont.truetype('Rogueland Slab Bold 700.ttf', size=image_text_size)
		
		draw_obj.text(xy=(40,40), text=image_text, font=font, fill=(0,0,0))
		draw_obj.line([(0,0),(width,height), (0,height), (width,0)], fill=(0,0,0))
		draw_obj.point(xy=self.random_noise(blank_image), fill=(0,0,0))
		
	def create_captcha(self):
		image_text = generate_captcha_text()
		image_text_size = 48
		
		captcha_image = self.create_blank_image(len(image_text), image_text_size)
		self.draw_text_image(captcha_image, image_text, image_text_size)
		image_path = "static//"+ image_text + '.jpeg'
		captcha_image.save(image_path, format='jpeg')
		return image_path
	
	@staticmethod
	def delete_captcha(filename):
		filename = 'static//' + filename
		if exists(filename):
			remove(filename)
		else:
			print("The file does not exist")