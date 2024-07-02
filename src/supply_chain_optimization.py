from gremlin_python.driver import client, serializer

# Neptune connection details
neptune_endpoint = 'your-neptune-endpoint'
neptune_port = '8182'
neptune_ssl = True

# Connect to Neptune
neptune_client = client.Client(f'wss://{neptune_endpoint}:{neptune_port}/gremlin', 'g',
                               message_serializer=serializer.GraphSONSerializersV2d0())

# Function to find shortest path between nodes
def find_shortest_path(source, target):
    query = f"g.V().has('name', '{source}').repeat(out().simplePath()).until(has('name', '{target}')).path().limit(1).toList()"
    result = neptune_client.submit(query).all().result()
    return result

# Example usage
if __name__ == "__main__":
    path = find_shortest_path('Warehouse A', 'Warehouse B')
    print(path)
