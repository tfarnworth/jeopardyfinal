categories = ["Shakespeare", "Movies", "History", "Sports", "Computer Science"]

Shakespeare = ["Shakespeare heavily relied on this theatre company to produce his plays.", "It wasn't true love that killed Romeo, it was this.", "This character is famously known as a foil to Macbeth.", "In King Lear, Gloucester loses one of his senses when this is cut off.", "This character delivered Shakespeare's famous To Be or Not to Be Speech."]

Movies = ["This actor plays Batman in 2008s The Dark Knight", "In this 1980 horror movie, a family is isolated in an eerie hotel with a sinister past.","This 1999 film features a group of misfits who band together to fight against a corrupt system in a dystopian future.","In this animated film, a young lion named Simba learns to embrace his identity and take his place in the circle of life.","This popular film franchise follows a hobbit named Frodo as he embarks on a quest to destroy a powerful ring."]

History = ["This ancient civilization is known for its pyramids and pharaohs, located along the Nile River.","In 1776, this document was signed, declaring the thirteen American colonies' independence from British rule.","This conflict, known for its trench warfare and the introduction of tanks, lasted from 1914 to 1918.","This famous speech by Martin Luther King Jr. was delivered during the March on Washington in 1963.","This empire, which spanned three continents at its height, was ruled by Suleiman the Magnificent in the 16th century."]

Sports = ["This sport is known as 'the beautiful game' and is played by two teams of eleven players.","In 1980, this U.S. hockey team achieved a stunning upset over the Soviet Union in the Winter Olympics.","This athlete holds the record for the most home runs in a single MLB season, hitting 73 in 2001.","This tennis tournament, held annually in London, is the oldest Grand Slam event and features a grass court.","This basketball player, known as 'His Airness,' won six NBA championships with the Chicago Bulls in the 1990s."]

Computer_Science = ["This programming language, known for its use in web development, was created by Brendan Eich in 1995.","This data structure follows the Last In, First Out (LIFO) principle.","In computer networking, this protocol is commonly used to transfer files over the internet.","This algorithm, often associated with sorting, has an average time complexity of O(n log n).","This type of machine learning involves training a model on labeled data to make predictions."]

score = 0

def start_game(score):
    w = str(input("Welcome to Jeopardy! Would you like to play? Yes or no?: "))
    if w.upper() == "YES":
        one_turn(score)
    else:
        print("Too bad")
        exit()


def one_turn(score):
    print(categories)
    select = str(input("Select a category: "))
    if select.upper() == "SHAKESPEARE":
        Shakespeare_questions(score)
    if select.upper() == "MOVIES":
        Movies_questions(score)


def Shakespeare_questions(score):
    pvs = str(input("Select your point value. 100, 200, 300, 400, 500: "))
    if pvs == "500":
        print(Shakespeare[0])
        a1 = str(input("Answer: "))
        if a1.upper() == "THE GLOBE":
            score += 500
            print("Correct! Total score=",score,)
        else:
            score -= 500
            print("Wrong! Total score=",score,"Correct answer was The Globe.")
            return score
    if pvs == "400":
        print(Shakespeare[3])
        a2 = str(input("Answer: "))
        if a2.upper() == "EYES" or a2.upper() == "HIS EYES":
            score += 400
            print("Correct! Total score =", score)
        else:
            score -= 400
            print("Wrong! Total score =",score,"Correct Answer is eyes.")
            return score
    if pvs == "300":
        print(Shakespeare[4])
        a3 = str(input("Answer: "))
        if a3.upper() == "HAMLET":
            score += 300
            print("Correct! Total score =",score)
        else:
            score -= 300
            print("Wrong! Total score =",score,"Correct answer is Hamlet.")
            return score
    if pvs == "200":
        print(Shakespeare[2])
        a4 = str(input("Answer: "))
        if a4.upper() == "MACDUFF":
            score += 200
            print("Correct! Total score =",score)
        else:
            score -= 200
            print("Wrong! Total score =",score,"Correct answer is Macduff.")
            return score
    if pvs == "100":
        print(Shakespeare[1])
        a5 = str(input("Answer: "))
        if a5.upper() == "POISON":
            score += 100
            print("Correct! Total score =",score)
        else:
            score += 100
            print("Wrong! Total score =",score)
            return score

def Movies_questions(score):
    pvs = str(input("Select your point value. 100, 200, 300, 400, 500: "))
    if pvs == "500":
        print(Movies[0])
        a1 = str(input("Answer: "))
        if a1.upper() == "CHRISTIAN BALE":
            score += 500
            print("Correct! Total score =",score,)
        else:
            score -= 500
            print("Wrong! Total score =",score,"Correct answer was Christian Bale.")
            return score
    if pvs == "400":
        print(Movies[2])
        a2 = str(input("Answer: "))
        if a2.upper() == "MATRIX" or a2.upper() == "THE MATRIX":
            score += 400
            print("Correct! Total score =", score)
        else:
            score -= 400
            print("Wrong! Total score =",score,"Correct Answer is The Matrix.")
            return score
    if pvs == "300":
        print(Movies[1])
        a3 = str(input("Answer: "))
        if a3.upper() == "THE SHINING" or a3.upper() == "SHINING":
            score += 300
            print("Correct! Total score =",score)
        else:
            score -= 300
            print("Wrong! Total score =",score,"Correct answer is The Shining.")
            return score
    if pvs == "200":
        print(Movies[3])
        a4 = str(input("Answer: "))
        if a4.upper() == "THE LION KING" or a4.upper() == "LION KING":
            score += 200
            print("Correct! Total score =",score)
        else:
            score -= 200
            print("Wrong! Total score =",score,"Correct answer is The Lion King.")
            return score
    if pvs == "100":
        print(Movies[1])
        a5 = str(input("Answer: "))
        if a5.upper() == "LORD OF THE RINGS" or "THE LORD OF THE RINGS":
            score += 100
            print("Correct! Total score =",score)
        else:
            score += 100
            print("Wrong! Total score =",score,"Correct answer is The Lord of The Rings")
            return score
 
        
        
start_game(score)
one_turn(score)
