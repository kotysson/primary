import OOPSA

class ChatBot:
    def __init__(self):
        self.sentiment_analyzer = OOPSA.SentimentAnalyzer()

    def _analyze_text(self, text):
        sentiment_score = self.sentiment_analyzer.analyze_sentiment(text)
        sentiment_class = self.sentiment_analyzer.classify_sentiment(sentiment_score)
        return sentiment_class

    def chat(self):

        while True:
            user_input = str(input()).lower()
            if user_input == 'exit':
                print('Chatbot: Goodbye!')
                break

            else:
                sentiment_class = self._analyze_text(user_input)
                response = self._generate_response(sentiment_class)
                print(f'Chatbot: {response}')

    def _generate_response(self, sentiment_class):
        if sentiment_class == 'Positive':
            return 'That is great to hear!'
        elif sentiment_class == 'Negative':
            return 'I am sorry to hear that. Can I help you with anything?'
        else:
            return 'Neutral response. How can I assist you?'

text_analyzer = ChatBot()
text_analyzer.chat()
