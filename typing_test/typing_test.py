import time
import random

def calculate_wpm(word_count, time):
    wps = word_count / time
    wpm = wps * 60
    return wpm

def calculate_accuracy(original, typed):
    match_summary = [1 if w1==w2 else 0 for w1, w2 in zip(original, typed)]
    word_count = sum(match_summary)
    accuracy = word_count / len(original)
    
    return match_summary, word_count, accuracy

def typing_test():
    word_list = [
    # Medium-sized words
    "blanket", "vibrant", "cluster", "horizon", "package", 
    "weather", "glimmer", "pioneer", "journey", "storage", 
    "phantom", "gravity", "scholar", "browser", "vortex", 
    "harmony", "crystal", "justice", "morning", "whisper", 
    "network", "diamond", "capture", "monarch", "freedom", 
    "stadium", "kitchen", "picture", "desktop", "balance", 
    "venture", "element", "product", "genuine", "fragile", 
    "surface", "traffic", "vintage", "quality", "dynamic", 
    "captain", "miracle", "triumph", "speaker", "kingdom", 
    "habitat", "culture", "mystery", "instant", "organic",

    # Small words
    "cat", "sky", "run", "blue", "map", "oak", "sun", "ice",
    "fox", "gem", "lamp", "desk", "vibe", "glow", "fast",
    "pure", "gold", "leaf", "bird", "wind", "bold", "calm",

    # Prepositions (Small to Large)
    "at", "by", "in", "of", "on", "to", "up", "for", "off", 
    "via", "amid", "from", "into", "near", "onto", "over", 
    "past", "upon", "with", "about", "above", "after", "along", 
    "among", "below", "since", "under", "until", "across", 
    "before", "behind", "beside", "beyond", "during", "inside", 
    "toward", "within", "against", "beneath", "between", "despite", 
    "outside", "without", "regarding", "following", "including", 
    "throughout", "underneath", "concerning"
    ]
    while True:
        test_words = [random.choice(word_list) for _ in range(30)]
        test_string = " ".join(test_words)
        
        print("Start typing in...", end="", flush=True)
        time.sleep(1)
        print("3...", end="", flush=True)
        time.sleep(1)
        print("2...", end="", flush=True)
        time.sleep(1)
        print("1...", end="", flush=True)
        time.sleep(1)
        print("GO!!!\n")
        print(f"{test_string}\n--------------------------------------------------------\n")
        
        start_time = time.time()
        typed_string = input()
        end_time = time.time()
        test_time = end_time - start_time
        
        typed_words = typed_string.split(" ")
        
        match_summary, correct_word_count, accuracy = calculate_accuracy(test_words, typed_words)
        
        raw_score = calculate_wpm(len(typed_words), test_time)
        true_score = calculate_wpm(correct_word_count, test_time)
        
        print("\n\n-----------------------Results--------------------------")
        print(f"Total correct words typed: {correct_word_count}/{len(typed_words)} in {round(test_time, 2)} seconds.")
        print(f"Words Per Minute (Raw): {round(raw_score, 2)}")
        print(f"Words Per Minute (True): {round(true_score, 2)}")
        print(f"Accuracy: {accuracy*100}%")
        # print(f"Match Summary: {match_summary}")
        # print(f"Test_words: {test_words}. Count {len(test_words)}")
        # print(f"Typed_words: {typed_words}")
        
        again = input("Would you like to play again? (y,n): ")
        while again not in ["y", "n"]:
            again = input("Would you like to play again? (y,n): ")
        if again == "n":
            print("Thank you for Playing!\n")
            break
        else: continue
            

if __name__ == "__main__":
    typing_test()