import pandas as pd
import sandie.model.logger as l
import sandie.conf.model.connection as con
import sandie.model.source as src

# CSV definition object for connection
class CSVSource(src.Source):
    def __init__(self, source):
        self.logger = l.Logger()

        # definition des parameter de la connexion API REST
        self.csv_connect = con.Csv(
            path=source['PATH']
        )
        self.connection = con.Connection(
            alias=source['ALIAS'],
            type='CSV',
            csv=self.csv_connect
        )

    def read_data(self, query=None):
        self.logger.debug('lecture de la source CSV....')
        return pd.read_csv(self.connection.csv.path)