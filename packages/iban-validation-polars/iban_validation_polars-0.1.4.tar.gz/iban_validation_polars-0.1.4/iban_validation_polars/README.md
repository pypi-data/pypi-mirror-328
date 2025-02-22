# iban_validation_polars
A package to facilitate validation of IBANs and selecting Bank_id and Branch_id as a Polars plugin.

Leveraging Polars Multi-threaded feature to split IBANs

Example:
```python
import polars as pl
from iban_validation_polars import process_ibans
import os

inputfile = r'iban_validation_rs/data/IBAN Examples.txt'
outputfile = r'iban_validation_polars/examples/test_file.csv'

# File generation 
df = pl.read_csv(inputfile).sample(10000000, with_replacement=True)
df.write_csv(outputfile)
print('writing to file complete')

# using the library
df = pl.scan_csv(outputfile)\
    .with_columns(
    validated=process_ibans('IBAN Examples').str.split_exact(',',2)\
        .struct.rename_fields(['valid_ibans', 'bank_id', 'branch_id'])
).unnest('validated').sort(by='IBAN Examples', descending=True)

# show some results
print(df.collect(streaming=True))

# cleanup
os.remove(outputfile)
```

# Changes
 - 0.14: technical update; updated polars dependency to polars 0.46.0, and py03 0.23 impacting only the Python packages.