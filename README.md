## Project Architecture

This project follows a modular supply chain automation design.

Logical structure (for understanding):

config/
- settings.py
- prompts.py

data_sample/
- sales.csv
- inventory.csv
- suppliers.csv

src/
- ingestion/
- features/
- forecasting/
- optimization/
- agents/
- outputs/
- utils/

tests/
- test_smoke.py

Note:
Due to GitHub upload constraints, files may appear in a flat structure, but the logical architecture remains modular as described above.