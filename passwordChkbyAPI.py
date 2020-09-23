import requests
import hashlib
import sys


def request_api_check(password):
    url = "https://api.pwnedpasswords.com/range/" + password
    res = requests.get(url)
    return res


def get_leaked_count(hashes, hash2check):
    hashes = (line.split(":") for line in str.splitlines(hashes.text))
    for h, count in hashes:
        if h == hash2check:
            return count
    return 0


def request_passwd_chk(password):
    hashed = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    firstpwd, tailpwd = hashed[:5], hashed[5:]
    response = request_api_check(firstpwd)
    return get_leaked_count(response, tailpwd)


def main(argvs):
    for argv in argvs:
        count = request_passwd_chk(argv)
        if count:
            print(f"{argv} has been used for {count} times, You should change it!")
        else:
            print(f"{argv} Not find!")
    print("Done!")


if __name__ == "__main__":
    main(sys.argv[1:])

