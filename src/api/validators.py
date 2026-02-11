def validate_user_object(user):
    assert isinstance(user, dict)

    required_keys = {"id", "email", "first_name", "last_name", "avatar"}

    assert required_keys.issubset(user.keys())

    assert isinstance(user["id"], int)
    assert isinstance(user["email"], str)
    assert "@" in user["email"]
