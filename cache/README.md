# Cache Directory

This directory stores cached responses to improve performance.

## Structure

```
cache/
└── responses/    # Cached LLM response files (JSON format)
```

## How It Works

- Responses are cached based on query + context hash
- Cache files are stored as JSON with metadata
- TTL (Time To Live) can be configured in `config.yaml`
- Cache improves response time by avoiding redundant LLM calls

## Note

Cache files are gitignored as they are auto-generated and can be regenerated.

