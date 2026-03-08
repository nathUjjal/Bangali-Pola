from ddgs import DDGS
class SearchWeb:
    def __init__(self):
        self.search=DDGS()
  
    def search_web_text(self,query, max_results=5):
        try:
            search_result=self.search.text(
                query,
                region="in-en",
                max_results=max_results);
        except Exception as e:
            raise Exception(f"Error while searching the web: {str(e)}")
        return search_result
    
    def search_web_images(self,query, max_results=100):
        try:
            search_results=self.search.images(
                query,
                region="in-en",
                max_results=max_results,
                color="Monochrome",
                license="Public");
        except Exception as e:
            raise Exception(f"Error while searching the web: {str(e)}")
        return search_results
    
    
    def search_web_news(self,query, max_results=10):
        try:
            search_results=self.search.news(
                query,
                region="in-en",
                max_results=max_results,
                safe_search="on");
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