# coding:UTF-8

from qiniu import Auth, put_data
from own import settings


def upload_file(file_name, data):
    q = Auth(settings.QINIU_KEY, settings.QINIU_TOKEN)
    token = q.upload_token(settings.QINIU_BUCKET)
    ret, info = put_data(token, file_name, data)
    return ret['key'] == file_name


def get_download_file_url(file_name):
    """获取文件url"""
    q = Auth(settings.QINIU_KEY, settings.QINIU_TOKEN)
    base_url = 'http://%s/%s' % (settings.QINIU_HOST, file_name)
    private_url = q.private_download_url(base_url, expires=3600)
    return private_url

