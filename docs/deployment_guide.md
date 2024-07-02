# Deployment Guide for Supply Chain Optimization using Neptune Graph Database

## Prerequisites

- AWS account with access to Neptune service.
- Python 3.x installed locally.
- Neptune endpoint and credentials configured.

## Setting Up Neptune

1. **Create Neptune Instance**:
   - Log in to AWS Management Console.
   - Navigate to Amazon Neptune.
   - Create a new Neptune instance with appropriate configurations.

2. **Configure Security Groups**:
   - Ensure that your Neptune instance security group allows inbound connections on port 8182 from your IP address or network.

3. **Obtain Neptune Endpoint**:
   - Once the instance is created, note down the endpoint URL and port for connecting to Neptune.

## Running the Project

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/supply-chain-neptune.git
   cd supply-chain-neptune
