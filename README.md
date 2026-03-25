# <img src="https://play-lh.googleusercontent.com/yku1SMpSGE-4oD8UrRZHzzjL8h9Hy3pevCGa3Kg9PkPHe-XXnGvof4Q3puCmV483Gj0=w480-h960-rw" width="28" style="vertical-align:middle;" /> podslyshano.py

> Mobile-API for [Podslyshano](https://podslyshano.com) a Russian anonymous secret-sharing social network where users post confessions, comment, and interact anonymously.

## Quick Start
```python
from podslyshano import Podslyshano

ps = Podslyshano()
ps.login(email="example@gmail.com", password="password")

# Post an anonymous secret
ps.post_secret(note="I secretly love pineapple on pizza")
```

---

## Authentication

| Method | Description |
|--------|-------------|
| `login(email, password)` | Sign in and store auth token |
| `register(email, password, device_type, captcha, captcha_key)` | Create a new account |
| `get_email_confirmation()` | Request email confirmation |
| `resend_confirmation()` | Resend confirmation email |
| `change_email(email)` | Change account email |

---

## Profile

| Method | Description |
|--------|-------------|
| `get_account_profile()` | Get current user's profile |
| `get_user_profile(user_id)` | Get a user's public profile |
| `edit_profile(bio, nickname, show_comments, show_likes)` | Update your profile |
| `get_categories()` | Get available post categories |

---

## Posts

| Method | Description |
|--------|-------------|
| `post_secret(note)` | Post an anonymous secret |
| `get_new_posts()` | Get latest posts |
| `get_random_posts()` | Get random posts |
| `get_best_posts()` | Get top posts of the day |
| `like_post(post_id, like_type)` | Like a post |
| `unlike_post(post_id)` | Unlike a post |
| `get_post_likes(post_id)` | Get likes on a post |

---

## Comments

| Method | Description |
|--------|-------------|
| `comment_post(post_id, text, parent_id)` | Post a comment |
| `get_post_comments(post_id)` | Get all comments on a post |
| `get_post_latest_comments(post_id)` | Get latest comments on a post |
| `get_post_best_comments(post_id)` | Get top comments on a post |
| `like_comment(comment_id)` | Like a comment |
| `unlike_comment(comment_id)` | Unlike a comment |
| `report_comment(comment_id)` | Report a comment |

---

## Bookmarks

| Method | Description |
|--------|-------------|
| `add_to_bookmarks(post_id, comment_id)` | Add a post or comment to bookmarks |
| `delete_from_bookmarks(post_id, comment_id)` | Remove from bookmarks |

---

## Users

| Method | Description |
|--------|-------------|
| `block_user(user_id)` | Block a user |
| `unblock_user(user_id)` | Unblock a user |
| `get_block_list()` | Get your block list |
| `report_user(user_id, reason)` | Report a user |
| `get_user_comments(user_id)` | Get a user's comments |
| `get_user_likes(user_id)` | Get a user's liked posts |

---

## Misc

| Method | Description |
|--------|-------------|
| `get_notifications()` | Get your activity notifications |
