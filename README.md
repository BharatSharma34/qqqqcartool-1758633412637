# qqqqCarTool - Lambda Tool

Testing car tool

## Quick Start

1. Clone this repository:
   ```bash
   git clone https://github.com/BharatSharma34/qqqqcartool-1758633412637.git
   cd qqqqcartool-1758633412637
   ```

2. Add your AWS credentials to GitHub Secrets:
   - Go to Settings → Secrets and variables → Actions
   - Add: `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`
   - Optionally add: `TOOL_SECRET` for additional security

3. Edit `tool.py` with your tool logic (see example below)

4. Update `requirements.txt` if you need additional Python packages

5. Push to main branch to auto-deploy to AWS Lambda

## Files

- `tool.py` - Your tool's main code (edit this file)
- `requirements.txt` - Python dependencies
- `.github/workflows/deploy.yml` - Auto-deployment workflow
- `README.md` - This file

## How to Write Your Tool

Edit the `tool.py` file with your logic. Here's an example:

```python
def process_data(name, age, city="Unknown"):
    """
    Your tool function - this will be automatically called
    
    Parameters from the request body will be matched to function parameters
    """
    result = {
        "greeting": f"Hello {name}!",
        "info": f"You are {age} years old from {city}",
        "processed_at": "2024-01-01"
    }
    return result

def another_function(data):
    # If you have multiple functions, the last one will be used
    return {"processed": data}
```

## How Your Tool Works

1. **Automatic Parameter Matching**: Parameters from the request body are automatically matched to your function parameters
2. **Simple Return**: Just return any JSON-serializable data (dict, list, string, number)
3. **Error Handling**: Errors are automatically caught and returned as error responses
4. **Dependencies**: Add any Python packages to `requirements.txt`

## Testing Your Tool

Once deployed, your Lambda function will be available as:
**Function Name:** `qqqqcartool-1758633412637`

You can test it using AWS CLI:
```bash
aws lambda invoke \
  --function-name qqqqcartool-1758633412637 \
  --payload '{"body": "{\"name\": \"John\", \"age\": 25, \"city\": \"New York\"}"}' \
  response.json
```

## Deployment

Every push to the `main` branch automatically:
1. Takes your `tool.py` code
2. Wraps it with necessary Lambda handling code
3. Installs dependencies from `requirements.txt`
4. Deploys to AWS Lambda

**Note:** You don't need to worry about Lambda handlers or AWS-specific code - just write your tool logic!

## Tool Details

- **Secret Key:** sk-tvyod3gap-mfwkw5wu
- **Created:** 2025-09-23T13:16:54.320Z
- **Runtime:** Python 3.11
- **Timeout:** 60 seconds
- **Memory:** 128 MB

## Support

For issues or questions about this tool, please contact the development team.
