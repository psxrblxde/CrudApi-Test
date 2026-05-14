from authx import AuthXConfig, AuthX

config = AuthXConfig(
    JWT_SECRET_KEY = 'SECRET_KEY',
    JWT_ACCESS_COOKIE_NAME= 'JWT_ACCESS_COOKIE',
    JWT_ALGORITHM = 'HS256',
    JWT_TOKEN_LOCATION = ['cookies']

)

auth = AuthX(config = config)