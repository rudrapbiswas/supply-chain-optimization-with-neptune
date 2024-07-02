## Clone the repository:
git clone https://github.com/your-username/supply-chain-neptune.git

cd supply-chain-neptune

## Install Python dependencies:
pip install -r requirements.txt

## Explanation
gremlinpython: This library provides the Python bindings for interacting with Amazon Neptune using Gremlin query language.

networkx: Used for creating, manipulating, and visualizing complex networks (graphs) in Python, which is handy for graph-based operations and visualizations.

matplotlib: A plotting library for creating static, animated, and interactive visualizations in Python, suitable for visualizing graphs and data plots.


Execute Gremlin scripts (01_create_schema.gremlin, 02_load_data.gremlin) in scripts/ to set up schema and load data into Neptune.

Run supply_chain_optimization.py to execute optimization algorithms.

Open visualization.ipynb in Jupyter Notebook for visual analysis.
