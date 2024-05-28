def env_to_bool(value: str):
    value = str(value).lower().strip()
    return value in ["1", "t", "true"]
