import csv_io
from model import CategoryClassifier
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.realpath(__file__))


class TransactionManager:
    def __init__(self, year, month):
        self.input_cc_path = '/input/'+str(year)+'_'+str(month)+'_cc.csv'
        self.input_chequing_path = '/input/' + \
            str(year)+'_'+str(month)+'_chequing.csv'
        self.input_questrade_path = '/input/' + \
            str(year)+'_'+str(month)+'_questrade.csv'
        self.input_wealthsimple_path = '/input/' + \
            str(year)+'_'+str(month)+'_wealthsimple.csv'
        self.merged_transactions_path = '/output/merged_' + \
            str(year)+'_'+str(month)+'.csv'
        self.categorized_transactions_path = '/output/categorized_' + \
            str(year)+'_'+str(month)+'.csv'
        self.merged_transactions = []
        self.sorted_transactions = []
        self.categorized_transactions = []

    def merge_inputs(self):
        cc_file = BASE_DIR+self.input_cc_path
        if os.path.isfile(cc_file):
            cc_t = csv_io.parse_cc_csv(cc_file)
            self.merged_transactions.extend(cc_t)

        chequing_file = BASE_DIR+self.input_chequing_path
        if os.path.isfile(chequing_file):
            chequing_t = csv_io.parse_chequing_csv(
                chequing_file)
            self.merged_transactions.extend(chequing_t)

    def sort_transactions_by_date(self):
        self.sorted_transactions = sorted(
            self.merged_transactions, key=lambda d: datetime.strptime(d['date'], '%m/%d/%Y'))

    def categorize_inputs(self):
        if self.sorted_transactions:
            c = CategoryClassifier()
            c.load_model()
            c.eval_model()
            transaction_names = [
                name for t in self.sorted_transactions for name in t['date']]
            pred_categories = c.tokenize(transaction_names)
            for transaction, category in zip(self.sorted_transactions, pred_categories):
                transaction['category'] = category
            self.categorized_transactions = self.sorted_transactions
            print('Sampling first categorized item: \n',
                  self.categorized_transactions[0])

    def write_categorized_transactions(self):
        csv_columns = ['date', 'vendor', 'price', 'category']
        csv_io.write_csv(BASE_DIR+self.categorized_transactions_path,
                         self.categorized_transactions, csv_columns)

    def get_categorized_transactions(self):
        self.categorized_transactions = csv_io.parse_categorized_csv(
            BASE_DIR+self.categorized_transactions_path)
