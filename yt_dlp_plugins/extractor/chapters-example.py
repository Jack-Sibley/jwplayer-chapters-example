from yt_dlp.extractor.common import InfoExtractor
from yt_dlp.YoutubeDL import YoutubeDL
from yt_dlp.utils import (
    urljoin
)


class ChaptersExampleIE(InfoExtractor):
    _VALID_URL = r'https://jwplayer-chapters-example.vercel.app'

    def _real_extract(self, url):
        video_id = 'steamboat'
        data_url = urljoin(url, 'data.json')
        data = self._download_json(data_url, video_id)

        

        return self._parse_jwplayer_data(data, video_id)
