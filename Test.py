
import requests
import feedparser

def fetch_llama2_papers(max_results=70):
    base_url = "http://export.arxiv.org/api/query?"

    # Construct the API query parameters for papers related to "llama2"
    query = "llama"
    params = {
        'search_query': f'all:"{query}"',
        'max_results': max_results,
        'sortBy': 'relevance',
        'start': 0,
        'sortOrder': 'descending',
    }

    # Make the request to the arXiv API
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        # Parse the XML response using feedparser
        feed = feedparser.parse(response.text)

        # Check if there are entries in the feed
        if feed.entries:
            # Extract paper titles and abstracts
            papers = []
            for entry in feed.entries:
                title = entry.get('title', '').strip()
                abstract = entry.get('summary', '').strip()
                paper_info = f"Title: {title}\nAbstract: {abstract}\n"
                papers.append(paper_info)

            return papers
        else:
            print("No papers found for the given query.")
            return []
    else:
        print(f"Error fetching papers. Status code: {response.status_code}")
        return []

# Example usage
llama2_papers = fetch_llama2_papers(max_results=70)


 # Write the fetched papers to a text file
output_file="llama2_papers.txt"
with open(output_file, 'w', encoding='utf-8') as file:
    file.writelines(llama2_papers)