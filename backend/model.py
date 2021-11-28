import torch
import transformers as tfmr

categories2 = {
    'Maintenance': ['Car', 'Home', 'Clothing'],
    'Education': ['Books'],
    'Entertainment': ['Movie', 'Concert', 'Games'],
    'Food and Drink': ['Groceries', 'Restaurants', 'Alcohol'],
    'Gift': ['Birthday', 'Wedding', 'Anniversary', 'Specal Occasion'],
    'Healthcare': ['Gym', 'Equipment', 'Pads', 'Drugs'],
    'Hobbies': ['Knitting', 'Painting', 'Sports', 'Plants'],
    'Home': ['Rent', 'Moving'],
    'Household Items': ['Toiletries', 'Laundry', 'Dishwash', 'Cleaning', 'Tools'],
    'Payments': ['Tax', 'Subscriptions', 'Government'],
    'Utilities': ['Cell', 'Internet', 'TV', 'Electricity'],
    'Transportation': ['Public Transit', 'Car Payment', 'Bike'],
    'Travel': ['Transit', 'Food', 'Shopping', 'Sightseeing'],
    'Income': ['Salary', 'Credit Card Payment'],
    'Shopping': ['Clothing', 'Accessories', 'Home Decor', 'Cosmetics', 'Stationery'],
    'Investment': ['Retirement', 'Savings']
}

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
