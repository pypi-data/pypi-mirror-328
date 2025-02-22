import datetime

import pytest

from scrapyloganalyzer import ScrapyLogFile
from tests import path

data_version = datetime.datetime(2020, 1, 2, 3, 4, 5)
message = "2020-01-02 03:04:05 [scrapy.utils.log] INFO message"


@pytest.mark.parametrize(
    ("files", "expected"),
    [
        # Only match.
        (
            {
                "test1.log": "2020-01-02 03:04:02 [scrapy.utils.log] INFO message",
                "test2.log": "2020-01-02 03:04:05 [scrapy.utils.log] INFO message",
            },
            ("test2.log",),
        ),
        # First match.
        (
            {
                "test1.log": "2020-01-02 03:04:03 [scrapy.utils.log] INFO message",
                "test2.log": "2020-01-02 03:04:05 [scrapy.utils.log] INFO message",
            },
            ("test1.log", "test2.log"),
        ),
        (
            {
                "test1.log": "2020-01-02 03:04:05 [scrapy.utils.log] INFO message",
                "test2.log": "2020-01-02 03:04:03 [scrapy.utils.log] INFO message",
            },
            ("test1.log", "test2.log"),
        ),
        # No match.
        ({"test1.log": "2020-01-02 03:04:06 [scrapy.utils.log] INFO message"}, None),
    ],
)
def test_find(files, expected, tmpdir):
    directory = tmpdir.mkdir("source_id")
    for filename, content in files.items():
        file = directory.join(filename)
        file.write(content)

    if expected:
        assert any(
            ScrapyLogFile.find(tmpdir, "source_id", data_version).name == directory.join(name) for name in expected
        )
    else:
        assert ScrapyLogFile.find(tmpdir, "source_id", data_version) is None


def test_find_not_existing(tmpdir):
    assert ScrapyLogFile.find(tmpdir, "source_id", data_version) is None


def test_find_not_directory(tmpdir):
    file = tmpdir.join("source_id")
    file.write(message)

    assert ScrapyLogFile.find(tmpdir, "source_id", data_version) is None


def test_find_bad_extension(tmpdir):
    directory = tmpdir.mkdir("source_id")
    file = directory.join("file.ext")
    file.write(message)

    assert ScrapyLogFile.find(tmpdir, "source_id", data_version) is None


@pytest.mark.parametrize(
    "filenames",
    [
        ("test.log",),
        ("test.log.stats",),
        ("test.log", "test.log.stats"),
    ],
)
def test_delete(filenames, tmpdir):
    for filename in filenames:
        log = tmpdir.join(filename)
        log.write("content")

    scrapy_log_file = ScrapyLogFile(tmpdir.join("test.log"))
    scrapy_log_file.delete()

    for filename in filenames:
        assert not tmpdir.join(filename).exists()


@pytest.mark.parametrize(
    ("datetime", "expected"),
    [
        (datetime.datetime(2020, 9, 2, 5, 24, 55), False),
        (datetime.datetime(2020, 9, 2, 5, 24, 56), False),
        (datetime.datetime(2020, 9, 2, 5, 24, 57), False),
        (datetime.datetime(2020, 9, 2, 5, 24, 58), True),  # exact
        (datetime.datetime(2020, 9, 2, 5, 24, 59), True),
        (datetime.datetime(2020, 9, 2, 5, 25, 0), True),
        (datetime.datetime(2020, 9, 2, 5, 25, 1), False),
    ],
)
def test_match(datetime, expected):
    assert ScrapyLogFile(path("log_error1.log")).match(datetime) is expected


@pytest.mark.parametrize(
    ("filename", "expected"),
    [
        ("log_crawl_time_spider_argument.log", datetime.datetime(2020, 1, 1, 0, 0, 0)),
        ("log_crawl_time_crawl_statistic.log", datetime.datetime(2020, 1, 1, 12, 34, 55)),
        ("log_crawl_time_log_message.log", datetime.datetime(2020, 1, 1, 12, 34, 56)),
    ],
)
def test_crawl_time(filename, expected):
    assert ScrapyLogFile(path(filename)).crawl_time == expected


@pytest.mark.parametrize(
    ("filename", "expected"),
    [
        ("log_error1.log", True),
        ("log_sample1.log", False),
        ("log_from_date1.log", True),
        ("log_sigint1.log", False),
        ("log_in_progress1.log", False),
    ],
)
def test_is_finished(filename, expected):
    assert ScrapyLogFile(path(filename)).is_finished() is expected


@pytest.mark.parametrize(
    ("filename", "files", "file_items"),
    [
        ("log1.log", 2, 0),
        ("log_error1.log", 2, 0),
        ("log_file_items.log", 0, 3),
    ],
)
def test_item_counts(filename, files, file_items):
    item_counts = ScrapyLogFile(path(filename)).item_counts
    assert item_counts["File"] == files
    assert item_counts["FileItem"] == file_items


@pytest.mark.parametrize(
    ("filename", "expected"),
    [
        ("log_error1.log", True),
        ("log_sample1.log", False),
        ("log_from_date1.log", False),
    ],
)
def test_is_complete(filename, expected):
    assert ScrapyLogFile(path(filename)).is_complete() is expected


@pytest.mark.parametrize(
    ("filename", "expected"),
    [
        (
            "log1.log",
            {
                "_job": "a38ed0e2ecdc11ea879e0c9d92c523cb",
                "compile_releases": None,
                "crawl_time": None,
                "from_date": None,
                "keep_collection_open": None,
                "note": "Started by for the use of Datasketch.",
                "package_pointer": None,
                "release_pointer": None,
                "sample": None,
                "truncate": None,
                "until_date": None,
            },
        ),
        (
            "log_sample1.log",
            {
                "compile_releases": None,
                "crawl_time": None,
                "from_date": None,
                "keep_collection_open": None,
                "note": None,
                "package_pointer": None,
                "release_pointer": None,
                "sample": "1",
                "truncate": None,
                "until_date": None,
            },
        ),
    ],
)
def test_spider_arguments(filename, expected):
    assert ScrapyLogFile(path(filename)).spider_arguments == expected


@pytest.mark.parametrize(
    ("filename", "expected"),
    [
        ("log1.log", 0),
        ("log_file_items.log", 0),
        ("log_error_no_data.log", 1),
        ("log_no_file_error_no_data.log", 1),
        ("log_error1.log", 0.33),
        ("log_error_invalid_json.log", 0.82),
    ],
)
def test_error_rate(filename, expected):
    assert round(ScrapyLogFile(path(filename)).error_rate, 2) == expected
