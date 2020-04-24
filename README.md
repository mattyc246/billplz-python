# Billplz Python

A simple implementation of a Billplz Client to interface with some of the commonly used API endpoints.


## Dependencies

* [requests](http://docs.python-requests.org/en/latest/)

This implementation was writing in Python version 3.7.6 and has been tested against only version 3.7.6

## Quick Start Example

```python
from billplz.client import Billplz

client = Billplz(
  api_key='<api_key>',
  collection_id="<collection_id>",
  test=True # By default this will be set to False which will use production endpoint, if you wish to use sandbox, set to True
)

response = client.create_bill_with_redirect(
  email="test@email.com",
  name="Test User",
  amount=100, # amount provided in smallest demnomination 100 = RM1.00
  description="Test Product",
  callback_url="somethingurl",
  redirect_url="somethingurl",
  collection_id="<collection_id>" # Optional to use alternative collection than the initialized
)

if response.is_success:
  return redirect(response.redirect_url)


```

## Developing

1. Create Environment and Start with Poetry:

   ```
   poetry shell
   ```

2. Install dependencies:

   ```
   poetry install
   ```

## Testing

Tests are to be written in Pytest.

## License

See the [LICENSE](LICENSE) file for more info.