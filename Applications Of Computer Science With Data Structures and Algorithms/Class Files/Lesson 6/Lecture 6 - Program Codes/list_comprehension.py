def main():
    my_list = [1, 2, 3, 4, 5]

    # without comprehension
    print("Without Comprehension")
    for i in range(len(my_list)):
        print("first loop: " + str(my_list[i]))

    # with comprehension
    print("\nWith Comprehension")
    [print("second loop: " + str(my_list[i])) for i in range(len(my_list))]

    print("\nWithout Comprehension")
    # without comprehension
    h_letters = []
    for letter in "human":
        h_letters.append(letter)
    print(h_letters)

    print("\nWith Comprehension")
    # with comprehension
    h_letters = [letter for letter in "human"]
    print(h_letters)

    print("\nWithout Comprehension")
    # without comprehension
    squares1 = []
    for i in range(1, 101):
        squares1.append(i ** 2)
    print(squares1)

    print("\nWith Comprehension")
    # with comprehension
    squares2 = [i ** 2 for i in range(1, 101)]
    print(squares2)

    print("\nWithout Comprehension")
    # without comprehension
    combs = []
    for x in [1, 2, 3]:
        for y in [3, 1, 4]:
            if (x != y) and (x < y):
                tuples = (x, y)
                combs.append((x, y))
    print(combs)

    print("\nWith Comprehension")
    # with comprehension
    comes = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if (x != y) and (x < y)]
    print(combs)

    print("\nWithout Comprehension")
    # without comprehension
    movies = ["The Nun", "Peppermint", "A Simple Favor", "White Boy Rick", "UFO", "Hunt For The Skinwalker",
              "Breaking & Exiting", "The Equalizer 2", "The Hate U Give", "How It Ends", "Blaze", "Zoe",
              "Skate Kitchen", "Skyscraper", "The Bookshop", "Bisbee '17", "Good Manners",
              "The Predator - Added Full Trailer", "Beautiful Boy", "Assassination Nation", "Mandy",
              "Support the Girls", "Madeline's Madeline", "Our House"]
    gmovies = []
    for title in movies:
        if title.startswith("G"):
            gmovies.append(title)
    print(gmovies)

    print("\nWith Comprehension")
    # with comprehension
    gmovies = [title for title in movies if title.startswith("G")]
    print(gmovies)

if __name__ == "__main__":
    main()