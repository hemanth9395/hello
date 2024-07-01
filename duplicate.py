from utilis import is_valid_name
profile = {"mob": None, "name": None, "dob": None,
           "blood_group": None, "gender": None ,
           "Address": {"street_name": "", "city": "",
                       "state": "", "pin": ""}}

registered_users = [9333466662,88885990919]

print(f"please enter tge profule details")

profile ["mob"] = int(input ("mobile:"))
if profile ["mob"] in registered_users:
    print ("mobile no verified successfully\n please enter the details")
    profile ["name"] = input ("name is :")
    if is_valid_name(profile ["name"]):
        profile ["dob"] = input ("Date of birth:")
        profile ["blood_group"] = input ("blood group:")
        profile ["gender"] = input ("gender:")

        print(f"profile saved successfully for mobile no {profile["mob"]}")
        print(f"{profile}")
else:
    print(f"incorrect {profile["mob"]}")
