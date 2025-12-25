#!/usr/bin/env python3
"""
Simple Publication Adder
Just provide a DOI and it will fetch metadata from Crossref API

Usage:
    py scripts/add_publication.py "10.1016/j.jenvman.2024.123456"
"""

import requests
import sys
import yaml
import re

def clean_doi(doi_input):
    """Clean and extract DOI from various formats"""
    # Remove URL parts
    doi = re.sub(r'https?://(dx\.)?doi\.org/', '', doi_input)
    doi = doi.strip()
    
    # Validate DOI format
    if not re.match(r'^10\.\d+/', doi):
        return None
    return doi

def fetch_publication(doi):
    """Fetch publication metadata from Crossref"""
    try:
        url = f"https://api.crossref.org/works/{doi}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        message = data.get('message', {})
        
        # Extract authors
        authors = []
        for author in message.get('author', []):
            given = author.get('given', '')
            family = author.get('family', '')
            if given and family:
                authors.append(f"{given} {family}")
            elif family:
                authors.append(family)
        
        # Extract date
        date_parts = None
        for date_type in ['published-print', 'published-online', 'created']:
            if date_type in message and 'date-parts' in message[date_type]:
                date_parts = message[date_type]['date-parts'][0]
                break
        
        year = date_parts[0] if date_parts else None
        
        # Extract other fields
        title = message.get('title', [''])[0] if message.get('title') else ''
        journal = message.get('container-title', [''])[0] if message.get('container-title') else ''
        volume = message.get('volume', '')
        pages = message.get('page', '')
        
        # Extract abstract
        abstract = ''
        if 'abstract' in message:
            # Remove HTML tags if present
            abstract = re.sub(r'<[^>]+>', '', message['abstract'])
        elif 'description' in message:
            desc = message['description']
            if isinstance(desc, list):
                abstract = re.sub(r'<[^>]+>', '', desc[0])
            else:
                abstract = re.sub(r'<[^>]+>', '', desc)
        
        return {
            'title': title,
            'authors': authors,
            'journal': journal,
            'year': year,
            'volume': str(volume) if volume else None,
            'pages': pages,
            'doi': doi,
            'url': f"https://doi.org/{doi}",
            'abstract': abstract.strip() if abstract else ''
        }
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return None

def generate_yaml_entry(metadata):
    """Generate YAML entry"""
    entry = {
        'title': metadata['title'],
        'authors': metadata['authors'],
        'journal': metadata['journal'],
        'year': metadata['year'],
        'url': metadata['url']
    }
    
    if metadata.get('volume'):
        entry['volume'] = metadata['volume']
    if metadata.get('pages'):
        entry['pages'] = metadata['pages']
    if metadata.get('doi'):
        entry['doi'] = metadata['doi']
    if metadata.get('abstract'):
        entry['abstract'] = metadata['abstract']
    
    # Add placeholders
    entry['categories'] = []
    entry['tags'] = []
    
    return yaml.dump([entry], default_flow_style=False, allow_unicode=True, sort_keys=False)

def main():
    if len(sys.argv) < 2:
        print("Usage: py scripts/add_publication.py <DOI>")
        print("\nExample:")
        print('  py scripts/add_publication.py "10.1016/j.jenvman.2024.123456"')
        print("\nFor ScienceDirect articles:")
        print("  1. Open the article page")
        print("  2. Find the DOI (usually shown on the page)")
        print("  3. Run this script with the DOI")
        sys.exit(1)
    
    doi_input = sys.argv[1]
    doi = clean_doi(doi_input)
    
    if not doi:
        print(f"Error: Invalid DOI format: {doi_input}", file=sys.stderr)
        print("DOI should start with '10.' (e.g., 10.1016/j.jenvman.2024.123456)", file=sys.stderr)
        sys.exit(1)
    
    print(f"Fetching metadata for DOI: {doi}...\n", file=sys.stderr)
    
    metadata = fetch_publication(doi)
    
    if not metadata:
        print("Failed to fetch metadata. Please add manually.", file=sys.stderr)
        sys.exit(1)
    
    yaml_output = generate_yaml_entry(metadata)
    
    print("\n" + "="*70, file=sys.stderr)
    print("Copy the following YAML to data/publications.yaml:", file=sys.stderr)
    print("="*70 + "\n", file=sys.stderr)
    print(yaml_output)
    
    print("\n" + "="*70, file=sys.stderr)
    print("Preview:", file=sys.stderr)
    print("="*70, file=sys.stderr)
    print(f"Title: {metadata['title']}", file=sys.stderr)
    print(f"Authors: {', '.join(metadata['authors']) if metadata['authors'] else 'N/A'}", file=sys.stderr)
    print(f"Journal: {metadata['journal']}", file=sys.stderr)
    print(f"Year: {metadata['year']}", file=sys.stderr)
    print("="*70, file=sys.stderr)
    print("\nNote: Don't forget to add categories and tags!", file=sys.stderr)

if __name__ == '__main__':
    main()



