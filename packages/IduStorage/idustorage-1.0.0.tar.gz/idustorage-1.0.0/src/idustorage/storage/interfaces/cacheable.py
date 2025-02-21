from pathlib import Path


class Cacheable:
    """Abstract class for anything that can or should be cached"""

    def to_file(self, path: Path, name: str, ext: str, date: str, separator: str, *args) -> str:
        """
        Save cacheable object to file

        :param path: Path-like path to file
        :param name: rather a type of a file
        :param ext: extension of a file
        :param date: creation date of a file
        :param separator: separator used for filename
        :param args: specification for a file to distinguish between
        """
        pass
