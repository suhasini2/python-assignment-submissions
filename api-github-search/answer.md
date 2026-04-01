1. What is the role of query parameters in this request?
Query parameters are the key-value pairs added to the end of a URL (after the ?) to filter, sort, or paginate the server's database results. In this specific request:

q: Acts as the search filter (searching for "python").

sort and order: Tell the GitHub server how to organize the data before sending it back.

per_page: Limits the payload size, ensuring the server only sends the top 5 results rather than the default (usually 30).

2. Why do we use response.json() instead of response.text?
response.text: Returns a raw string. To access a specific piece of data (like the number of stars), you would have to manually parse that string using complex string slicing or regular expressions.

response.json(): Automatically parses the string and converts it into a Python dictionary/list. This allows you to access data using standard keys (e.g., data["items"][0]["name"]), making the code significantly cleaner, faster to write, and less prone to errors.