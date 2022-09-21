from os import environ
import mandrill
import time
import base64
import locale
import random


def letter(name,email,template_name,subject):

    try:
        mandrill_client = mandrill.Mandrill(environ['MAIL_CHIMP_APIKEY'])
        message = {
            'from_email' : 'hola@mail.com',
            'from_name' : 'Me',
            'important' : True,
            'merge_lenguage' : 'mailchimp',
            'subject' : subject,
            'to' : [{
                'email' : email,
                'name' : name,
                'type' : 'to'
            }],
            #"global_merge_vars" : [{'name':'variable', 'content': 'something'}] #In case you need extra variables
        }
        template_content = [{'name': 'full_name', 'content': name}]
        result = mandrill_client.messages.send_template(
            template_name = template_name,
            template_content = template_content,
            message = message,
            send_async = False,
            id_pool = 'Main Pool',
            send_at = time.strftime("%x")
        )
    except mandrill.Error, e:
        print(e)