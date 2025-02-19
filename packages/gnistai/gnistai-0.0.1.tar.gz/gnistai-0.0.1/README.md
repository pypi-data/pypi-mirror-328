# GnistAI Python API library

The OpenAI Python library provides convenient access to the GnistAI REST API from any Python 3.11+
application.

The REST API documentation can be found on [gnist.ai/api/docs](https://gnist.ai/api/docs).

# Usage

```python
import os
from gnistai import GnistAI

client = GnistAI(api_key=os.environ.get("GNISTAI_API_KEY"))
health_status = client.health_check()
```

While you can provide an `api_key` keyword argument,
we recommend using [python-dotenv](https://pypi.org/project/python-dotenv/)
to add `GNIST_API_KEY="My API Key"` to your `.env` file
so that your API Key is not stored in source control.
