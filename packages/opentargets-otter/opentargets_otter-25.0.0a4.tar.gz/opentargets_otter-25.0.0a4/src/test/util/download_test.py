from pathlib import Path
from threading import Event
from unittest.mock import Mock, patch

import pytest

from otter.errors import DownloadError
from otter.storage.download import (
    DownloadHelper,
    GoogleSheetsDownloader,
    GoogleStorageDownloader,
    HttpDownloader,
    TaskAbortedError,
    download,
)


@pytest.fixture
def download_helper():
    return DownloadHelper()


def test_get_protocol(download_helper):
    assert download_helper._get_protocol('https://example.com') == 'https'
    assert download_helper._get_protocol('http://example.com') == 'http'
    assert download_helper._get_protocol('gs://bucket/file') == 'gs'
    assert download_helper._get_protocol('https://docs.google.com/spreadsheets/d/123') == 'google_sheets'


@patch('pis.util.download.absolute_path')
@patch('pis.util.download.check_fs')
def test_prepare_destination(mock_check_fs, mock_absolute_path, download_helper):
    mock_absolute_path.return_value = Path('/full/path')

    result = download_helper._prepare_destination('/some/path')

    assert isinstance(result, Path)
    assert str(result) == '/full/path'
    mock_check_fs.assert_called_once()


@pytest.mark.parametrize(
    ('protocol', 'downloader_class'),
    [
        ('http', HttpDownloader),
        ('https', HttpDownloader),
        ('google_sheets', GoogleSheetsDownloader),
        ('gs', GoogleStorageDownloader),
    ],
)
def test_download_strategy_selection(download_helper, protocol, downloader_class):
    with patch.object(downloader_class, 'download') as mock_download:
        download_helper._prepare_destination = Mock(return_value=Path('/downloaded/file'))
        mock_download.return_value = Path('/downloaded/file')

        result = download_helper.download(f'{protocol}://example.com', '/dst')

        assert result == Path('/downloaded/file')
        mock_download.assert_called_once()


def test_download_unknown_protocol(download_helper):
    download_helper._prepare_destination = Mock(return_value=Path('/downloaded/file'))

    with pytest.raises(DownloadError, match='unknown protocol ftp'):
        download_helper.download('ftp://example.com', '/dst')


@patch('pis.util.download.DownloadHelper.download')
def test_download_function(mock_download):
    mock_download.return_value = Path('/downloaded/file')

    result = download('https://example.com', '/dst')

    assert result == Path('/downloaded/file')
    mock_download.assert_called_once_with('https://example.com', '/dst', abort=None)


@patch('pis.util.download.requests.Session')
def test_http_downloader(mock_session, tmp_path):
    downloader = HttpDownloader()
    downloader._download = Mock()
    mock_session_instance = Mock()
    mock_session.return_value = mock_session_instance
    dst = tmp_path / 'file.txt'

    result = downloader.download('https://example.com', dst)

    assert result == dst
    mock_session_instance.mount.assert_called()


@patch('pis.util.download.open')
@patch('pis.util.download.shutil.copyfileobj')
@patch('pis.util.download.requests.Session')
def test_download_with_abort(mock_session, mock_copyfileobj, mock_open):
    downloader = HttpDownloader()
    mock_response = Mock()
    mock_session.return_value.get.return_value = mock_response
    mock_response.raise_for_status.return_value = None

    abort_event = Event()
    abort_event.set()  # Set the abort event

    mock_copyfileobj.side_effect = lambda *args: args[0].read(1, abort_event)  # Simulate reading the stream

    with pytest.raises(TaskAbortedError):
        downloader.download('https://example.com', Path('/dst'), abort=abort_event)

    mock_session.return_value.get.assert_called_once()
    mock_open.assert_called_once()
    mock_copyfileobj.assert_called_once()  # The copy should not complete due to the abort
