import json


class DataLoader:
     def __init__(self, interesting_file_path = "app/data/newsgroups_interesting.json", not_interesting_file_path = "app/data/newsgroups_not_interesting.json"):
         self.interesting_file_path = interesting_file_path
         self.not_interesting_file_path = not_interesting_file_path



     def load_interesting_newsgroups(self):
         """Load interesting newsgroups data"""
         try:
             with open(self.interesting_file_path) as json_file:
                 data = json.load(json_file)

             return data
         except Exception as e:
             raise Exception(f"An error occurred while loading interesting newsgroups: {e}")


     def load_not_interesting_newsgroups(self):
            """Load not interesting newsgroups data"""
            try:
                with open(self.not_interesting_file_path) as json_file:
                    data = json.load(json_file)
                return data
            except Exception as e:
                raise Exception(f"An error occurred while loading not interesting newsgroups: {e}")




