import jwt,time
from config import configs

config = configs.get('development')


def get_default_payload(uid,username,group):
    payload = {
        'exp': int(time.time()+86400),
        'iat':int(time.time()),
        'iss':'Li',
        'data':{
            'uid':uid,
            'name':username,
            'group':group
        }
    }
    return payload

class Auth():
    @staticmethod
    def encode_token(uid,username,group):
        '''
        生成认证Token
        :param uid: int
        :param username: string
        :return:string
        '''
        try:
            return str(jwt.encode(key=config.SECRET_KEY,payload=get_default_payload(uid,username,group)).decode('utf-8'))
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
            return 'Token解析错误！'

