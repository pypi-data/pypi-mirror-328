Projet de construction d un gestionnaire de flux

Ajouter une nouvelle source : 
1. ajouter dans sandie.model.sources le nouvel fichier py
   definition des methodes defini par sandie.model.source.py
2. ajouter dans sandie.model.connection.py la nouvelle source
   import sandie.model.sources.xxxx as xxx
   elif source_type == "MYSQL":
        return my.MYSQLSource(*args, **kwargs)
3. definir la source dans data.config.sources.yaml