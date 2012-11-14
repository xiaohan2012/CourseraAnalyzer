from simplejson import loads

user_info_url = "https://www.coursera.org/maestro/api/user/profile?user-id=%s"
user_topics_url = "https://www.coursera.org/maestro/api/topic/list_my?user_id=%s"
class User(dict):
    def __init__(self,sha):
        dict.__init__(self,{})
        self.sha = sha

    def _get_user_info(user_sha):
        pass

    def _get_user_topics(user_id):
        pass
