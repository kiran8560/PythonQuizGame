class Question:
    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_question(self):
        user_answer = input(self.question)
        return user_answer.lower() == self.correct_answer.lower()


def main():
    print("Welcome to the quiz game")
    playing = input("Do you want to play? (yes/no): ")
    if playing.lower() != "yes":
        quit()

    questions = [
        Question("What does the CPU stand for? ", "central processing unit"),
        Question("What does the RAM stand for? ", "random access memory"),
        Question("Who is the author of 'Romeo and Juliet'? ", "William Shakespeare"),
        Question("What is the largest planet in our solar system? ", "Jupiter"),
        Question("Which gas do plants absorb from the atmosphere? ", "Carbon dioxide"),
        Question("What is the capital of France? ", "Paris"),
        Question("Who painted the 'Mona Lisa'? ", "Leonardo da Vinci"),
        Question("What is the chemical symbol for gold? ", "Au"),
        Question("Which planet is known as the Red Planet? ", "Mars"),
        Question("Who was the first President of the United States? ", "George Washington"),
        Question("What is the largest mammal in the world? ", "Blue whale"),
Question("Who wrote 'Pride and Prejudice'? ", "Jane Austen"),
Question("What is the chemical symbol for water? ", "H2O"),
Question("In which country is the Great Barrier Reef located? ", "Australia"),
Question("Which gas is most abundant in the Earth's atmosphere? ", "Nitrogen"),
Question("What is the currency of Japan? ", "Japanese yen"),
Question("What is the largest ocean on Earth? ", "Pacific Ocean"),
Question("Who is known as the 'Father of Modern Physics'? ", "Albert Einstein"),
Question("Which gas do humans exhale when they breathe? ", "Carbon dioxide"),
Question("In which year did the Titanic sink? ", "1912"),
Question("What is the capital of China? ", "Beijing"),
Question("Which planet is known as the 'Morning Star' or 'Evening Star'? ", "Venus"),
Question("Who painted the 'Starry Night'? ", "Vincent van Gogh"),
Question("What is the chemical symbol for silver? ", "Ag"),
Question("What is the smallest prime number? ", "2"),
Question("Which gas is responsible for the green color of plants? ", "Chlorophyll"),
Question("Who wrote 'The Catcher in the Rye'? ", "J.D. Salinger"),
Question("What is the currency of the United Kingdom? ", "British pound"),
Question("Which country is known as the Land of the Rising Sun? ", "Japan"),
Question("What is the chemical symbol for iron? ", "Fe"),
Question("How many continents are there in the world? ", "7"),
Question("Who is the Greek god of the sea? ", "Poseidon"),
Question("What is the largest desert in the world? ", "Antarctica"),
Question("In which city is the Eiffel Tower located? ", "Paris"),
Question("Which gas is known as 'Laughing Gas'? ", "Nitrous oxide"),
Question("Who is the author of 'To Kill a Mockingbird'? ", "Harper Lee"),
Question("What is the national flower of Japan? ", "Cherry blossom"),
Question("What is the chemical symbol for oxygen? ", "O"),
Question("What is the primary function of the mitochondria in a cell? ", "Energy production"),
Question("What is the largest bird in the world? ", "Ostrich"),
Question("Who is the creator of the 'Harry Potter' series? ", "J.K. Rowling"),
Question("What is the capital of Brazil? ", "Brasília"),
Question("What is the chemical symbol for sodium? ", "Na"),
Question("What is the densest planet in our solar system? ", "Earth"),
Question("What is the main component of the Earth's core? ", "Iron"),
Question("Who is known as the 'Father of the Internet'? ", "Tim Berners-Lee"),
Question("What is the chemical symbol for carbon? ", "C"),
Question("What is the capital of India? ", "New Delhi"),
Question("Who painted the 'Sistine Chapel Ceiling'? ", "Michelangelo"),
Question("What is the chemical symbol for helium? ", "He"),
Question("What is the closest star to Earth (other than the Sun)? ", "Proxima Centauri"),
Question("What is the longest river in the world? ", "Nile River"),
Question("Who wrote 'The Great Gatsby'? ", "F. Scott Fitzgerald"),
Question("What is the currency of Russia? ", "Russian ruble"),
Question("What is the chemical symbol for lead? ", "Pb"),
Question("What is the main component of the Earth's atmosphere? ", "Nitrogen"),
Question("Who is the author of 'The Odyssey'? ", "Homer"),
Question("What is the national animal of China? ", "Giant panda"),
Question("What is the chemical symbol for potassium? ", "K"),
Question("What is the largest moon in the solar system? ", "Ganymede"),
Question("What is the fastest land animal in the world? ", "Cheetah"),
Question("Who painted the 'Last Supper'? ", "Leonardo da Vinci"),
Question("What is the chemical symbol for copper? ", "Cu"),
Question("What is the smallest planet in our solar system? ", "Mercury"),
Question("What is the main component of the Earth's crust? ", "Silicon"),
Question("Who is known as the 'Father of Modern Psychology'? ", "Sigmund Freud"),
Question("What is the chemical symbol for nitrogen? ", "N"),
Question("What is the capital of Canada? ", "Ottawa"),
Question("Who wrote 'The Iliad'? ", "Homer"),
Question("What is the national flower of India? ", "Lotus"),
Question("What is the chemical symbol for calcium? ", "Ca"),
Question("What is the second most abundant gas in the Earth's atmosphere? ", "Oxygen"),
Question("Who is the author of 'The Lord of the Rings' series? ", "J.R.R. Tolkien"),
Question("What is the currency of Canada? ", "Canadian dollar"),
Question("What is the chemical symbol for silicon? ", "Si"),
Question("What is the largest planet in the Milky Way galaxy? ", "Jupiter"),
Question("What is the highest mountain in the world? ", "Mount Everest"),
Question("Who is known as the 'Father of Modern Medicine'? ", "Hippocrates"),
Question("What is the chemical symbol for phosphorus? ", "P"),
Question("What is the national bird of the United States? ", "Bald eagle"),
Question("What is the chemical symbol for uranium? ", "U"),
Question("What is the smallest ocean in the world? ", "Arctic Ocean"),
Question("What is the national flower of the United States? ", "Rose"),
Question("What is the chemical symbol for silver? ", "Ag"),
Question("What is the capital of Australia? ", "Canberra"),
Question("Who is known as the 'Father of Geometry'? ", "Euclid"),
Question("What is the chemical symbol for aluminum? ", "Al"),
Question("What is the largest fish in the world? ", "Whale shark"),
Question("Who is the author of 'War and Peace'? ", "Leo Tolstoy"),
Question("What is the currency of Australia? ", "Australian dollar"),
Question("What is the chemical symbol for neon? ", "Ne"),
Question("What is the national animal of Australia? ", "Kangaroo"),
Question("What is the chemical symbol for sulfur? ", "S"),
Question("What is the longest mountain range in the world? ", "Andes"),
Question("Who is known as the 'Father of Western Philosophy'? ", "Socrates"),
Question("What is the chemical symbol for gold? ", "Au"),
Question("What is the most abundant gas in the Sun? ", "Hydrogen"),
Question("What is the chemical symbol for nitrogen? ", "N"),
Question("What is the capital of Egypt? ", "Cairo"),
Question("Who wrote 'Frankenstein'? ", "Mary Shelley"),
Question("What is the national flower of China? ", "Peony"),
Question("What is the chemical symbol for tin? ", "Sn"),
Question("What is the highest waterfall in the world? ", "Angel Falls"),
Question("Who is known as the 'Father of Modern Chemistry'? ", "Antoine Lavoisier"),
Question("What is the chemical symbol for mercury? ", "Hg"),
Question("What is the smallest continent in the world? ", "Australia"),
Question("What is the national bird of India? ", "Indian Peafowl"),
Question("What is the chemical symbol for magnesium? ", "Mg"),
Question("What is the deepest part of the ocean? ", "Mariana Trench"),
Question("Who is known as the 'Father of Microbiology'? ", "Louis Pasteur"),
Question("What is the chemical symbol for zinc? ", "Zn"),
Question("What is the capital of Germany? ", "Berlin"),
Question("Who wrote 'Dracula'? ", "Bram Stoker"),
Question("What is the national flower of Japan? ", "Cherry blossom"),
Question("What is the chemical symbol for barium? ", "Ba"),
Question("What is the largest moon of Saturn? ", "Titan"),
Question("What is the hottest planet in our solar system? ", "Venus"),
Question("Who is known as the 'Father of Modern Rocketry'? ", "Robert Goddard"),
Question("What is the chemical symbol for mercury? ", "Hg"),
Question("What is the largest desert in Asia? ", "Gobi Desert"),
Question("Who wrote 'The Adventures of Sherlock Holmes'? ", "Sir Arthur Conan Doyle"),
Question("What is the national animal of Russia? ", "Russian bear"),
Question("What is the chemical symbol for chromium? ", "Cr"),
Question("What is the fastest fish in the ocean? ", "Sailfish"),
Question("Who is known as the 'Father of the Constitution'? ", "James Madison"),
Question("What is the chemical symbol for palladium? ", "Pd"),
Question("What is the highest mountain in North America? ", "Denali (formerly Mount McKinley)"),
Question("What is the largest sea in the world? ", "Philippine Sea"),
Question("Who wrote 'The Grapes of Wrath'? ", "John Steinbeck"),
Question("What is the national bird of Russia? ", "Double-headed eagle"),
Question("What is the chemical symbol for iodine? ", "I"),
Question("What is the largest lake in Africa? ", "Lake Victoria"),
Question("Who is known as the 'Father of the Atomic Bomb'? ", "J. Robert Oppenheimer"),
Question("What is the chemical symbol for radium? ", "Ra"),
Question("What is the highest mountain in South America? ", "Aconcagua"),
Question("What is the largest island in the Mediterranean Sea? ", "Sicily"),
Question("Who wrote 'One Hundred Years of Solitude'? ", "Gabriel García Márquez"),
Question("What is the national flower of Russia? ", "Camomile"),
Question("What is the chemical symbol for cobalt? ", "Co"),
Question("What is the deepest lake in the world? ", "Lake Baikal"),
Question("Who is known as the 'Father of Psychoanalysis'? ", "Sigmund Freud"),
Question("What is the chemical symbol for bismuth? ", "Bi"),
Question("What is the highest mountain in Europe? ", "Mount Elbrus"),
Question("What is the largest desert in North America? ", "Chihuahuan Desert"),
Question("Who wrote 'Moby-Dick'? ", "Herman Melville"),
Question("What is the national bird of China? ", "Red-crowned crane"),
Question("What is the chemical symbol for antimony? ", "Sb"),
Question("What is the highest mountain in Africa? ", "Mount Kilimanjaro"),
Question("What is the largest island in the world? ", "Greenland"),
Question("Who is known as the 'Father of Western Medicine'? ", "Hippocrates"),
Question("What is the chemical symbol for tungsten? ", "W"),
Question("What is the highest mountain in Australia? ", "Mount Kosciuszko"),
Question("What is the largest reef system in the world? ", "Great Barrier Reef"),
Question("Who wrote 'The Picture of Dorian Gray'? ", "Oscar Wilde"),
Question("What is the national bird of Australia? ", "Emu"),
Question("What is the chemical symbol for platinum? ", "Pt"),
Question("What is the highest mountain in South Asia? ", "Kangchenjunga"),
Question("What is the largest island in Oceania? ", "New Guinea"),
Question("Who is known as the 'Father of Economics'? ", "Adam Smith"),
Question("What is the chemical symbol for vanadium? ", "V"),
Question("What is the highest mountain in Antarctica? ", "Mount Vinson"),
Question("What is the largest lake in North America? ", "Lake Superior"),
Question("Who wrote 'The Canterbury Tales'? ", "Geoffrey Chaucer"),
Question("What is the national bird of India? ", "Indian Peafowl"),
Question("What is the chemical symbol for manganese? ", "Mn"),
Question("What is the highest mountain in the Americas? ", "Aconcagua"),
Question("What is the largest coral atoll in the world? ", "Kiritimati"),
Question("Who is known as the 'Father of Botany'? ", "Theophrastus"),
Question("What is the chemical symbol for rhodium? ", "Rh"),
Question("What is the highest mountain in the Andes? ", "Aconcagua"),
Question("What is the largest lake in South America? ", "Lake Titicaca"),
Question("Who wrote 'The Art of War'? ", "Sun Tzu"),
Question("What is the national bird of Japan? ", "Green pheasant"),
Question("What is the chemical symbol for uranium? ", "U"),
Question("What is the highest mountain in the Western Hemisphere? ", "Aconcagua"),
Question("What is the largest fjord in the world? ", "Scoresby Sund"),
Question("Who is known as the 'Father of Taxonomy'? ", "Carl Linnaeus"),
Question("What is the chemical symbol for krypton? ", "Kr"),
Question("What is the highest mountain in the Southern Hemisphere? ", "Aconcagua"),
Question("What is the largest lake in Asia? ", "Caspian Sea"),
Question("Who wrote 'The Federalist Papers'? ", "Alexander Hamilton, James Madison, John Jay"),
Question("What is the national bird of Russia? ", "Russian bear"),
Question("What is the chemical symbol for rhodium? ", "Rh"),
Question("What is the highest mountain in the Southern Andes? ", "Aconcagua"),
Question("What is the largest river in South America? ", "Amazon River"),
Question("Who is known as the 'Father of Algebra'? ", "Al-Khwarizmi"),
Question("What is the chemical symbol for cerium? ", "Ce"),
Question("What is the highest mountain in the Alps? ", "Mont Blanc"),
Question("What is the largest salt flat in the world? ", "Salar de Uyuni"),
Question("Who wrote 'The Brothers Karamazov'? ", "Fyodor Dostoevsky"),
Question("What is the national bird of China? ", "Red-crowned crane"),


    ]

    score = 0

    for question in questions:
        if question.ask_question():
            print("Correct!")
            score += 1
        else:
            print("Wrong! You can quit by typing 'quit'.")
            user_input = input("Do you want to quit? (yes/no): ")
            if user_input.lower() == "yes":
                print("Game over! Your score is:", score)
                quit()

    print("Game over! Your score is:", score)

if __name__ == "__main__":
    main()
