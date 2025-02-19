from copy import deepcopy

class DataPoint:
    def __init__(self, row, datapoint_name=None):
        self.row = row
        self.og  = deepcopy(row)
        self.extra = {}
        self.datapoint_name = datapoint_name
    
    def __getitem__(self, k):
        if k not in self.row:
            return self.extra.get(k, None)
        return self.row[k]
    
    def __setitem__(self, k, v):
        if k not in self.row:
            self.extra[k] = v
        else:
            self.row[k] = v
    
    def dict(self):
        return deepcopy(self.row)

    def save(self):
        self.og = deepcopy(self.row)
    
    def rollback(self):
        self.row = deepcopy(self.og)
    
    @property
    def has_changes(self):
        return any([self.og[k]!=v for k,v in self.row.items()])
    
    def __repr__(self):
        if self.datapoint_name is not None:
            return f"<DataPoint ({self.datapoint_name})>"
        return "<DataPoint>"