# Simple SHA1 Password Cracker
import hashlib

def converted_txt_to_sha1(password):
    digest = hashlib.sha1(
        password.encode()
    ).hexdigest()

    return digest 

def main():
    user_sha1 = input("Enter the SHA1 hash to crack: ")
    cleaned_user_sha1 = user_sha1.strip().lower()

    with open("./rockyou.txt") as f:
        for line in f:
            password = line.strip()
            converted_sha1 = converted_txt_to_sha1(password)
            if cleaned_user_sha1 == converted_sha1:
                print(f"Password found: {password}")
                return
    print("Password not found in the list.")


if __name__ == "__main__":
    main()