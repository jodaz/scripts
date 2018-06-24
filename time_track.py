import datetime
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.timedata
improvement_hours = db.improvement_hours

def ask_data():
    print("Add hours with format Work-College-Practice")
    data = input('>: ')
    return list(data)

def main():
    data = ask_data()
    current_date = datetime.date.today().strftime("%Y-%m-%d")

    document = {
        'date': current_date,
        'improvement_hours': [
            {
                'work_hours': data[0],
                'college_hours': data[1],
                'practice_hours': data[2]
            }
        ]
    }

    improvement_hours.insert_one(document)

main()
