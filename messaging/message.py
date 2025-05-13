import json
import uuid
from datetime import datetime

def create_message(sender, recipient, content, metadata=None):
    return {
        "id": str(uuid.uuid4()),
        "timestamp": datetime.utcnow().isoformat(),
        "from": sender,
        "to": recipient,
        "content": content,
        "metadata": metadata or {},
        # Optional: "signature": sign_with_private_key(...)
    }