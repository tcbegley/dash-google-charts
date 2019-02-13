from .gviz import _DataTable


class DataTable(_DataTable):
    @classmethod
    def from_pandas(cls, df):
        """
        Convert a Pandas DataFrame to a DataTable object.
        """
        pass

    @staticmethod
    def _resolve_type():
        pass
