Sample of the OpenAI GPT message with image content:
```json
{
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "What is in this image?"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": "data:image/jpeg;base64,<base64_image>"
          }
        }
      ]
    }
  ]
}
```

Sample of the Google Gemini message with image content:
```json
{
  "contents": [
    {
      "role": "user",
      "parts": [
        {
          "text": "What is in this image?"
        },
        {
          "inline_data": {
            "mime_type": "image/jpeg",
            "data": "<base64_image>"
          }
        }
      ]
    }
  ]
}
```

Sample of the Anthropic Claude message with image content:
```json
{
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "What is in this image?"
        },
        {
          "type": "image",
          "source": {
            "type": "base64",
            "media_type": "image/jpeg", 
            "data": "<base64_image>"
          }
        }
      ]
    }
  ]
}
```