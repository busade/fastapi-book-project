from fastapi import APIRouter
from fastapi.responses import JSONResponse

from core.config import settings


router = APIRouter()

integration_json = {
  "data": {
    "date": {
      "created_at": "2025-02-15",
      "updated_at": "2025-02-15"
    },
    "descriptions": {
      "app_name": "CI/CD pipeline",
      "app_description": "This is a real time update  integration platform",
      "app_logo": "ec2-13-61-190-61.eu-north-1.compute.amazonaws.com",
      "app_url": "ec2-13-61-190-61.eu-north-1.compute.amazonaws.com",
      "background_color": "#fff"
    },
    "is_active": True,
    "integration_type": "modifier",
    "key_features": [
      "real-time updates",
      "slack notification"
    ],
    "author": "Adesola",
    "settings": [
      {
        "label": "Slack-channel",
        "type": "text",
        "required": True,
        "default": "#updates"
      },
      {
        "label": "Time interval",
        "type": "dropdown",
        "required": True,
        "default": "immediate",
        "options": [
          "immediate",
          "Every-5mins",
          "Every-10mins",
          "Every-1hour"
        ]
      },
      {
        "label": "Event type",
        "type": "dropdown",
        "required": True,
        "default": "CI_pipeline",
        "options": [
          "CI_pipeline",
          "CD_pipeline",
          "Log error"
        ]
      },
      {
        "label": "Message",
        "type": "text",
        "required": True,
        "default": "Basic"
      },
      {
        "label": "Inlude Logs",
        "type": "checkbox",
        "required": True,
        "default": "True"
      }
    ],
    "target_url": settings.SLACK_WEBHOOK_URL,
    "tick_url": settings.THICK_URL
  }
}

@router.get('/integration-config')
async def get_integration_json():
    return JSONResponse(content=integration_json)