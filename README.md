# Dynamic DNS Updater for IONOS

This Python script updates your A and AAAA DNS records in IONOS to match your machine’s current public IPv4 and IPv6 addresses. It is useful when you want to keep your domain or subdomain pointed to a dynamic IP address (like when using a residential ISP without a static IP).

## Features
✅ Fetches current public IPv4 and IPv6 addresses using ipify.
✅ Retrieves your DNS zone and record information from the IONOS DNS API.
✅ Updates A and AAAA records if they differ from your current public IPs.
✅ Logs detailed debug output for troubleshooting.

## Requirements
- Python 3.10 or newer (uses type hints with | syntax).
- requests library.

### You can install dependencies with:

```bash
pip install requests
```

## Usage

```bash
python update_dns.py --subdomain SUBDOMAIN --domain DOMAIN --api-json PATH_TO_JSON
```

## Arguments

```bash
--subdomain or -s: The subdomain to update (e.g., www).
--domain or -d: The root domain (e.g., example.com).
--api-json or -j: Path to a JSON file containing your IONOS API credentials.
```

## JSON Config File

Create a JSON file (e.g., secrets.json) with the following structure:

```bash
{
  "public_prefix": "your_api_key_prefix",
  "secret": "your_api_key_secret"
}
```

## License

MIT License — use freely and modify as needed.
