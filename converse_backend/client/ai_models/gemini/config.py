from utils.decouple_config_util import DecoupleConfigUtil


config = DecoupleConfigUtil.get_env_config()


GOOGLE_API_KEY = config("GOOGLE_API_KEY")
GEMINI_MODEL_NAME = config("GEMINI_MODEL_NAME")
