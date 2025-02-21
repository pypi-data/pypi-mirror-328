import sandie.model.sources.restapi as ra
import sandie.model.sources.csv as csv
import sandie.model.sources.postgresql as pg
import sandie.model.sources.mysql as my

class Connection:
    @staticmethod
    def create(source_type, *args, **kwargs):
        if source_type == "CSV":
            return csv.CSVSource(*args, **kwargs)
        elif source_type == "POSTGRESQL":
            return pg.POSTGRESQL(*args, **kwargs)
        elif source_type == "RESTAPI":
            return ra.RESTAPISource(*args, **kwargs)
        elif source_type == "MYSQL":
            return my.MYSQLSource(*args, **kwargs)
        else:
            raise ValueError(f"Source type {source_type} not supported.")