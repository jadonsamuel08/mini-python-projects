import secrets
import string

def get_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please enter y or n.")


def get_length(min_length=8, default=12):
    while True:
        raw = input(f"Password length (default {default}, min {min_length}): ").strip()
        if raw == "":
            return default
        if raw.isdigit() and int(raw) >= min_length:
            return int(raw)
        print(f"Enter a number >= {min_length}.")


def build_pools():
    pools = []

    use_lower = get_yes_no("Include lowercase? (y/n): ")
    use_upper = get_yes_no("Include uppercase? (y/n): ")
    use_digits = get_yes_no("Include digits? (y/n): ")
    use_symbols = get_yes_no("Include symbols? (y/n): ")

    if use_lower:
        pools.append(string.ascii_lowercase)
    if use_upper:
        pools.append(string.ascii_uppercase)
    if use_digits:
        pools.append(string.digits)
    if use_symbols:
        pools.append("!@#$%^&*()-_=+[]{};:,.?/")

    return pools


def generate_password(length, pools):
    # Ensure at least one char from each selected group
    password_chars = [secrets.choice(pool) for pool in pools]

    combined_pool = "".join(pools)
    for _ in range(length - len(password_chars)):
        password_chars.append(secrets.choice(combined_pool))

    # Shuffle to avoid predictable order
    secrets.SystemRandom().shuffle(password_chars)
    return "".join(password_chars)


def main():
    print("=== Password Generator ===")

    while True:
        length = get_length()
        pools = build_pools()

        if not pools:
            print("You must choose at least one character type.\n")
            continue

        if length < len(pools):
            print(f"Length must be at least {len(pools)} for your selected options.\n")
            continue

        password = generate_password(length, pools)
        print(f"\nGenerated password:\n{password}\n")

        again = get_yes_no("Generate another? (y/n): ")
        if not again:
            print("Goodbye.")
            break
        print()


if __name__ == "__main__":
    main()