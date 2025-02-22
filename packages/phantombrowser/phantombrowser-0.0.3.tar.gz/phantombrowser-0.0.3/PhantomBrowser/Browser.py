# -*-coding:utf8;-*-
import requests
import json as jsonpy
import os
import re
import multiprocessing
from tqdm import tqdm
from urllib.parse import urlparse, unquote, urlencode
from typing import Optional, Union, Dict, Any, List


class Browser:
    """
    Phantomjs cloud api wrapper.
    author: guangrei.
    """

    def __init__(self, apikey: Optional[str] = None) -> None:
        if apikey is None:
            apikey = os.environ.get(
                "PHANTOMJSCLOUD.COM_APIKEY", "a-demo-key-with-low-quota-per-ip-address"
            )
        userAgent: str = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Guangrei/2025.02.13 Chrome/124.0.0.0 Safari/537.36"
        self.pageRequest: Dict[str, Any] = {}
        self.verify: bool = True
        self.endpoints: str = (
            "https://phantomjscloud.com/api/browser/v2/" + apikey + "/"
        )
        self.response: Optional[bytes] = None
        self.disableJavascript: bool = False
        self.customHeaders: Dict[str, str] = {}
        self.urlSettings: Dict[str, Any] = {}
        self.requestSettings: Dict[str, Any] = {"doneWhen": [{"event": "domReady"}]}
        self.renderSettings: Dict[str, Any] = {}
        self.userAgent: str = userAgent
        self.cookies: List[str] = []
        self.session: requests.Session = requests.Session()

    def _magicRender(self, type: str) -> None:
        if type == "html":
            self.pageRequest["renderType"] = "html"
            self.requestSettings["ignoreImages"] = True
        elif type == "pdf":
            self.pageRequest["renderType"] = "pdf"
            self.requestSettings["ignoreImages"] = False
        elif type == "plainText":
            self.pageRequest["renderType"] = "plainText"
            self.requestSettings["ignoreImages"] = True
        elif type == "png":
            self.pageRequest["renderType"] = "png"
            self.requestSettings["ignoreImages"] = False
        elif type == "jpg":
            self.pageRequest["renderType"] = "jpg"
            self.requestSettings["ignoreImages"] = False
        elif type == "jpeg":
            self.pageRequest["renderType"] = "jpeg"
            self.requestSettings["ignoreImages"] = False
        else:
            raise ValueError("Not supported!")

    def _evaluate(self) -> requests.Response:
        self.requestSettings["disableJavascript"] = self.disableJavascript
        self.requestSettings["userAgent"] = self.userAgent
        self.requestSettings["cookies"] = self.cookies
        self.pageRequest["urlSettings"] = self.urlSettings
        self.pageRequest["renderSettings"] = self.renderSettings
        self.pageRequest["requestSettings"] = self.requestSettings
        response: requests.Response = self.session.post(
            self.endpoints, data=jsonpy.dumps(self.pageRequest), verify=self.verify
        )
        self.response = response.content
        return response

    def post(
        self,
        url: str,
        json: Optional[Dict[str, Any]] = None,
        data: Optional[Union[Dict[str, str], str]] = None,
        encoding: Optional[str] = None,
        headers: Dict[str, str] = {},
        render: str = "html",
        json_output: bool = False,
    ) -> requests.Response:
        self._magicRender(render)
        self.pageRequest["outputAsJson"] = json_output
        self.pageRequest["url"] = url
        self.urlSettings["operation"] = "POST"
        if json is not None:
            self.urlSettings["data"] = jsonpy.dumps(json)
            self.urlSettings["contentType"] = "application/json"
        elif json is None and data is not None:
            if isinstance(data, dict):
                self.urlSettings["data"] = urlencode(data)
                self.urlSettings["contentType"] = "application/x-www-form-urlencoded"
            elif isinstance(data, str):
                self.urlSettings["data"] = data
                self.urlSettings["contentType"] = "text/plain"
            else:
                raise TypeError
        self.urlSettings["encoding"] = encoding
        self.urlSettings["headers"] = headers
        return self._evaluate()

    def get(
        self,
        url: str,
        encoding: Optional[str] = None,
        headers: Dict[str, str] = {},
        render: str = "html",
        json_output: bool = False,
    ) -> requests.Response:
        self._magicRender(render)
        self.pageRequest["outputAsJson"] = json_output
        self.pageRequest["url"] = url
        self.urlSettings["operation"] = "GET"
        self.urlSettings["encoding"] = encoding
        self.urlSettings["headers"] = headers
        return self._evaluate()

    def put(
        self,
        url: str,
        encoding: Optional[str] = None,
        headers: Dict[str, str] = {},
        render: str = "html",
        json_output: bool = False,
    ) -> requests.Response:
        self._magicRender(render)
        self.pageRequest["outputAsJson"] = json_output
        self.pageRequest["url"] = url
        self.urlSettings["operation"] = "PUT"
        self.urlSettings["encoding"] = encoding
        self.urlSettings["headers"] = headers
        return self._evaluate()

    def patch(
        self,
        url: str,
        json: Optional[Dict[str, Any]] = None,
        data: Optional[Union[Dict[str, str], str]] = None,
        encoding: Optional[str] = None,
        headers: Dict[str, str] = {},
        render: str = "html",
        json_output: bool = False,
    ) -> requests.Response:
        self._magicRender(render)
        self.pageRequest["outputAsJson"] = json_output
        self.pageRequest["url"] = url
        self.urlSettings["operation"] = "PATCH"
        if json is not None:
            self.urlSettings["data"] = jsonpy.dumps(json)
            self.urlSettings["contentType"] = "application/json"
        elif json is None and data is not None:
            if isinstance(data, dict):
                self.urlSettings["data"] = urlencode(data)
                self.urlSettings["contentType"] = "application/x-www-form-urlencoded"
            elif isinstance(data, str):
                self.urlSettings["data"] = data
                self.urlSettings["contentType"] = "text/plain"
            else:
                raise TypeError
        self.urlSettings["encoding"] = encoding
        self.urlSettings["headers"] = headers
        return self._evaluate()

    def option(
        self,
        url: str,
        encoding: Optional[str] = None,
        headers: Dict[str, str] = {},
        render: str = "html",
        json_output: bool = False,
    ) -> requests.Response:
        self._magicRender(render)
        self.pageRequest["outputAsJson"] = json_output
        self.pageRequest["url"] = url
        self.urlSettings["operation"] = "OPTION"
        self.urlSettings["encoding"] = encoding
        self.urlSettings["headers"] = headers
        return self._evaluate()

    def delete(
        self,
        url: str,
        encoding: Optional[str] = None,
        headers: Dict[str, str] = {},
        render: str = "html",
        json_output: bool = False,
    ) -> requests.Response:
        self._magicRender(render)
        self.pageRequest["outputAsJson"] = json_output
        self.pageRequest["url"] = url
        self.urlSettings["operation"] = "DELETE"
        self.urlSettings["encoding"] = encoding
        self.urlSettings["headers"] = headers
        return self._evaluate()

    def saveAs(self, path: str, content: Optional[bytes] = None) -> bool:
        if content is not None:
            with open(path, "wb") as f:
                f.write(content)
                return True
        if self.response is not None:
            with open(path, "wb") as f:
                f.write(self.response)
                return True
        else:
            return False

    def download(
        self,
        url: str,
        folder: Optional[str] = None,
        filename: Optional[str] = None,
        overwrite: bool = False,
        progress: bool = False,
        **kwargs: Any,
    ) -> str:
        if not folder:
            folder = os.getcwd()
        ua = {"headers": {"User-Agent": self.userAgent}}
        kwargs.update(ua)

        response = self.session.get(url, stream=True, **kwargs)
        response.raise_for_status()

        if not filename:
            content_disposition = response.headers.get("content-disposition")
            if content_disposition:
                match = re.search(
                    r'filename\*?=["\']?(?:UTF-8\'\')?([^"\']+)',
                    content_disposition,
                    re.IGNORECASE,
                )
                filename = unquote(match.group(1)) if match else None
            else:
                filename = None

            if not filename:
                filename = os.path.basename(urlparse(url).path) or "downloaded_file"

        if not overwrite:
            counter = 1
            parts = filename.split(".")
            if len(parts) > 2 and parts[-2].isalnum():
                name = ".".join(parts[:-2])
                ext = "." + ".".join(parts[-2:])
            else:
                name = ".".join(parts[:-1])
                ext = "." + parts[-1]
            name = re.sub(r"\(\d+\)$", "", name)
            filename = f"{name}{ext}"
            while os.path.exists(os.path.join(folder, filename)):
                filename = f"{name}({counter}){ext}"
                counter += 1

        filepath = os.path.join(folder, filename)
        total_size = int(response.headers.get("content-length", 0))
        chunk_size = 1024  # 1 KB
        if progress:
            progress_bar = tqdm(
                total=total_size,
                unit="B",
                unit_scale=True,
                desc=filename,
            )

        with open(filepath, "wb") as file:
            for chunk in response.iter_content(chunk_size=chunk_size):
                file.write(chunk)
                if progress:
                    progress_bar.update(len(chunk))
        if progress:
            progress_bar.close()
        return filepath

    def downloader(
        self, urls: List[str], folder: str = "Downloads", **kwargs: Any
    ) -> None:
        os.makedirs(folder, exist_ok=True)
        kwargs.update(dict(progress=True, allow_redirects=True))
        process = []
        for url in urls:
            kwargs["url"] = url
            kwargs["folder"] = folder
            p = multiprocessing.Process(target=self.download, kwargs=kwargs)
            process.append(p)
            p.start()
        for p in process:
            p.join()

    def close(self) -> None:
        self.session.close()

    def __del__(self) -> None:
        self.close()
