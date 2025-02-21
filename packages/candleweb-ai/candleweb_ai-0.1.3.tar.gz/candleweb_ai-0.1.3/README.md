# My Custom Tool

A custom tool for Candleweb AI agents.

## Installation

```bash
pip install candleweb-ai
```

## Usage

import the tool and use it within your application:

```bash
from candleweb_ai import PlaceOrderTool

# Create an instance of the tool
order_tool = PlaceOrderTool()

# Execute the tool with required parameters
response = order_tool._run(
    ai='BINANCE-ETHDEMO',
    exchange='BINANCE',
    pair='ETHUSDT',
    mode='DEMO',
    side='BUY',
    api_key='your_api_key_here',
    enviroment='demo'  # for sandboxapi and 'live' for production
)

print(response)
```

## Features

- Place BUY or SELL orders on the Candleweb AI platform.

- Supports different AI models and exchanges.

- Handles authentication via API keys.

- Ensures idempotency for requests.


## License

This project is licensed under the MIT License. See the LICENSE file for details.