def get_team_id(team_key):
    query = """
    query TeamQuery($key: String!) {
      team(key: $key) {
        id
        name
      }
    }
    """
    payload = {
        "query": query,
        "variables": {"key": team_key},
    }
    
    # Print the payload for debugging
    print("Payload being sent:", payload)
    
    try:
        resp = session.post(LINEAR_API_URL, json=payload)
        resp.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

    data = resp.json()
    if not data.get("data") or not data["data"]["team"]:
        print(f"Could not find team with key {team_key}")
        return None
    return data["data"]["team"]["id"]
