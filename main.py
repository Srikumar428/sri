PLACE_HOLDER = "[name]"
with open("invited_names.txt") as invitees:
    names = invitees.readlines()
    print(names)
with open("starting_letter.txt") as invitation:
    invite = invitation.read()
    for name in names:
        stripped_letter = name.strip()
        new = invite.replace(PLACE_HOLDER,stripped_letter)
        with open(f"letter_to_{stripped_letter}",mode = "w") as new_letter:
            new_letter.write(new)