# Publications Configuration Guide

## Overview
This file explains how to add publications to your website using the `publications.yaml` configuration file.

## File Location
`data/publications.yaml`

## Adding a New Publication

### Basic Template
```yaml
- title: "Your Publication Title"
  authors:
    - "First Author Name"
    - "Second Author Name"
  journal: "Journal Name"
  year: 2024
  volume: "123"  # Optional
  pages: "1-10"  # Optional
  doi: "10.xxxx/xxxxx"  # Optional: DOI number
  url: "https://doi.org/10.xxxx/xxxxx"  # Required: Link to publication
  pmid: "12345678"  # Optional: PubMed ID
  abstract: "Publication abstract text here..."
  categories:
    - "Category 1"
    - "Category 2"
  tags:
    - "tag1"
    - "tag2"
  image: "/images/publications/example.jpg"  # Optional: publication image
```

### Required Fields
- `title`: Publication title
- `authors`: List of author names
- `journal`: Journal name
- `year`: Publication year
- `url`: Link to the publication (DOI link or direct URL)

### Optional Fields
- `doi`: DOI number (e.g., "10.1038/nature12373")
- `pmid`: PubMed ID
- `volume`: Journal volume
- `pages`: Page numbers
- `abstract`: Publication abstract
- `categories`: List of categories
- `tags`: List of tags
- `image`: Path to publication image

## Fetching Publication Metadata

### Using DOI
You can fetch metadata from DOI using these methods:

#### 1. Crossref API (Recommended)
```bash
# Example: Get metadata for DOI 10.1038/nature12373
curl "https://api.crossref.org/works/10.1038/nature12373"
```

#### 2. Python Script
```python
import requests
import json

def get_publication_info(doi):
    url = f"https://api.crossref.org/works/{doi}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        message = data['message']
        return {
            'title': message.get('title', [''])[0],
            'authors': [f"{a.get('given', '')} {a.get('family', '')}" for a in message.get('author', [])],
            'journal': message.get('container-title', [''])[0],
            'year': message.get('published-print', {}).get('date-parts', [[None]])[0][0],
            'doi': doi,
            'url': f"https://doi.org/{doi}",
            'abstract': message.get('abstract', '')
        }
    return None

# Usage
doi = "10.1038/nature12373"
info = get_publication_info(doi)
print(json.dumps(info, indent=2))
```

#### 3. Using habanero Library
```python
from habanero import Crossref

cr = Crossref()
result = cr.works(ids="10.1038/nature12373")
# Extract information from result
```

### Using PubMed ID
```python
import requests
from xml.etree import ElementTree as ET

def get_pubmed_info(pmid):
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params = {
        'db': 'pubmed',
        'id': pmid,
        'retmode': 'xml'
    }
    response = requests.get(url, params=params)
    # Parse XML and extract information
    # ... (implementation details)
```

## Example Entry

```yaml
publications:
  - title: "Forest dynamics and biodiversity in tropical ecosystems"
    authors:
      - "John Doe"
      - "Jane Smith"
      - "Yuyue Deng"
    journal: "Nature Ecology & Evolution"
    year: 2024
    volume: "8"
    pages: "123-145"
    doi: "10.1038/s41559-024-01234-5"
    url: "https://doi.org/10.1038/s41559-024-01234-5"
    abstract: "This study examines forest dynamics and biodiversity patterns in tropical ecosystems using long-term monitoring data from multiple forest plots."
    categories:
      - "Forest Ecology"
      - "Biodiversity"
    tags:
      - "forest dynamics"
      - "biodiversity"
      - "tropical forests"
```

## Notes
- Publications are displayed in the order they appear in the YAML file
- You can sort them by year, journal, or any other criteria by reordering the list
- The abstract will be truncated to 150 characters on the display page
- All links open in a new tab for better user experience

