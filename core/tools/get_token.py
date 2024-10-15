from configparser import ConfigParser


def get_token(section: str = None, token_name: str = None):
    """

    :param section: The section where you can access the token.
    :param token_name: The token which you can take from his name.
    :return: token
    """
    config = ConfigParser()
    config.read("config.ini")
    return config[section][token_name]
