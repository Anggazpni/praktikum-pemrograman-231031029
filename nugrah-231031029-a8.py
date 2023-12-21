passwords = ["angga", "regas", "123"]
percobaan = 3
correct_passwords = 0
locked_account = False

while correct_passwords < len(passwords) and not locked_account:
    attempts = 0

    while attempts < percobaan:
        password = input(f"Masukkan password {correct_passwords + 1}: ")
        attempts += 1

        if password == passwords[correct_passwords]:
            print(f"Password {correct_passwords + 1} benar!")
            correct_passwords += 1
            break
        else:
            if attempts == percobaan:
                print("Anda telah melebihi masa percobaan untuk password ini. Akun terkunci.")
                locked_account = True
                break
            else:
                remaining_attempts = percobaan - attempts
                print(f"Password anda salah. Anda memiliki {remaining_attempts} percobaan lagi untuk password {correct_passwords + 1}.")

if correct_passwords == len(passwords) and not locked_account:
    print("Selamat Anda telah Login!")