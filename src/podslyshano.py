from requests import Session

class Podslyshano:
    def __init__(self) -> None:
        self.api = "https://podslyshano.com/api/v3.3"
        self.session = Session()
        self.session.headers = {
            "User-Agent": "okhttp/4.9.1",
            "X-Client-Version": "and3.3.2.2",
            "Connection": "Keep-Alive"
        }
        self.user_id = None
        self.auth_token = None

    def login(self, email: str, password: str) -> dict:
        response = self.session.post(
            f"{self.api}/auth/sign_in?type=email&email={email}&password={password}").json()
        if "user" in response:
            self.user_id = response["user"]["id"]
            self.auth_token = response["user"]["auth_token"]
            self.session.headers["Authorization"] = self.auth_token
        return response

    def register(
            self,
            email: str,
            password: str,
            device_type: str = "android",
            captcha: str = None,
            captcha_key: str = None) -> dict:
        params = {
            "captcha": captcha,
            "captcha_key": captcha_key
        }
        filtered_params = {
            key: value for key, value in params.items() if value is not None
        }
        return self.session.post(
            f"{self.api}/auth/sign_up?device_type={device_type}&type=email&email={email}&password={password}",
            params=filtered_params).json()

    def get_account_profile(self) -> dict:
        return self.session.get( f"{self.api}/profile/me").json()

    def get_new_posts(self) -> dict:
        return self.session.get(f"{self.api}/posts").json()

    def get_random_posts(self) -> dict:
        return self.session.get(f"{self.api}/posts/random").json()

    def get_best_posts(self) -> dict:
        return self.session.get(f"{self.api}/posts/top/day").json()

    def get_categories(self) -> dict:
        return self.session.get(
            f"{self.api}/profile/categories").json()

    def get_post_likes(self, post_id: int) -> dict:
        return self.session.get(
            f"{self.api}/posts/{post_id}/likes").json()

    def add_to_bookmarks(
            self,
            post_id: int = None,
            comment_id: int = None) -> dict:
        return self.session.post(
            f"{self.api}/bookmarks/posts/{post_id}" if post_id else f"{self.api}/bookmarks/comments/{comment_id}").json()

    def delete_from_bookmarks(
            self,
            post_id: int = None,
            comment_id: int = None) -> dict:
        return self.session.delete(
            f"{self.api}/bookmarks/posts/{post_id}" if post_id else f"{self.api}/bookmarks/comments/{comment_id}").json()

    def like_post(
            self,
            post_id: int,
            type: str) -> dict:
        return self.session.post(
            f"{self.api}/posts/{post_id}/like?type={type}").json()

    def unlike_post(self, post_id: int) -> dict:
        return self.session.delete(
            f"{self.api}/posts/{post_id}/like").json()

    def get_post_comments(self, post_id: int) -> dict:
        return self.session.get(
            f"{self.api}/posts/{post_id}/comments").json()

    def get_post_latest_comments(self, post_id: int) -> dict:
        return self.session.get(
            f"{self.api}/posts/{post_id}/comments/latest").json()

    def get_post_best_comments(self, post_id: int) -> dict:
        return self.session.get(
            f"{self.api}/posts/{post_id}/comments/top").json()

    def get_email_confirmation(self) -> dict:
        return self.session.post(
            f"{self.api}/profile/email_confirmation").json()

    def comment_post(
            self,
            post_id: int,
            text: str,
            parent_id: int = None) -> dict:
        data = {
            "text_fixed": text
        }
        if parent_id:
            data["parent_id"] = parent_id
        return self.session.post(
            f"{self.api}/posts/{post_id}/comments",
            data=data).json()

    def change_email(self, email: str) -> dict:
        return self.session.put(
            f"{self.api}/profile/me?user[email]={email}").json()

    def report_comment(self, comment_id: int) -> dict:
        return self.session.post(
            f"{self.api}/comments/{comment_id}/complain").json()

    def like_comment(self, comment_id: int) -> dict:
        return self.session.post(
            f"{self.api}/comments/{comment_id}/like").json()

    def unlike_comment(self) -> dict:
        return self.session.delete(
            f"{self.api}/comments/{comment_id}/cancel_like").json()

    def get_user_profile(self, user_id: int) -> dict:
        return self.session.get(
            f"{self.api}/profile/{user_id}").json()

    def block_user(self, user_id: int) -> int:
        return self.session.post(
            f"{self.api}/profile/{user_id}/ban").status_code

    def unblock_user(self, user_id: int) -> int:
        return self.session.post(
            f"{self.api}/profile/{user_id}/unban").status_code

    def get_user_comments(self, user_id: int) -> dict:
        return self.session.get(
            f"{self.api}/comments/for_user/{user_id}").json()

    def get_user_likes(self, user_id: int) -> dict:
        return self.session.get(
            f"{self.api}/posts/liked?user_id={user_id}").json()

    def report_user(self, user_id: int, reason: str) -> dict:
        return self.session.post(
            f"{self.api}/profile/{user_id}/complain?reason_text={reason}").json()

    def post_secret(self, note: str) -> dict:
        data = {
            "note": note
        }
        return self.session.post(
            f"{self.api}/secrets", data=data).json()

    def get_notifications(self) -> dict:
        return self.session.get(f"{self.api}/activities").json()

    def get_block_list(self) -> dict:
        return self.session.get(
            f"{self.api}/profile/banned_users").json()

    def edit_profile(
            self,
            bio: str = None,
            nickname: str = None,
            show_comments: bool = False,
            show_likes: bool = True) -> dict:
        url = f"{self.api}/profile/me?user[show_comments]={show_comments}&user[show_likes]={show_likes}"
        if bio:
            url += f"&user[bio]={bio}"
        if nickname:
            url += f"&user[fullname]={nickname}"
        return self.session.put(url).json()
