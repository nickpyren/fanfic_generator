import markovify


class FanficGenerator:
    def __init__(self):
        with open('./training_data/my_immortal_no_authors_notes.txt') as f:
            my_immortal_text = f.readlines()
        with open('./training_data/colours_of_the_kaze.txt', encoding='cp850') as f:
            colours_of_the_kaze_text = f.readlines()
        newline_texts = [my_immortal_text, colours_of_the_kaze_text]
        text_models = [markovify.NewlineText(text, state_size=2) for text in newline_texts]
        self.text_model = markovify.combine(text_models)

    def generate(self) -> str:
        fanfic = ""
        for chapter in range(1, 6):
            fanfic += f"\nChapter {chapter}\n"
            for sentence in range(10):
                fanfic += self.text_model.make_short_sentence(max_chars=250, tries=10000, max_overlap_ratio=0.6) + "\n"
        return fanfic
