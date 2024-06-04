# Sanity check - hello world
def hello_world():
    print("Hello World")
    

# Function to benchmark a simple query
def benchmark_query(query, time, benchmark_data, collection, index_name=None):
    if index_name:
        print(f"\nQuerying with index on {index_name}...")
    else:
        print("\nQuerying without index...")

    start_time = time.time()
    results = list(collection.find(query))
    end_time = time.time()

    duration = end_time - start_time
    result_count = len(results)

    print(f"Query took {duration:.6f} seconds")
    print(f"Number of results: {result_count}")

    benchmark_data.append({
        "query": query,
        "index_name": index_name,
        "duration": duration,
        "result_count": result_count
    })
    
    return benchmark_data
# Function definitions
def build_query_left_join_listings_reviewsm_10():
    """Builds SQL query for left joining listings and reviews on review_id, for IDs starting with '10'."""
    query = """
select *
from listings l left join reviewsm r 
        on l.id = r.listing_id
  where left(l.id,2) = '10'
    """
    return query

def build_query_left_join_listings_reviewsm():
    """Builds SQL query for left joining all listings and reviews on review_id."""
    query = """
select *
from listings l left join reviewsm r 
        on l.id = r.listing_id
    """
    return query


def time_diff(start_time, end_time):
    """Calculate the difference in seconds between two datetime objects."""
    difference = end_time - start_time
    return difference.total_seconds()