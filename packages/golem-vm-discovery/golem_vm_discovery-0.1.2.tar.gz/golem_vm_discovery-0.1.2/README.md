# Golem VM Discovery Server

The Discovery Server acts as the central hub for the Golem Network, enabling requestors to find providers with matching resources.

## Installation

```bash
pip install golem-vm-discovery
```

## Running the Server

1. Create a configuration file `.env`:

```bash
# Server Settings
GOLEM_DISCOVERY_HOST="0.0.0.0"
GOLEM_DISCOVERY_PORT=7465
GOLEM_DISCOVERY_DEBUG=false

# Database Settings (optional)
GOLEM_DISCOVERY_DATABASE_DIR="/path/to/database/dir"  # Default: ~/.golem/discovery
GOLEM_DISCOVERY_DATABASE_NAME="discovery.db"          # Default: discovery.db

# Rate Limiting (optional)
GOLEM_DISCOVERY_RATE_LIMIT_PER_MINUTE=100

# Advertisement Settings (optional)
GOLEM_DISCOVERY_ADVERTISEMENT_EXPIRY_MINUTES=5
GOLEM_DISCOVERY_CLEANUP_INTERVAL_SECONDS=60
```

2. Run the server:

```bash
golem-discovery
```

The server will:
- Create a SQLite database in `~/.golem/discovery` by default
- Listen on port 7465 by default
- Accept provider advertisements
- Clean up expired advertisements automatically

## API Endpoints

- `GET /health` - Health check endpoint
- `GET /api/v1/advertisements` - List available providers
- `POST /api/v1/advertisements` - Register a provider

## Environment Variables

All settings can be configured through environment variables:

| Variable | Description | Default |
|----------|-------------|---------|
| GOLEM_DISCOVERY_HOST | Server host | 0.0.0.0 |
| GOLEM_DISCOVERY_PORT | Server port | 7465 |
| GOLEM_DISCOVERY_DEBUG | Enable debug mode | false |
| GOLEM_DISCOVERY_DATABASE_DIR | Database directory | ~/.golem/discovery |
| GOLEM_DISCOVERY_DATABASE_NAME | Database filename | discovery.db |
| GOLEM_DISCOVERY_RATE_LIMIT_PER_MINUTE | Rate limit per IP | 100 |
| GOLEM_DISCOVERY_ADVERTISEMENT_EXPIRY_MINUTES | Advertisement TTL | 5 |
| GOLEM_DISCOVERY_CLEANUP_INTERVAL_SECONDS | Cleanup interval | 60 |

## Development

To run the server in development mode:

```bash
GOLEM_DISCOVERY_DEBUG=true golem-discovery
```

This will enable auto-reload on code changes and more detailed logging.
