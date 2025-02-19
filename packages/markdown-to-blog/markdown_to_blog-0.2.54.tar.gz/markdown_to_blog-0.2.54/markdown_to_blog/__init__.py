import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import click
from loguru import logger

from .libs.blogger import (
    check_config,
    get_blogger_service,
    get_blogid,
    get_datetime_after,
    get_datetime_after_hour,
    set_blogid,
    set_client_secret,
    upload_html_to_blogspot,
    upload_to_blogspot,
)
from .libs.click_order import CustomOrderGroup
from .libs.image_uploader import ImageUploader, get_available_services
from .libs.markdown import convert, read_first_header_from_md, upload_markdown_images


@click.command(
    cls=CustomOrderGroup,
    order=[
        "set_blogid",
        "get_blogid",
        "convert",
        "refresh_auth",
        "set_client_secret",
        "publish",
        "upload_image",
        "upload_images",
        "publish_folder",
    ],
)
def mdb():
    click.echo("markdown to blogger\nresult:\n\n")


@mdb.command("upload_image", help="이미지를 선택한 서비스에 업로드합니다.")
@click.argument("image_path", type=click.Path(exists=True))
@click.option(
    "--service",
    "-s",
    type=click.Choice(get_available_services(), case_sensitive=False),
    help="사용할 이미지 업로드 서비스. 지정하지 않으면 랜덤 선택됩니다.",
)
def run_upload_image(image_path: str, service: str = None):
    """이미지를 지정된 서비스 또는 랜덤 서비스에 업로드합니다."""
    try:
        uploader = ImageUploader(service=service)
        url = uploader.upload(image_path)
        click.echo(f"업로드 성공: {url}")
    except Exception as e:
        click.echo(f"업로드 실패: {str(e)}", err=True)
        sys.exit(1)


@mdb.command("upload_images", help="마크다운의 이미지들을 업로드합니다.")
@click.option(
    "--input", "-i", "input_", required=True, help="markdown filename to convert"
)
@click.option(
    "--service",
    "-s",
    type=click.Choice(get_available_services(), case_sensitive=False),
    help="사용할 이미지 업로드 서비스. 지정하지 않으면 랜덤 선택됩니다.",
)
def run_upload_images(input_, service: str = None):
    try:
        upload_markdown_images(input_, service=service)
        click.echo("이미지 업로드 완료")
    except Exception as e:
        click.echo(f"이미지 업로드 실패: {str(e)}", err=True)
        sys.exit(1)


@mdb.command("set_blogid", help="Set the blog ID.1")
@click.argument("blogid")
def run_set_blogid(blogid):
    check_config()
    set_blogid(blogid)


@mdb.command("get_blogid", help="show blog id")
def run_get_blogid():
    check_config()
    print(get_blogid())


@mdb.command("convert", help="마크다운 파일을 html로 변경합니다. ")
@click.option(
    "--input", "-i", "input_", required=True, help="markdown filename to convert"
)
@click.option("--output", "-o", "output_", required=True, help="html filename to save")
def run_convert(input_, output_):
    convert(input_, output_)


@mdb.command("set_client_secret", help="client_secret.json을 저장합니다.")
@click.argument("filename")
def run_set_client_secret(filename):
    set_client_secret(filename)


@mdb.command("refresh_auth", help="구글에 authentication을 refresh 합니다. ")
def run_refresh_auth():
    sys.argv[1] = "--noauth_local_webserver"
    get_blogger_service()


@mdb.command("publish", help="마크다운 파일을 blogger에 발행합니다.")
@click.option("--title", "-t", required=False, help="블로그제목", default=None)
@click.option(
    "--draft",
    "is_draft",
    flag_value=True,
    default=False,
    help="드래프트모드로 게시할지.. 이게 없으면 무조건 바로 게시다. ",
)
@click.option(
    "--after",
    "-af",
    type=click.Choice(
        ["now", "1m", "10m", "1h", "1d", "1w", "1M"], case_sensitive=True
    ),
    default=None,
    prompt=True,
    help="얼마후에 publish할 것인가?",
)
@click.option(
    "--after_hour",
    "-ah",
    type=int,
    default=None,
    help="몇시간 후에 publish할 것인가?",
)
@click.option("--blogid", "-b", default=None, help="업로드하려는 블로그 id")
@click.argument("filename")
def run_publish(title, filename, is_draft, after, after_hour, blogid):
    """Publish Markdown File filename"""
    if blogid is None:
        blog_id = get_blogid()
    else:
        blog_id = blogid

    if not title:
        title = read_first_header_from_md(filename).replace("# ", "")
        logger.info(f"title:{title}")

    datetime_string = (
        get_datetime_after_hour(after_hour)
        if after_hour is not None
        else (
            get_datetime_after(after)
            if after is not None
            else get_datetime_after("now")
        )
    )
    upload_to_blogspot(
        title, filename, blog_id, is_draft=is_draft, datetime_string=datetime_string
    )


@mdb.command("publish_html")
@click.argument("filename")
@click.option("--title", "-t", required=True, help="블로그제목")
def run_publish_html(title, filename):
    blog_id = get_blogid()
    upload_html_to_blogspot(title, filename, blog_id)


@mdb.command(
    "publish_folder", help="폴더 내의 모든 마크다운 파일을 blogger에 발행합니다."
)
@click.option("--blogid", "-b", default=None, help="업로드하려는 블로그 id")
@click.option("--interval", "-i", default=1, help="publish 간격")
@click.option(
    "--service",
    "-s",
    type=click.Choice(get_available_services(), case_sensitive=False),
    help="사용할 이미지 업로드 서비스. 지정하지 않으면 랜덤 선택됩니다.",
)
@click.argument("folder_path")
def run_publish_folder(blogid, interval, service, folder_path):
    if blogid is None:
        blog_id = get_blogid()
    else:
        blog_id = blogid

    seoul_timezone = timezone(timedelta(hours=9))
    current_dt = datetime.now(seoul_timezone)

    # folder_path 하위의 md 파일을 모두 가지고 온다. python pathlib을 사용
    file_list = Path(folder_path).glob("*.md")
    interval_cnt = 0
    for file in file_list:
        interval_cnt += 1
        target_dt = current_dt + timedelta(hours=interval * interval_cnt)
        datetime_string = target_dt.isoformat(timespec="seconds")

        # 파일의 Absolute Path를 가지고 온다.
        file_path = file.resolve()
        # 파일의 이름을 가지고 온다.
        file_name = file.name
        # 파일의 제목을 가지고 온다.
        file_title = read_first_header_from_md(file_path)

        try:
            logger.info(f"Uploading images from file: {file_name}")
            upload_markdown_images(file_path, service=service)

            logger.info(
                f"Publishing '{file_title}' to blog ID: {blog_id} at {datetime_string}"
            )
            upload_to_blogspot(
                file_title,
                file_path,
                blog_id,
                is_draft=False,
                datetime_string=datetime_string,
            )
        except Exception as e:
            logger.error(f"Error processing file {file_name}: {str(e)}")
            continue
