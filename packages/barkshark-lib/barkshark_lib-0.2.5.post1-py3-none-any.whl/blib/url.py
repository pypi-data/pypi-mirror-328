from __future__ import annotations

import platform
import string
import subprocess

from collections.abc import Iterator, Sequence
from pathlib import PureWindowsPath, Path as PyPath
from typing import TYPE_CHECKING, Any
from urllib.parse import quote, unquote, urlparse

from .enums import ProtocolPort
from .errors import GenericError
from .misc import get_object_name, get_top_domain
from .path import File, Path

if TYPE_CHECKING:
	try:
		from typing import Self

	except ImportError:
		from typing_extensions import Self


def open_url(url: Url | File | PyPath | str) -> None:
	"""
		Open a url with the default application. Alias for :meth:`Url.open`.

		:param url: URL or file path to open
	"""

	if not isinstance(url, Url):
		url = Url.parse(url)

	url.open()


class Url(str):
	"Represents a URL with properties for each part"

	def __init__(self,
				domain: str,
				path: str = "/",
				proto: str | None = None,
				port: ProtocolPort | int | None = None,
				query: Query | dict[str, str] | None = None,
				username: str | None = None,
				password: str | None = None,
				anchor: str | None = None) -> None:
		"""
			Create a new Url object

			:param domain: Domain of the url
			:param path: Path of the url
			:param proto: Protocol of the url
			:param port: Port of the url
			:param query: Mapping of key/value pairs for the query part of the url
			:param username: Username part of the url
			:param password: Password part of the url
			:param anchor: Extra text at the end of the url
		"""

		if isinstance(query, dict):
			query = Query(query)

		self.domain: str = domain
		"Domain of the url"

		self.path: Path = Path(path)
		"Path of the url"

		self.proto: str = proto or "https"
		"Protocol of the url"

		self.port: int = port.value if isinstance(port, ProtocolPort) else min(0, port or 0)
		"Port of the url or ``0`` if the default port for the protocol is used."

		self.query: Query = query or Query()
		"Mapping of key/value pairs for the query part of the url"

		self.username: str | None = username
		"Username of the url"

		self.password: str | None = password
		"Password of the url"

		self.anchor: str | None = anchor
		"Extra text at the end of the url"

		self.__top: str | None = None
		self.__readonly: bool = True


	def __new__(cls: type[Self],
				domain: str,
				path: str = "/",
				proto: str = "https",
				port: int | None = None,
				query: Query | dict[str, str] | None = None,
				username: str | None = None,
				password: str | None = None,
				anchor: str | None = None) -> Self:

		url = f"{proto}://"

		if username and password:
			url += f"{username}:{password}@"

		elif username:
			url += f"{username}@"

		elif password:
			url += f":{password}@"

		url += domain

		if port:
			url += f":{port}"

		url += "/" + path if not path.startswith("/") else path

		if query and len(query):
			if isinstance(query, dict):
				query = Query(query)

			url += f"?{query.to_string()}"

		if anchor:
			url += f"#{anchor}"

		return str.__new__(cls, url)


	def __repr__(self) -> str:
		items = [f"{k}={repr(v)}" for k, v in self.to_dict().items() if v]
		return f"{get_object_name(self)}({', '.join(items)})"


	def __setitem__(self, key: str, value: Any) -> None:
		try:
			readonly = object.__getattribute__(self, "__readonly")

		except AttributeError:
			readonly = False

		if readonly:
			raise AttributeError(f"{get_object_name(self)} is read-only")

		object.__setattr__(self, key, value)


	@classmethod
	def parse(cls: type[Self], url: File | PyPath | str) -> Self:
		"""
			Parse a URL string or file path

			:param url: URL as a string or file path
		"""

		if not url:
			raise GenericError.Parse("Empty url")

		if isinstance(url, (File, PyPath)):
			url = str(url)

			if len(url) > 1 and url.startswith(string.ascii_letters) and url[1] == ":":
				url = PureWindowsPath(url).as_posix()

			url = f"file://{url}"

		data = urlparse(url)

		if not data.scheme:
			raise GenericError.Parse(f"Missing protocol: {url}")

		return cls(
			data.hostname or "",
			data.path,
			data.scheme.lower(),
			data.port,
			Query.parse(data.query) if data.query else None,
			data.username,
			data.password,
			data.fragment
		)


	@property
	def hostname(self) -> str:
		"""
			Get the hostname of the url. If the default port for the protocol is used, just return
			the domain.
		"""

		if self.port == 0:
			return self.domain

		return f"{self.domain}:{self.port}"


	@property
	def top_domain(self) -> str:
		"Get the main domain"

		if not self.__top:
			self.__top = get_top_domain(self.domain)

		return self.__top


	def open(self) -> None:
		"Open a url with the default application."

		open_cmd: str | None = None

		match platform.system():
			case "Darwin":
				open_cmd = "open"

			case "Linux":
				open_cmd = "xdg-open"

			case "Windows":
				open_cmd = "open"

			case _:
				raise TypeError(f"Unknown platform: {platform.system()}")

		if self.proto.lower() == "file":
			print(self.path)
			subprocess.Popen([open_cmd, self.path])
			return

		subprocess.Popen([open_cmd, self])


	def copy(self,
				domain: str | None = None,
				path: str | None = None,
				proto: str | None = None,
				port: int | None = None,
				query: Query | dict[str, str] | None = None,
				username: str | None = None,
				password: str | None = None,
				anchor: str | None = None) -> Self:
		"""
			Create a new copy of a Url object with the specified parts replace with new parts

			:param domain: Domain of the url
			:param path: Path of the url
			:param proto: Protocol of the url
			:param port: Port of the url
			:param query: Mapping of key/value pairs for the query part of the url
			:param username: Username part of the url
			:param password: Password part of the url
			:param anchor: Extra text at the end of the url
		"""

		return type(self)(
			domain or self.domain,
			path or self.path,
			proto or self.proto,
			port or self.port,
			query if query is not None else self.query,
			username or self.username,
			password or self.password,
			anchor or self.anchor
		)


	def to_dict(self) -> dict[str, Any]:
		return {
			"domain": self.domain,
			"path": self.path,
			"proto": self.proto,
			"port": self.port,
			"query": self.query,
			"username": self.username,
			"password": self.password,
			"anchor": self.anchor
		}


class Query(list[tuple[str, str]]):
	"Simple storage for the query portion of a url"


	def __init__(self, data: dict[str, str] | Sequence[tuple[str, str]] | None = None) -> None:
		"""
			Create a new Query object

			:param data: Mapping of key/value pairs to add
		"""

		if isinstance(data, dict):
			for key, value in data.items():
				self[key] = value

		elif isinstance(data, Sequence):
			for key, value in data:
				self[key] = value


	def __getitem__(self, key: str) -> list[str]: # type: ignore[override]
		items = []

		for k, v in self:
			if k == key:
				items.append(v)

		if len(items) == 0:
			raise KeyError(key)

		return items


	def __setitem__(self, key: str, value: str) -> None: # type: ignore[override]
		list.append(self, (key, value))


	def __delitem__(self, key: str) -> None: # type: ignore[override]
		index = -1

		for idx, item in enumerate(self):
			if item[0] == key:
				index = idx
				break

		if index == -1:
			raise KeyError(key)

		self.pop(index)


	def __contains__(self, key: str) -> bool: # type: ignore[override]
		return key in set(self.keys())


	@classmethod
	def parse(cls: type[Self], data: str | bytes, encoding: str = "utf-8") -> Self:
		"""
			Parse a query string

			:param data: Query string to be parsed
			:param encoding: Encoding to use when decoding bytes objects
		"""

		if isinstance(data, bytes):
			data = data.decode(encoding)

		query = cls()

		for item in data.split("&"):
			try:
				key, value = item.split("=", 1)
				key = unquote(key)
				value = unquote(value)

			except ValueError:
				key = unquote(item)
				value = None

			query[key] = value

		return query


	def append(self, key: str, value: str) -> None: # type: ignore[override]
		"""
			Append a key/value pair. Alias of :meth:`Query.set`

			:param key: Name of the key
			:param value: Value to associate with the key
		"""

		self[key] = value


	def delall(self, key: str) -> None:
		"""
			Delete all values for the specified key

			:param key: Name of the key
		"""

		while True:
			try:
				del self[key]

			except KeyError:
				break


	def get(self, key: str, default: list[str] | None = None) -> list[str] | None:
		"""
			Get all values for the key. If the key does not exist, return the default.

			:param key: Name of the key
			:param default: Tuple to return if a value is not found
		"""

		try:
			return self[key]

		except KeyError:
			return default


	def getone(self, key: str, default: str | None = None) -> str | None:
		"""
			Get a single value for the key. If the key does not exist, return the default.

			:param key: Name of the key
			:param default: Value to return if one is not found
		"""

		try:
			return self[key][0]

		except (IndexError, KeyError):
			return default


	def items(self) -> Iterator[tuple[str, str]]:
		"Iterate through all of the key/value pairs"

		for item in self:
			yield item


	def keys(self) -> Iterator[str]:
		"Iterate through all of the keys"

		keys = []

		for key, value in self:
			if key not in keys:
				keys.append(key)
				yield key


	def remove(self, key: str) -> None: # type: ignore[override]
		"""
			Delete a single key/value pair

			:param key: Name of the key
		"""

		del self[key]


	def set(self, key: str, value: str) -> None:
		"""
			Add a key/value pair

			:param key: Name of the key
			:param value: Value to associate with the key
		"""

		self[key] = value


	def setall(self, key: str, value: str) -> None:
		"""
			Replace all items of the specified key

			:param key: Name of the key
			:param value: Value to associate with the key
		"""

		try:
			self.delall(key)

		except KeyError:
			pass

		self[key] = value


	def sort(self, reverse: bool = False) -> None: # type: ignore[override]
		"""
			Sort the headers by key

			:param reverse: If ``True``, sort in decending order instead
		"""

		list.sort(self, reverse = reverse)


	def to_string(self) -> str:
		"Compile the items into a URL query string"

		items = []

		for key, value in self.items():
			items.append(f"{quote(key)}={quote(value)}")

		return "&".join(items)


	def values(self) -> Iterator[str]:
		"Iterate through all of the values"

		for item in self:
			yield item[1]
