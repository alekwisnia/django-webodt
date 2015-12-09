# -*- coding: utf-8 -*-
import os
import hashlib
from webodt.conf import WEBODT_CACHE_DIR
from django.conf import settings
from webodt import Document


class CacheManager(object):

    def __init__(self):
        if not os.path.isdir(WEBODT_CACHE_DIR):
            os.makedirs(WEBODT_CACHE_DIR)

    def get(self, odf_document, format):
        filename = self.get_filename(odf_document, format)
        if os.path.isfile(filename):
            return Document(filename, delete_on_close=False)
        return None

    def set(self, odf_document, format, document):
        filename = self.get_filename(odf_document, format)
        with open(filename, 'w') as fd:
            document.seek(0)
            fd.write(document.read())

    def delete(self, odf_document, format):
        filename = self.get_filename(odf_document, format)
        if os.path.isfile(filename):
            os.unlink(filename)

    def get_filename(self, odf_document, format):
        sha1 = hashlib.new('sha1')
        odf_document.seek(0)
        odf_data = odf_document.read()
        sha1.update(odf_data)
        odf_document.seek(0)
        sha1.update(format)
        sha1.update(settings.SECRET_KEY.encode('utf-8'))
        digest = sha1.hexdigest()
        filename = os.path.join(WEBODT_CACHE_DIR, '%s.%s' % (digest, format))
        return filename

    def clear(self):
        for filename in os.listdir(WEBODT_CACHE_DIR):
            path = os.path.join(WEBODT_CACHE_DIR, filename)
            if os.path.isfile(path):
                os.unlink(path)
