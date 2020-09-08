def convert_to_months(years):
    months = years * 12
    return months


def main():
    age = input('How many years old is your child? ')
    age_in_years = int(age)
    age_in_months = convert_to_months(age_in_years)
    print(str(age_in_years) + ' years is ' + str(age_in_months) + ' months')


if __name__ == '__main__':
    main()
