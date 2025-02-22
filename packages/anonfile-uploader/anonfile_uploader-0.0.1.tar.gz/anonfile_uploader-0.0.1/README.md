# Anonfile Uploader 

```bash
$ python3 -m pip install anonfile-uploader
```


## Example
```python
from anonfile import Anonfile

anonfile = Anonfile()
link = anonfile.upload_file('path/to/your/file.jpg')
print(f"Uploaded File: {link}")
```
