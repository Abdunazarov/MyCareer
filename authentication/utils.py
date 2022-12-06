from django.core.mail import send_mail
import os

password = os.environ.get('MY_PASS')
email = os.environ.get('MY_EMAIL')


class Util:
	@staticmethod
	def send_email(data):

		send_mail(
			subject=data['email_subject'], 
			html_message=data['email_body'],
			message='',
			recipient_list=[data['to_email']],
			from_email=f"MyCareer {email}",
			auth_password='snktgjbsikpsvyal'
			)