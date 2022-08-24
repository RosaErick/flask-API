"""flask configuration"""


class BaseConfig:
    TESTING = False
    SECRET_KEY="change_me"
   
   

class DevelopmentConfig(BaseConfig):
    pass



class TestingConfig(BaseConfig):
   TESTING=True