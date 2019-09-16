import json
import requests
from flask import current_app
from flask_babel import _


def translate(text, source_language, dest_language):
    if 'YANDEX_TRANSLATE_API' not in current_app.config or \
            not current_app.config['YANDEX_TRANSLATE_API']:
        return _('Error: the translation service is not configured.')
    key = current_app.config['YANDEX_TRANSLATE_API']
    r = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate?text={}&lang={}-{}&key={}'.format(
                         text, source_language, dest_language, key))
    if r.status_code != 200:
        return _('Error: the translation service failed.')
    return json.loads(r.content.decode('utf-8-sig')).get('text')[0]
