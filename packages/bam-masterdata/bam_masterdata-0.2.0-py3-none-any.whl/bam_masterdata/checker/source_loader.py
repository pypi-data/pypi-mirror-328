class SourceLoader:
    def __init__(self, source: str, source_type: str):
        self.source = source
        self.source_type = source_type

    def load(self) -> dict:
        """
        Read and transform the new entity data into JSON.
        """
        if self.source_type == "python":
            return self._parse_python_classes()
        elif self.source_type == "excel":
            return self._parse_excel()
        else:
            raise NotImplementedError(f"Source type {self.source_type} not supported.")

    def _parse_python_classes(self) -> dict:
        """
        Parse new entities defined as Python classes.
        """
        pass

    def _parse_excel(self) -> dict:
        """
        Parse new entities stored in an Excel file.
        """
        pass
