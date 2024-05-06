def build_profile(primeiro, ultimo, **user_info):
    profile = {} 
    profile['first_name'] = primeiro
    profile['last_name'] = ultimo
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile("paulo", "martins", age=40, profissão="engenheiro")
print(user_profile)
