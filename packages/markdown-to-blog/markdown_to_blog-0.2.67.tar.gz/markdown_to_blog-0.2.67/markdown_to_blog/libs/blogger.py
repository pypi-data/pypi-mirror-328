import codecs
import pathlib
import shutil
from datetime import datetime, timedelta, timezone

import httplib2
from bs4 import BeautifulSoup
from configobj import ConfigObj
from googleapiclient import discovery
from loguru import logger
from markdown2 import Markdown
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run_flow

SCOPE = "https://www.googleapis.com/auth/blogger"
CREDENTIAL_STORAGE_DIR = str(pathlib.Path.home().joinpath(".md_to_blog"))
CREDENTIAL_STORAGE_PATH = str(
    pathlib.Path(CREDENTIAL_STORAGE_DIR).joinpath("credential.storage")
)
CONFIG_PATH = str(pathlib.Path(CREDENTIAL_STORAGE_DIR).joinpath("config"))
CLIENT_SECRET = pathlib.Path(CREDENTIAL_STORAGE_DIR).joinpath("client_secret.json")


def extract_article(fn):
    """
    Extracts the title and content of an article from an HTML file.

    Args:
        fn (str): The path to the HTML file.

    Returns:
        dict: A dictionary containing the extracted title and content.
            - title (str): The title of the article.
            - content (str): The HTML content of the article.

    """
    with codecs.open(fn, "r", "utf_8") as fp:
        html = fp.read()
        html = html.replace("<!doctype html>", "")
        soup = BeautifulSoup(html, "html.parser")
        title = soup.select("title")[0].text
        article = soup.select("body")[0]
        return {"title": title, "content": article.prettify()}


def authorize_credentials():
    """
    Authorizes the credentials required for accessing the specified scope.

    Returns:
        Credentials: The authorized credentials.

    """
    storage = Storage(CREDENTIAL_STORAGE_PATH)
    credentials = storage.get()
    if credentials is None or credentials.invalid:
        flow = flow_from_clientsecrets(CLIENT_SECRET, scope=SCOPE)
        http = httplib2.Http()
        credentials = run_flow(flow, storage, http=http)
    return credentials


def get_blogger_service():
    credentials = authorize_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = (
        "https://{api}.googleapis.com/$discovery/rest?" "version={apiVersion}"
    )
    return discovery.build("blogger", "v3", http=http, discoveryServiceUrl=discoveryUrl)


def validate_credential_path():
    """
    Validates the existence of the credential storage directory and file.

    """
    target_dir: pathlib.Path = pathlib.Path(CREDENTIAL_STORAGE_DIR)
    if not target_dir.exists():
        target_dir.mkdir()
    target_path: pathlib.Path = pathlib.Path(CREDENTIAL_STORAGE_PATH)
    if not target_path.exists():
        target_path.touch()


def check_config():
    target_path: pathlib.Path = pathlib.Path(CONFIG_PATH)
    if not target_path.exists():
        logger.info("config not exists. it will make new config")
        config = ConfigObj()
        config.filename = str(target_path)
        config["BLOG_ID"] = ""
        config.write()


def set_blogid(value):
    config = ConfigObj(str(pathlib.Path(CONFIG_PATH)))
    config["BLOG_ID"] = value
    config.write()


def get_blogid():
    config = ConfigObj(str(pathlib.Path(CONFIG_PATH)))
    return config["BLOG_ID"]


def set_client_secret(fn):
    shutil.copy(fn, CLIENT_SECRET)


def upload_to_blogspot(title, fn, BLOG_ID, is_draft=False, datetime_string=None) -> str:
    """
    Uploads a blog post to the specified Blogspot blog.

    Args:
        title (str): The title of the blog post.
        fn (str): The path to the Markdown file.
        BLOG_ID (str): The ID of the Blogspot blog.
        is_draft (bool, optional): Whether the post should be saved as a draft. Defaults to False.
        datetime_string (str, optional): The datetime string to set for the post. Defaults to None.

    Returns:
        str: The ID of the uploaded blog post.

    """
    validate_credential_path()
    service = get_blogger_service()
    users = service.users()
    thisuser = users.get(userId="self").execute()
    logger.info(f"""This user's display name is: {thisuser["displayName"]}""")
    posts = service.posts()
    with codecs.open(fn, "r", "utf_8") as fp:
        markdowner = Markdown(
            extras=["highlightjs-lang", "fenced-code-blocks", "html-classes", ""]
        )
        html = markdowner.convert(fp.read())
        payload = {"title": title, "content": html, "published": datetime_string}
        output = posts.insert(blogId=BLOG_ID, body=payload, isDraft=is_draft).execute()
        logger.info(f"id:{output['id']}\nstatus:{output['status']}")
        return output["id"]  # return postid


def upload_html_to_blogspot(title, fn, BLOG_ID):
    """
    Uploads an HTML file as a blog post to the specified Blogspot blog.

    Args:
        title (str): The title of the blog post.
        fn (str): The path to the HTML file.
        BLOG_ID (str): The ID of the Blogspot blog.

    """
    validate_credential_path()
    service = get_blogger_service()
    users = service.users()
    thisuser = users.get(userId="self").execute()
    logger.info(f"""This user's display name is: {thisuser["displayName"]}""")
    posts = service.posts()
    with codecs.open(fn, "r", "utf_8") as fp:
        html = fp.read()
        payload = {"title": title, "content": html}
        posts.insert(blogId=BLOG_ID, body=payload, isDraft=False).execute()


def get_datetime_after(after_string):
    """
    Returns the ISO-formatted datetime string after a specified time interval.

    Args:
        after_string (str): The time interval string.
            - "now": Returns the current datetime.
            - "1m": Returns the datetime after 1 minute.
            - "10m": Returns the datetime after 10 minutes.
            - "1h": Returns the datetime after 1 hour.
            - "1d": Returns the datetime after 1 day.
            - "1w": Returns the datetime after 1 week.
            - "1M": Returns the datetime after 1 month.

    Returns:
        str: The ISO-formatted datetime string.

    """
    seoul_timezone = timezone(timedelta(hours=9))
    current_dt = datetime.now(seoul_timezone)
    match after_string:
        case "now":
            target_dt = current_dt
        case "1m":
            target_dt = current_dt + timedelta(minutes=1)
        case "10m":
            target_dt = current_dt + timedelta(minutes=10)
        case "1h":
            target_dt = current_dt + timedelta(hours=1)
        case "1d":
            target_dt = current_dt + timedelta(days=1)
        case "1w":
            target_dt = current_dt + timedelta(days=7)
        case "1M":
            target_dt = current_dt + timedelta(days=30)
    return target_dt.isoformat(timespec="seconds")

def get_datetime_after_hour(hour):
    seoul_timezone = timezone(timedelta(hours=9))
    current_dt = datetime.now(seoul_timezone)
    target_dt = current_dt + timedelta(hours=hour)
    return target_dt.isoformat(timespec="seconds")
