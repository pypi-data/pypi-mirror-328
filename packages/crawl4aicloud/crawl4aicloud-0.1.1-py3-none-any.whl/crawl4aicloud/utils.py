import base64
import binascii


def validate_base64(v: str) -> bool:
    """
    Validate if a string is a valid base64 encoded value.

    Args:
        v: String to validate

    Returns:
        bool: True if valid base64, False otherwise
    """
    try:
        # Try to decode it
        base64.b64decode(v, validate=True)
        return True
    except (binascii.Error, TypeError):
        return False


def decode_base64(v: str) -> bytes:
    """
    Decode a base64 encoded string to bytes.

    Args:
        v: Base64 encoded string

    Returns:
        bytes: Decoded bytes
    """
    return base64.b64decode(v)
