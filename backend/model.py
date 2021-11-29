import torch
import transformers as tfmr

categories2 = [
    'Education', 'Entertainment', 'Food and Drink', 'Gift', 'Healthcare', 'Hobbies',
    'Home Rent', 'Household Item', 'Payment', 'Transportation', 'Travel', 'Income',
    'Shopping', 'Investment', 'Miscellaneous'
]

categories = ['Clothing', 'Communications', 'Education', 'Entertainment', 'Food and Drink',
              'Gift', 'Healthcare', 'Hobbies', 'Home', 'Rent', 'Transportation', 'Travel', 'Wedding']


class CategoryClassifier:
    def __init__(self):
        self.model_name = "category_classifier"
        self.model = None
        self.tokenizer = None

    def load_model(self):
        print('Loading model')
        self.tokenizer = tfmr.AutoTokenizer.from_pretrained(self.model_name)
        self.model = tfmr.AutoModelForSequenceClassification.from_pretrained(
            self.model_name, num_labels=len(categories))

    def eval_model(self):
        print('Evaluating model')
        self.model.eval()

    def tokenize(self, item_names):
        tokenized_input = self.tokenizer(
            item_names, padding="max_length", truncation=True, return_tensors="pt").to(self.model.device)
        with torch.no_grad():
            outputs = self.model(**tokenized_input)

        logits = outputs.logits
        predictions = torch.argmax(logits, dim=-1)
        pred_categories = [categories[pred_id] for pred_id in predictions]

        return pred_categories
