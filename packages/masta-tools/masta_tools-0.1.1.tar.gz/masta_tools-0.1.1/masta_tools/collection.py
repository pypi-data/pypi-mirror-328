


class Collection(list):
    def __init__(self, data):
        super(Collection, self).__init__(data)
        
        
    @classmethod
    def fromListOfLists(cls, data:list, hdrIx:int=0, func=None):
        hdr = data[hdrIx]
        data = [dict(zip(hdr,x)) for x in data[hdrIx:]]
        if func is None:
            func=lambda x: True
        data = [x for x in data if func(x)]
        return cls(data)
    
    
    @staticmethod
    def listdict_to_listlist(data:list):
        out = []
        hdr = list(data[0].keys())
        out.append(hdr)
        for r in data:
            s=list(r.values())
            out.append(s)
        return out
    
    @staticmethod
    def chunkify(items:list, chunk=1_000):
        """"Takes an input list and returns a list of lists 
        chunked according to chunk size.
        """
        total = len(items)
        remaining = total
        A = 0
        Z = min(A + chunk, total)
        results = []
        while remaining > 0:
            Z = min(total, A + chunk)
            results.append(items[A:Z])
            remaining = total - Z
            A = Z 
        return results
    
    @classmethod
    def empty(cls):
        return cls([])
    
    
    @classmethod
    def where(cls, iterable, func):
        return cls.query(iterable, func)
    
    
    @staticmethod
    def query(iterable, func):
        t=[x for x in iterable if func(x)]
        return Collection(t)
    
    
    def align(self):
        # align a list of dicts so that all keys have same order 
        # this will base everything off of the first dict item in the list
        template = list(self[0].keys())
        for i in range(len(self)):
            x = self[i]
            r = {k:x.get(k,None) for k in template}
            self[i]=r
    
    
    @staticmethod
    def get_header(data):
        top=list(data[0].keys())
        return top
    
    
    @property
    def headers(self):
        return self.get_header(self)
    
    
    
    def sum_if(self, sumField:str, filterFunc=None, decimals:int=0):
        return self._sum_if(self, sumField, filterFunc, decimals)
    
    
    @staticmethod
    def _sum_if(iterable, sumField, filterFunc=None, decimals:int=0):
        if filterFunc is None:
            filterFunc = lambda x: True
        rsp = round(sum([(x.get(sumField,0) or 0) for x in iterable if filterFunc(x)]), decimals)
        if decimals==0:
            rsp=int(rsp)
        return rsp
    
    
    def max_if(self, maxField, filterFunc=None):
        return self._max_if(self, maxField, filterFunc)
    
    
    @staticmethod
    def _max_if(iterable, maxField, filterFunc=None):
        if filterFunc is None:
            filterFunc = lambda x: True
        m = [x[maxField] for x in iterable if filterFunc(x)]
        if len(m)==0:
            return None
        return max(m)
    
    
    def min_if(self, minField, filterFunc=None):
        return self._min_if(self, minField, filterFunc)
    
    
    @staticmethod
    def _min_if(iterable, minField, filterFunc=None):
        if filterFunc is None:
            filterFunc = lambda x: True
        m = [x[minField] for x in iterable if filterFunc(x)]
        if len(m)==0:
            return None
        return min(m)
    
    
    
    def count_if(self, filterFunc=None):
        if filterFunc is None:
            filterFunc = lambda x: True
        rsp = len([x for x in self if filterFunc(x)])
        return rsp
    
    
    def search(self, matchValue, matchField:str):
        rsp = [x for x in self if x[matchField]==matchValue]
        return Collection(rsp)
    
    
    def index_match(self, other, matchValue, matchField):
        other.sort()
        try:
            rsp = other.search(matchValue, matchField)
        except:
            other = Collection(other)
            rsp = other.search(matchValue, matchField)
        return rsp
    
    
    def order_by(self, by:str, reverse=False):
        self.sort(key=lambda x: x[by], reverse=reverse)
        



def fast_group(iterable, field, save_iterable=False, dotget=False):
    """
    iterable = list of dictionaries (or a collection object)
    field = str or list of str (for isolated multi-index grouping (1st and 2nd indexes can repeat, but their combinations cannot)
    save_iterable = bool (if true, retain the originally passed iterable to avoid accidental deletion, otherwise, it trashes itself)
    dotget = bool (if true, use a "." (dot) notation when filtering vs ["key"] (hash) notation (like a normal dictionary))
    """
    if save_iterable:
        runner = iterable.copy()
    else:
        runner = iterable
    out = {}
    multi = not isinstance(field, str)
    get = lambda item, field: item[field] if not dotget else getattr(item, field)
    while len(runner)>0:
        r = runner.pop()
        if multi:
            key = tuple(get(r, i) for i in field)
        else:
            key = get(r, field)
        c = out.get(key, Collection.empty())
        c.append(r)
        out[key]=c
    return out