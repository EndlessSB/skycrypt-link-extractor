import re
import sys

def extract_sky_shiiyu_links(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Regex pattern to find links starting with the given URL
        pattern = r'https://sky\.shiiyu\.moe/stats/\S*'
        links = re.findall(pattern, content)
        
        return links
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
    else:
        filename = sys.argv[1]
        extracted_links = extract_sky_shiiyu_links(filename)
        
        if extracted_links:
            print("Extracted Links:")
            for link in extracted_links:
                print(link)
        else:
            print("No matching links found.")
