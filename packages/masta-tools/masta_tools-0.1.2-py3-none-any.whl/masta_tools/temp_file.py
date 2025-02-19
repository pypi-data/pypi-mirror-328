from pathlib import Path
from anyio import Path as ioPath
import os, asyncio
import base64

class FileAlreadyExists(Exception):
    ...

class AsyncTempFile():
    def __init__(self,
                 filepath:str|ioPath|os.PathLike,
                 mode:str="wb"):
        self.filepath = (filepath 
                         if isinstance(filepath, ioPath) 
                         else ioPath(str(filepath)))
        self.mode = mode
        self.mgr  = None
        self.file = None
        
    async def __aenter__(self):
        self.mgr = await self.filepath.open(
            mode=self.mode
        )
        self.file = await self.mgr.__aenter__()
        return self.file
        
    async def __aexit__(self, ex_tp, ex_v, tx_tb):
        if self.mgr is not None:
            await self.mgr.__aexit__(ex_tp, ex_v, tx_tb)
        
        
async def process_async_temp_file(filepath:str|ioPath|os.PathLike, raw:bytes, processor:object):
    """
    Arguments:
    - filepath (str or pathlike object; absolute/relative path to the desired temporary location; it will check to make sure the path does not exist before running)
    - raw (bytes: this is the raw content of the file in bytes)
    - processor (sync or async callable function that takes one argument 'filepath')
    
    Utilizes AsyncTempFile to 'process' the file using this strategy:
    1. Write/Create temporary file by writing 'raw' (bytes) to the provided 'filepath'
    2. Run the processor method using the temporary filepath as the only argument
        - the result of 'processor' is returned at the end of the function
    3. Delete the file from file system
    """
    
    # raw is base64 encoded
    data = base64.b64decode(raw)
    filepath = ioPath(str(filepath))
    if await filepath.exists():
        raise FileAlreadyExists(f"Temporary file already exists: '{str(filepath)}'")
    if not callable(processor):
        raise Exception("Processor must be a callable function or a class with a __call__ method defined.")
    async with AsyncTempFile(filepath) as file:
        await file.write(data)
    if asyncio.iscoroutinefunction(processor):
        rsp = await processor(filepath)
    else:
        rsp = processor(filepath)
    os.remove(filepath)
    return rsp


def process_temp_file(filepath:str|ioPath|os.PathLike, raw:bytes, processor:object):
    """
    Arguments:
    - filepath (str or pathlike object; absolute/relative path to the desired temporary location; it will check to make sure the path does not exist before running)
    - raw (bytes: this is the raw content of the file in bytes)
    - processor (callable function that takes one argument 'filepath')
    
    Utilizes os.open to 'process' the file using this strategy:
    1. Write/Create temporary file by writing 'raw' (bytes) to the provided 'filepath'
    2. Run the processor method using the temporary filepath as the only argument
        - the result of 'processor' is returned at the end of the function
    3. Delete the file from file system
    """
    filepath = Path(str(filepath))
    if filepath.exists():
        raise FileAlreadyExists(f"Temporary file already exists: '{str(filepath)}'")
    if not callable(processor):
        raise Exception("Processor must be a callable function or a class with a __call__ method defined.")
    with open(filepath, 'wb') as file:
        file.write(raw)
    rsp = processor(filepath)
    os.remove(filepath)
    return rsp