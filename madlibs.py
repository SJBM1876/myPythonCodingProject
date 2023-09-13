story_template = """Once upon a time in a [adjective] [noun],
there lived a [adjective] [animal]. 
This [animal] was known for its [adjective] [body part]. 
Every day, the [animal] would [verb] [adverb] through the [noun], 
searching for [plural noun]. 
One day, it stumbled upon a [adjective] [object] that was [verb]
with [color] [liquid]. The [animal] was [emotion] 
and decided to [verb] the [object]. Suddenly, 
the [object] [verb] and [verb]! 
The [animal] had a [adjective] adventure, and it learned that [lesson].
"""

def get_user_input(word_type):
    word = input(f"Enter a {word_type}: ")
    return word

def generate_mad_libs(story_template):
    adjective = get_user_input("adjective")
    noun = get_user_input("noun")
    animal = get_user_input("animal")
    body_part = get_user_input("body part")
    verb = get_user_input("verb")
    adverb = get_user_input("adverb")
    plural_noun = get_user_input("plural noun")
    object = get_user_input("object")
    color = get_user_input("color")
    liquid = get_user_input("liquid")
    emotion = get_user_input("emotion")
    lesson = get_user_input("lesson")

    mad_libs_story = story_template.format(
        adjective = adjective, noun = noun, animal = animal, body_part = body_part, verb = verb, adverb = adverb, plural_noun = plural_noun,
        object = object, color = color, liquid = liquid, emotion = emotion, lesson = lesson
    )

    return mad_libs_story

if __name__ == "__main__":
    print("Welcome to this great madlibs story.")
    generated_story = generate_mad_libs(story_template)
    print("\nYour Mad Libs story:")
    print(generated_story)


