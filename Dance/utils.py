from instagrapi import Client

class Instagram:
    def __init__(self):
        self.cl = Client()
        self.cl.login('_thecloud_13', 'Myvhub@123')

    def get_all_posts(self,username):
        user_id = self.cl.user_id_from_username(username)
        medias = self.cl.user_medias(user_id, 40)
        posts = []
        for media in medias:
            temp = dict(media)
            data = {
                "media_type":temp['media_type'],
                "shortcode":temp['code'],
                "thumbnail":temp['thumbnail_url'],
                "user": dict(temp['user']),
                "comments":temp.get('comment_count'),
                "likes":temp.get('like_count'),
                "views": temp.get('play_count') if temp.get('play_count') else temp.get('view_count'),
                "video_url":temp.get("video_url")
            }
            posts.append(data)
        return posts