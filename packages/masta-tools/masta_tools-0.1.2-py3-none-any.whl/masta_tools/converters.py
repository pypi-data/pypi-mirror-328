import dateutil.parser
import json

def string_to_datetime(datestring):
    yourdate = dateutil.parser.parse(datestring)
    return yourdate

def string_to_money(moneystring:str) -> float:
    if isinstance(moneystring, (int,float)):
        return round(float(moneystring), 2)
    og = moneystring
    rms = [("$",""), ("(", "-"), (")",""), (",",""), (" ","")]
    for wrong, right in rms:
        moneystring = moneystring.replace(wrong, right)
    try:
        return round(float(moneystring or "0"), 2)
    except:
        raise Exception(f"{og} is not a valid money data type.")
    
def string_to_int(intstr:str) -> int:
    if isinstance(intstr, (int,float)):
        return int(round(intstr, 0))
    try:
        return int(round(float(intstr or '0')))    
    except:
        raise Exception(f"{intstr} is not a valid integer")
    
def truncate(f, n) -> float:
    """Round a float to the n-th decimal point without rounding up or down (truncate it)"""
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return float('.'.join([i, (d+'0'*n)[:n]]))


class TableMapper():
    def __init__(self, 
                 mapp:dict[str, list], 
                 case_sensitive:bool=True,
                 auto_meta:bool=False,
                 skip_missing:bool=False,
                 rem_chars:list=None
                 ):
        self.case_sensitive = case_sensitive
        self.auto_meta = auto_meta
        self.skip_missing = skip_missing
        self.rem_chars = rem_chars
        self.mapp = {
            self.standardize_key(key):
                [self.standardize_key(val) for val in vals]
            for key, vals in mapp.items()
        }
    
    def nocase(self, value):
        return str(value).lower()
    
    def standardize_key(self, value:str):
        if not self.case_sensitive:
            value = str(value).lower()
        if isinstance(self.rem_chars,list):
            for ch in self.rem_chars:
                value = str(value).replace(ch,'')
        return value
    
    def remap(self, remapper:dict, row:dict):
        new = {
            newk:row[oldk] for oldk,newk in remapper.items()
        }
        if self.auto_meta:
            new['_meta_'] = json.dumps(row, default=str, indent=2)
        return new
    
    def process(self, data:list[dict]):
        r = data[0]
        remapper = {}
        mapped = []
        remaining = list(self.mapp.keys())
        for key in r.keys():
            test = self.standardize_key(key)
            if test in self.mapp and test not in mapped:
                remapper[key]=test # key stays the same
                mapped.append(test)
                remaining.remove(test)
                continue
            for newkey,vs in self.mapp.items():
                if newkey in mapped:
                    continue # no duplicates
                if test in vs:
                    remapper[key]=newkey
                    mapped.append(newkey)
                    remaining.remove(newkey)
                    break
        if len(remaining) > 0 and not self.skip_missing:
            raise Exception("Some Fields are missing from the table: {}".format(", ".join(remaining)))
        output = list(map(lambda row: self.remap(remapper, row), data))
        return output