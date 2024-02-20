from decouple import config


class Config:
    DB_URL: str = config('DB_URL')
    DB_USERNAME: str = config('DB_USERNAME')
    DB_PASSWORD: str = config('DB_PASSWORD')
    OK_MSG: str = config('OK_MSG')
    NOK_MSG: str = config('NOK_MSG')


class DbHandler:
    def connect_to_database(self):
        return f"I am connecting to {Config.DB_URL} as {Config.DB_USERNAME} with pass: {Config.DB_PASSWORD}..."

    def show_msg_when_connected(self):
        return f"{Config.OK_MSG}"

    def show_msg_when_interrputed(self):
        return f"{Config.NOK_MSG}"
