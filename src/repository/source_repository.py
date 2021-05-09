from src.domain.data_source import OWIDDataSource, MapacheArgDataSource


class SourceRepository:

    sources = {
        'owid': OWIDDataSource(),
        'mapache_arg': MapacheArgDataSource()
    }

    @classmethod
    def retrieve_data_source(cls, source_id):
        return cls.sources.get(source_id)

    @classmethod
    def list_sources(cls):
        return cls.sources.values()
