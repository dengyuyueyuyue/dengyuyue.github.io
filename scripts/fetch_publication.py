#!/usr/bin/env python3
"""
Publication Metadata Fetcher
Fetches publication metadata from DOI, URL, or ScienceDirect links
and generates YAML format for publications.yaml

Usage:
    python scripts/fetch_publication.py "10.1016/j.jenvman.2024.123456"
    python scripts/fetch_publication.py "https://www.sciencedirect.com/science/article/pii/S0301479724038659"
    python scripts/fetch_publication.py "https://doi.org/10.1016/j.jenvman.2024.123456"
"""

import requests
import re
import sys
import json
from urllib.parse import urlparse, parse_qs
import yaml

def extract_doi_from_url(url):
    """Extract DOI from various URL formats"""
    # Direct DOI URL
    if 'doi.org' in url:
        match = re.search(r'10\.\d+/[^\s/?]+', url)
        if match:
            return match.group(0)
    
    # ScienceDirect URL - try to extract DOI from URL or fetch from page
    if 'sciencedirect.com' in url:
        # First try to get DOI from the page (more reliable)
        try:
            response = requests.get(url, timeout=15, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
            })
            response.raise_for_status()
            
            # Look for DOI in various formats in the page
            # Pattern 1: JSON-LD structured data
            json_ld_patterns = [
                r'"doi":\s*"(10\.\d+/[^"]+)"',
                r'"identifier":\s*{\s*"@type":\s*"PropertyValue"[^}]*"value":\s*"(10\.\d+/[^"]+)"',
            ]
            for pattern in json_ld_patterns:
                doi_match = re.search(pattern, response.text)
                if doi_match:
                    return doi_match.group(1)
            
            # Pattern 2: Meta tags
            meta_patterns = [
                r'<meta[^>]*name=["\']citation_doi["\'][^>]*content=["\'](10\.\d+/[^"\']+)["\']',
                r'<meta[^>]*property=["\']citation_doi["\'][^>]*content=["\'](10\.\d+/[^"\']+)["\']',
            ]
            for pattern in meta_patterns:
                doi_match = re.search(pattern, response.text, re.IGNORECASE)
                if doi_match:
                    return doi_match.group(1)
            
            # Pattern 3: In text content
            doi_match = re.search(r'DOI[:\s]+(10\.\d+/[^\s<"]+)', response.text, re.IGNORECASE)
            if doi_match:
                return doi_match.group(1)
            
            # Pattern 4: In script tags with JSON
            script_matches = re.findall(r'<script[^>]*>(.*?)</script>', response.text, re.DOTALL)
            for script_content in script_matches:
                doi_match = re.search(r'10\.\d+/[^\s"\'<>]+', script_content)
                if doi_match:
                    potential_doi = doi_match.group(0)
                    # Validate it looks like a DOI
                    if len(potential_doi) > 10 and potential_doi.startswith('10.'):
                        return potential_doi
        except Exception as e:
            print(f"Warning: Could not fetch page to extract DOI: {e}", file=sys.stderr)
    
    # Try to find DOI pattern in URL itself
    doi_match = re.search(r'10\.\d+/[^\s/?]+', url)
    if doi_match:
        return doi_match.group(0)
    
    return None

def fetch_from_crossref(doi):
    """Fetch metadata from Crossref API"""
    try:
        url = f"https://api.crossref.org/works/{doi}"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
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
            
            # Extract publication date
            date_parts = None
            if 'published-print' in message and 'date-parts' in message['published-print']:
                date_parts = message['published-print']['date-parts'][0]
            elif 'published-online' in message and 'date-parts' in message['published-online']:
                date_parts = message['published-online']['date-parts'][0]
            elif 'created' in message and 'date-parts' in message['created']:
                date_parts = message['created']['date-parts'][0]
            
            year = date_parts[0] if date_parts else None
            
            # Extract title
            title = message.get('title', [''])[0] if message.get('title') else ''
            
            # Extract journal
            journal = message.get('container-title', [''])[0] if message.get('container-title') else ''
            
            # Extract volume and pages
            volume = message.get('volume', '')
            pages = ''
            if 'page' in message:
                pages = message['page']
            elif 'article-number' in message:
                pages = f"Article {message['article-number']}"
            
            # Extract abstract
            abstract = ''
            if 'abstract' in message:
                abstract = message['abstract']
            elif 'description' in message:
                abstract = message['description'][0] if isinstance(message['description'], list) else message['description']
            
            return {
                'title': title,
                'authors': authors,
                'journal': journal,
                'year': year,
                'volume': str(volume) if volume else None,
                'pages': pages,
                'doi': doi,
                'url': f"https://doi.org/{doi}",
                'abstract': abstract
            }
    except Exception as e:
        print(f"Error fetching from Crossref: {e}", file=sys.stderr)
    
    return None

def fetch_from_sciencedirect(url):
    """Try to fetch metadata from ScienceDirect page"""
    try:
        response = requests.get(url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
        if response.status_code == 200:
            text = response.text
            
            # Try to find JSON-LD structured data
            json_ld_match = re.search(r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', text, re.DOTALL)
            if json_ld_match:
                try:
                    json_data = json.loads(json_ld_match.group(1))
                    if isinstance(json_data, list):
                        json_data = json_data[0]
                    
                    title = json_data.get('headline', '')
                    authors = []
                    if 'author' in json_data:
                        for author in json_data['author']:
                            if isinstance(author, dict):
                                name = author.get('name', '')
                                if name:
                                    authors.append(name)
                    
                    journal = json_data.get('publisher', {}).get('name', '') if isinstance(json_data.get('publisher'), dict) else ''
                    date_published = json_data.get('datePublished', '')
                    year = None
                    if date_published:
                        year_match = re.search(r'(\d{4})', date_published)
                        if year_match:
                            year = int(year_match.group(1))
                    
                    doi = json_data.get('identifier', {}).get('value', '') if isinstance(json_data.get('identifier'), dict) else ''
                    if not doi:
                        doi = json_data.get('doi', '')
                    
                    abstract = json_data.get('description', '')
                    
                    if title:
                        return {
                            'title': title,
                            'authors': authors,
                            'journal': journal,
                            'year': year,
                            'doi': doi,
                            'url': url,
                            'abstract': abstract
                        }
                except:
                    pass
            
            # Fallback: try to extract from meta tags
            title_match = re.search(r'<meta[^>]*property=["\']og:title["\'][^>]*content=["\']([^"\']+)["\']', text)
            title = title_match.group(1) if title_match else ''
            
            if title:
                return {
                    'title': title,
                    'authors': [],
                    'journal': '',
                    'year': None,
                    'doi': '',
                    'url': url,
                    'abstract': ''
                }
    except Exception as e:
        print(f"Error fetching from ScienceDirect: {e}", file=sys.stderr)
    
    return None

def generate_yaml(metadata):
    """Generate YAML format for publications.yaml"""
    yaml_data = {
        'title': metadata.get('title', ''),
        'authors': metadata.get('authors', []),
        'journal': metadata.get('journal', ''),
        'year': metadata.get('year'),
    }
    
    if metadata.get('volume'):
        yaml_data['volume'] = metadata['volume']
    if metadata.get('pages'):
        yaml_data['pages'] = metadata['pages']
    if metadata.get('doi'):
        yaml_data['doi'] = metadata['doi']
    
    yaml_data['url'] = metadata.get('url', '')
    
    if metadata.get('abstract'):
        yaml_data['abstract'] = metadata['abstract']
    
    # Add placeholder for categories and tags
    yaml_data['categories'] = []
    yaml_data['tags'] = []
    
    return yaml.dump([yaml_data], default_flow_style=False, allow_unicode=True, sort_keys=False)

def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/fetch_publication.py <DOI_or_URL>")
        print("\nExamples:")
        print("  python scripts/fetch_publication.py 10.1016/j.jenvman.2024.123456")
        print("  python scripts/fetch_publication.py https://www.sciencedirect.com/science/article/pii/S0301479724038659")
        print("  python scripts/fetch_publication.py https://doi.org/10.1016/j.jenvman.2024.123456")
        sys.exit(1)
    
    input_str = sys.argv[1].strip()
    
    print(f"Fetching metadata for: {input_str}\n", file=sys.stderr)
    
    # Try to extract DOI
    doi = None
    if input_str.startswith('10.'):
        doi = input_str
    elif 'doi.org' in input_str or 'sciencedirect.com' in input_str:
        doi = extract_doi_from_url(input_str)
    
    metadata = None
    
    # Try Crossref API first (most reliable)
    if doi:
        print(f"Found DOI: {doi}", file=sys.stderr)
        print("Fetching from Crossref API...", file=sys.stderr)
        metadata = fetch_from_crossref(doi)
    
    # If Crossref failed and it's a ScienceDirect URL, try direct fetch
    if not metadata and 'sciencedirect.com' in input_str:
        print("Fetching from ScienceDirect page...", file=sys.stderr)
        metadata = fetch_from_sciencedirect(input_str)
    
    if not metadata:
        print("Error: Could not fetch publication metadata.", file=sys.stderr)
        print("Please check the DOI/URL and try again, or add manually.", file=sys.stderr)
        sys.exit(1)
    
    # Generate YAML output
    yaml_output = generate_yaml(metadata)
    
    print("\n" + "="*60, file=sys.stderr)
    print("Generated YAML (copy this to data/publications.yaml):", file=sys.stderr)
    print("="*60 + "\n", file=sys.stderr)
    print(yaml_output)
    
    print("\n" + "="*60, file=sys.stderr)
    print("Preview:", file=sys.stderr)
    print("="*60, file=sys.stderr)
    print(f"Title: {metadata.get('title', 'N/A')}", file=sys.stderr)
    print(f"Authors: {', '.join(metadata.get('authors', [])) if metadata.get('authors') else 'N/A'}", file=sys.stderr)
    print(f"Journal: {metadata.get('journal', 'N/A')}", file=sys.stderr)
    print(f"Year: {metadata.get('year', 'N/A')}", file=sys.stderr)
    print(f"DOI: {metadata.get('doi', 'N/A')}", file=sys.stderr)
    print("="*60, file=sys.stderr)

if __name__ == '__main__':
    main()

