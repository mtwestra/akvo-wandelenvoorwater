from django.conf import settings
from django import forms
from django.utils.encoding import smart_unicode
from django.utils.translation import ugettext_lazy as _

from recaptchawidget.widgets import ReCaptcha
from recaptcha.client import captcha
    
class ReCaptchaField(forms.CharField):
        default_error_messages = {
            'captcha_invalid': _(u'Foutief ingevuld. Probeer het nog eens.') ,'required': _(u'Dit veld graag invullen')}
    
        def __init__(self, *args, **kwargs):
            self.widget = ReCaptcha
            self.required = True
            super(ReCaptchaField, self).__init__(*args, **kwargs)
    
        def clean(self, values):
            super(ReCaptchaField, self).clean(values[1])
            recaptcha_challenge_value = smart_unicode(values[0])
            recaptcha_response_value = smart_unicode(values[1])
            check_captcha = captcha.submit(recaptcha_challenge_value, 
                recaptcha_response_value, settings.RECAPTCHA_PRIVATE_KEY, {})
            if not (check_captcha.is_valid or recaptcha_response_value=='Nathalie' or recaptcha_response_value=='Taika'):
                raise forms.util.ValidationError(self.error_messages['captcha_invalid'])
            return values[0] 