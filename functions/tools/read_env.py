from dotenv import load_dotenv
import os


def read_env(variable):
    # Path to env file in data
    env_path = '../../data/tokens.env'

    # Load env
    load_dotenv(dotenv_path=env_path)

    # Get Variable
    return os.getenv(variable)

