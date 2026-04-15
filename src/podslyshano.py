from requests import Session, Response

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

	def _get(self, endpoint: str) -> dict:
		return self.session.get(f"{self.api}{endpoint}").json()

	def _post(
			self,
			endpoint: str,
			data: dict = None,
			params: dict = None) -> Response:
		return self.session.post(
			f"{self.api}{endpoint}",
			data=data,
			params=params or {})

	def _put(self, endpoint: str) -> dict:
		return self.session.put(f"{self.api}{endpoint}").json()

	def _delete(self, endpoint: str) -> dict:
		return self.session.delete(f"{self.api}{endpoint}").json()

	def _filter(self, data: dict) -> dict:
		return {key: value for key, value in data.items() if value is not None}

	def login(self, email: str, password: str) -> dict:
		params = {
			"type": "email",
			"email": email,
			"password": password
		}
		response = self._post("/auth/sign_in", params=params).json()
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
		params = self._filter({
			"captcha": captcha,
			"captcha_key": captcha_key,
			"device_type": device_type,
			"type": "email",
			"email": email,
			"password": password
		})
		return self._post("/auth/sign_up", params=params).json()

	def get_account_profile(self) -> dict:
		return self._get("/profile/me").json()

	def get_new_posts(self) -> dict:
		return self._get("/posts").json()

	def get_random_posts(self) -> dict:
		return self._get("/posts/random").json()

	def get_best_posts(self) -> dict:
		return self._get("/posts/top/day").json()

	def get_categories(self) -> dict:
		return self._get("/profile/categories").json()

	def get_post_likes(self, post_id: int) -> dict:
		return self._get(f"/posts/{post_id}/likes").json()

	def add_to_bookmarks(
			self,
			post_id: int = None,
			comment_id: int = None) -> dict:
		if post_id:
			return self._post(f"/bookmarks/posts/{post_id}").json()
		return self._post(f"/bookmarks/comments/{comment_id}").json()

	def delete_from_bookmarks(
			self,
			post_id: int = None,
			comment_id: int = None) -> dict:
		if post_id:
			return self._delete(f"/bookmarks/posts/{post_id}")
		return self._delete(f"/bookmarks/comments/{comment_id}")

	def like_post(self, post_id: int, like_type: str) -> dict:
		return self._post(f"/posts/{post_id}/like?type={like_type}").json()

	def unlike_post(self, post_id: int) -> dict:
		return self._delete(f"/posts/{post_id}/like")

	def get_post_comments(self, post_id: int) -> dict:
		return self._get(f"/posts/{post_id}/comments")

	def get_post_latest_comments(self, post_id: int) -> dict:
		return self._get(f"/posts/{post_id}/comments/latest")

	def get_post_best_comments(self, post_id: int) -> dict:
		return self._get(f"/posts/{post_id}/comments/top")

	def get_email_confirmation(self) -> dict:
		return self._post("/profile/email_confirmation").json()

	def comment_post(
			self,
			post_id: int,
			text: str,
			parent_id: int = None) -> dict:
		data = {"text_fixed": text}
		if parent_id:
			data["parent_id"] = parent_id
		return self._post(f"/posts/{post_id}/comments", data).json()

	def change_email(self, email: str) -> dict:
		return self._put(f"/profile/me?user[email]={email}")

	def report_comment(self, comment_id: int) -> dict:
		return self._post(f"/comments/{comment_id}/complain").json()

	def like_comment(self, comment_id: int) -> dict:
		return self._post(f"/comments/{comment_id}/like").json()

	def unlike_comment(self, comment_id: int) -> dict:
		return self._delete(f"/comments/{comment_id}/cancel_like")

	def get_user_profile(self, user_id: int) -> dict:
		return self._get(f"/profile/{user_id}")

	def block_user(self, user_id: int) -> int:
		return self._post(f"/profile/{user_id}/ban").status_code

	def unblock_user(self, user_id: int) -> int:
		return self._post(f"/profile/{user_id}/unban").status_code

	def get_user_comments(self, user_id: int) -> dict:
		return self._get(f"/comments/for_user/{user_id}")

	def get_user_likes(self, user_id: int) -> dict:
		return self._get(f"/posts/liked?user_id={user_id}")

	def report_user(self, user_id: int, reason: str) -> dict:
		return self._post(
			f"/profile/{user_id}/complain?reason_text={reason}").json()

	def post_secret(self, note: str) -> dict:
		data = {"note": note}
		return self._post("/secrets", data).json()

	def get_notifications(self) -> dict:
		return self._get("/activities")

	def get_block_list(self) -> dict:
		return self._get("/profile/banned_users")

	def edit_profile(
			self,
			bio: str = None,
			nickname: str = None,
			show_comments: bool = False,
			show_likes: bool = True) -> dict:
		url = f"/profile/me?user[show_comments]={show_comments}&user[show_likes]={show_likes}"
		if bio:
			url += f"&user[bio]={bio}"
		if nickname:
			url += f"&user[fullname]={nickname}"
		return self._put(url)
