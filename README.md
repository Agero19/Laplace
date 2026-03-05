# Laplace - Marketplace Analytics engine

## Project Structure

Minimal but scalable.

```text
laplace/
│
├── app/
│   ├── core/
│   │   ├── config.py
│   │   └── database.py
│   │
│   ├── models/
│   │   └── listing.py
│   │
│   ├── collectors/
│   │   └── leboncoin.py
│   │
│   ├── analytics/
│   │   ├── liquidity.py
│   │   └── metrics.py
│   │
│   ├── api/
│   │   └── main.py
│   │
│   └── dashboard/
│       └── dashboard.py
│
├── scripts/
│   └── scrape_leboncoin.py
│
├── .env
└── pyproject.toml
```

Phisolsopy:

- collectors → raw data
- models → typed storage
- analytics → business intelligence
- dashboard → visualization
