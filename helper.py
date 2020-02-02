import os
import re
import numpy as np
import email
import email.policy
from html import unescape


SPAM_PATH = os.path.join("datasets", "spam")

def load_email(dir_name, filename, spam_path=SPAM_PATH):
	with open(os.path.join(spam_path, dir_name, filename), 'rb') as f:
		return email.parser.BytesParser(policy=email.policy.default).parse(f)

def get_dataset(dir_path, dir_class):
	X = []
	y = []
	for dir_name, c in dir_class:
		path = os.path.join(dir_path, dir_name)
		filenames = [name for name in os.listdir(path) if len(name) > 20]
		emails = [load_email(dir_name=dir_name, filename=name, spam_path=dir_path) for name in filenames]
		X += emails
		y += [c] * len(emails)
	return np.array(X), np.array(y)		

def html_to_plain_text(html):
    text = re.sub('<head.*?>.*?</head>', '', html, flags=re.M | re.S | re.I)
    text = re.sub('<a\s.*?>', ' HYPERLINK ', text, flags=re.M | re.S | re.I)
    text = re.sub('<.*?>', '', text, flags=re.M | re.S)
    text = re.sub(r'(\s*\n)+', '\n', text, flags=re.M | re.S)
    return unescape(text)

def email_to_text(email):
	html = None
	for part in email.walk():
		ctype = part.get_content_type()
		if not ctype in ("text/html", "text/plain"):
			continue
		try:
			content = part.get_content()
		except:
			content = str(part.get_payload())
		if ctype == "text/plain":
			return content
		else:
			html = content
	if html:
		return html_to_plain_text(html)


names_class = [
	("easy_ham", False),
	("hard_ham", False),
	("spam", True),
	("08", True),
	("09", True),
	("10", True)
]

def get_data():
	X, y = get_dataset(SPAM_PATH, names_class)
	X_text = [email_to_text(email) for email in X]
	return X_text, y


