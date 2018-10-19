import jwt,time
from config import configs

config = configs.get('development')


def get_default_payload(uid,username):
    payload = {
        'exp': int(time.time()+86400),
        'iat':int(time.time()),
        'iss':'Li',
        'data':{
            'uid':uid,
            'name':username
        }
    }
    return payload

class Auth():
    @staticmethod
    def encode_token(uid,username):
        '''
        生成认证Token
        :param uid: int
        :param username: string
        :return:string
        '''
        try:
            return str(jwt.encode(key=config.SECRET_KEY,payload=get_default_payload(uid,username)).decode('utf-8'))
        except Exception as e:
            return e

    @staticmethod
    def decode_token(token):
        '''
        验证Token
        :param token:string
        :return:
        '''
        try:
            return jwt.decode(token,config.SECRET_KEY)
        except:
            return '发生未知错误！'

