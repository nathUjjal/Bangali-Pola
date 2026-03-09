from ddgs import DDGS

class SearchWeb:
    """A class for performing various types of web searches using DuckDuckGo Search (DDGS).

    This class provides methods to search for text, images, and news articles on the web.
    It utilizes the DDGS library to interact with DuckDuckGo's search engine.
    """

    def __init__(self):
        """Initialize the SearchWeb instance.

        Creates a DDGS search object for performing web searches.
        """
        self.search = DDGS()

    def search_web_text(self, query, max_results=5):
        """Search for text-based web results.

        Performs a text search on the web using DuckDuckGo and returns relevant results.

        Args:
            query (str): The search query string.
            max_results (int, optional): Maximum number of results to return. Defaults to 5.

        Returns:
            list: A list of dictionaries containing search results with keys like 'title', 'url', 'body', etc.

        Raises:
            Exception: If an error occurs during the search process.
        """
        try:
            search_result = self.search.text(
                query,
                region="in-en",
                max_results=max_results
            )
        except Exception as e:
            raise Exception(f"Error while searching the web: {str(e)}")
        return search_result

    def search_web_images(self, query, max_results=100):
        """Search for images on the web.

        Performs an image search on the web using DuckDuckGo and returns image results.

        Args:
            query (str): The search query string for images.
            max_results (int, optional): Maximum number of image results to return. Defaults to 100.

        Returns:
            list: A list of dictionaries containing image search results with keys like 'title', 'url', 'thumbnail', etc.

        Raises:
            Exception: If an error occurs during the search process.
        """
        try:
            search_results = self.search.images(
                query,
                region="in-en",
                max_results=max_results,
                color="Monochrome",
                license="Public"
            )
        except Exception as e:
            raise Exception(f"Error while searching the web: {str(e)}")
        return search_results

    def search_web_news(self, query, max_results=10):
        """Search for news articles on the web.

        Performs a news search on the web using DuckDuckGo and returns recent news articles.

        Args:
            query (str): The search query string for news.
            max_results (int, optional): Maximum number of news results to return. Defaults to 10.

        Returns:
            list: A list of dictionaries containing news search results with keys like 'title', 'url', 'date', 'body', etc.

        Raises:
            Exception: If an error occurs during the search process.
        """
        try:
            search_results = self.search.news(
                query,
                region="in-en",
                max_results=max_results,
                safe_search="on"
            )
        except Exception as e:
            raise Exception(f"Error while searching the web: {str(e)}")
        return search_results


if __name__=="__main__":
    # results=SearchWeb().search_web_images("messy kolkata recent..")
    # for r in results:
    #     print(f"Title: {r['title']}")
    #     print(f"URL: {r['url']}")
    #     print(f"Source: {r['source']}")
    #     print(f"Thumbnail: {r['thumbnail']}")
    #     print("-"*50)
    try:
        results=SearchWeb().search_web_news("messy kolkata recent crowdrage")
        print(f"Total news found: {len(results)}")
        print("-"*70)
        print("Top news results:",results[:5])
        for r in results:
            print(f"Title: {r['title']}")
            print(f"URL: {r['url']}")
            print(f"Source: {r['source']}")
            print(f"Description : {r['body']}")
            print("-"*70)
    except Exception as e:
        print(f"Error: {str(e)}")